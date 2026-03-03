#!/usr/bin/env python3
"""Generate a pre-reading vocabulary list from plain-text files.

This tool extracts words, normalizes them to root-ish forms, scores rarity using the
public `wordfreq` library, and outputs a sorted study sheet.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from nltk.stem import PorterStemmer
from wordfreq import zipf_frequency

TOKEN_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
STEMMER = PorterStemmer()


@dataclass
class WordEntry:
    root: str
    count: int
    first_index: int
    rarity_score: float
    zipf: float
    forms: str
    definition: str | None = None


def extract_words(text: str) -> list[str]:
    return [m.group(0).lower() for m in TOKEN_RE.finditer(text)]


def root_form(word: str) -> str:
    # Porter stemming is lightweight and deterministic, suitable for grouping
    # inflected forms (e.g., "running", "runs" -> "run").
    return STEMMER.stem(word)


def rarity_from_zipf(zipf: float) -> float:
    # Lower Zipf frequency means rarer words.
    return max(0.0, 8.0 - zipf)


def rank_words(
    words: Iterable[str],
    min_length: int,
    min_count: int,
    rarity_threshold: float,
) -> list[WordEntry]:
    words = list(words)
    grouped: dict[str, list[tuple[int, str]]] = {}
    for i, token in enumerate(words):
        if len(token) < min_length:
            continue
        root = root_form(token)
        grouped.setdefault(root, []).append((i, token))

    entries: list[WordEntry] = []
    for root, occurrences in grouped.items():
        count = len(occurrences)
        if count < min_count:
            continue

        zipf = zipf_frequency(root, "en")
        rarity = rarity_from_zipf(zipf)
        if rarity < rarity_threshold:
            continue

        forms = sorted({token for _, token in occurrences})
        first_index = min(i for i, _ in occurrences)
        entries.append(
            WordEntry(
                root=root,
                count=count,
                first_index=first_index,
                rarity_score=rarity,
                zipf=zipf,
                forms=", ".join(forms),
            )
        )

    entries.sort(key=lambda e: (-e.rarity_score, -e.count, e.first_index))
    return entries


def fetch_definition(word: str, timeout_s: float = 3.0) -> str | None:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{urllib.parse.quote(word)}"
    req = urllib.request.Request(url, headers={"User-Agent": "word-prep/0.2"})
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError):
        return None

    if not isinstance(payload, list) or not payload:
        return None

    meanings = payload[0].get("meanings")
    if not meanings:
        return None
    for meaning in meanings:
        defs = meaning.get("definitions")
        if defs and isinstance(defs, list) and defs[0].get("definition"):
            return defs[0]["definition"]
    return None


def write_csv(entries: list[WordEntry], output: Path) -> None:
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["root", "forms_seen", "count", "first_word_index", "zipf_frequency", "rarity_score", "definition"])
        for e in entries:
            writer.writerow([e.root, e.forms, e.count, e.first_index, f"{e.zipf:.2f}", f"{e.rarity_score:.2f}", e.definition or ""])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a pre-reading list of rare words from a text file.")
    parser.add_argument("input", type=Path, help="Input plain text file (.txt)")
    parser.add_argument("--output", type=Path, default=Path("vocab.csv"), help="Output CSV path")
    parser.add_argument("--top", type=int, default=40, help="Maximum number of words to output")
    parser.add_argument("--min-length", type=int, default=5, help="Minimum token length to include")
    parser.add_argument("--min-count", type=int, default=1, help="Minimum occurrences per root to include")
    parser.add_argument(
        "--rarity-threshold",
        type=float,
        default=2.2,
        help="Minimum rarity score (0-8). Higher means rarer words only.",
    )
    parser.add_argument("--order", choices=["rarity", "appearance"], default="rarity", help="Ordering mode")
    parser.add_argument("--with-definitions", action="store_true", help="Fetch short definitions from dictionaryapi.dev")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = args.input.read_text(encoding="utf-8", errors="ignore")
    words = extract_words(text)
    entries = rank_words(
        words,
        min_length=args.min_length,
        min_count=args.min_count,
        rarity_threshold=args.rarity_threshold,
    )

    if args.order == "appearance":
        entries.sort(key=lambda e: e.first_index)

    entries = entries[: args.top]
    if args.with_definitions:
        for e in entries:
            e.definition = fetch_definition(e.root)

    write_csv(entries, args.output)
    print(f"Wrote {len(entries)} entries to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
