# Word Prep (prototype)

`word_prep.py` is a CLI prototype that prepares a chapter vocabulary sheet from a plain text file.

## What it does

- Parses all English-like words from a `.txt` file.
- Normalizes words to root forms using Porter stemming (`nltk`).
- Uses the public [`wordfreq`](https://pypi.org/project/wordfreq/) library to read English frequency data.
- Filters output by a configurable rarity threshold.
- Outputs a CSV sorted by rarity (default) or order of appearance.
- Optionally fetches definitions from `dictionaryapi.dev`.

## Install

```bash
python3 -m pip install wordfreq nltk
```

## Usage

```bash
python3 word_prep.py ./chapter1.txt \
  --output chapter1_vocab.csv \
  --top 80 \
  --rarity-threshold 2.6 \
  --with-definitions
```

### Helpful flags

- `--order appearance` to follow chapter flow.
- `--min-length 6` to focus on longer tokens.
- `--min-count 2` to ignore one-off roots.
- `--rarity-threshold N` to tune rarity strictness (`rarity = 8 - zipf_frequency`).

## Notes

- Current version supports plain text input only.
- PDF/EPUB ingestion can be added next with a converter pipeline.
