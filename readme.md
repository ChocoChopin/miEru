# miEru

###### ***見える*** *v.i. to be seen; to be in sight*

miEru is a Windows-based language-learning tool that does one thing extremely well: optically recognize text in the active window, and then send that text to the Windows clipboard.

This opens up a wealth of possibilities, chief of which for language learners is the ability to analyze scanned text with browser-based hover dictionaries such as Rikaikun.

Now, you can play your favorite games, classic or contemporary, in their original language and use them as a learning resource. Old things become new again through the eyes of a student, and almost everything is more enjoyable and engaging when you're learning.

![Alt](https://iili.io/dIugQs.png "Does &quot;iconic&quot; even begin to describe it?")

## Setup summary
###### *No, I will not read your novella*
If you're short on time, follow these basic steps for getting started.

1. Extract **miEru.zip** anywhere you'd like
2. Install the browser addons [rikaikun](https://chrome.google.com/webstore/detail/rikaikun/jipdnfibhldikgcjhfnomkfpcebammhp?hl=en) (or [Rikaichamp for Firefox](https://addons.mozilla.org/en-US/firefox/addon/rikaichamp/)), [Clipboard Inserter](https://chrome.google.com/webstore/detail/clipboard-inserter/deahejllghicakhplliloeheabddjajm?hl=en) (or [for Firefox](https://addons.mozilla.org/en-US/firefox/addon/clipboard-inserter/)), and [Open-as-Popup](https://chrome.google.com/webstore/detail/open-as-popup/ncppfjladdkdaemaghochfikpmghbcpc?hl=en) (or [Popup window for Firefox](https://addons.mozilla.org/en-US/firefox/addon/popup-window/))
3. Navigate to **/miEru/CSS Files/** and open one of the provided HTML files by dragging and dropping it into your browser window
4. Toggle the dictionary and clipboard extensions on so that they look like [this](https://prnt.sc/tofam6); press the Open-as-Popup extension button to get rid of the window frame if you want
5. Run **miEru.exe**; you'll see its **見** taskbar icon appear
6. Select the window of whatever you want to capture, and press **Ctrl + F12**; captured text appears at the top of the browser window
7. Contemplate the **real value** of your time, and reevaluate any commitments that may be interfering with your ability to read verbose documentation

> Can't be arsed to click on all that stuff? Click on [**this**](https://www.dropbox.com/s/ucr41hrljggg890/Firefox%20miEru.zip?dl=1) instead, for a portable version of Firefox with the addons already installed. 

## Initial setup
###### *Let's get one thing straight*
No initial setup of miEru itself is required—simply unzip the miEru folder wherever you'd like to place it, and launch **miEru.exe**. You'll see its **見** icon appear in the system tray/notification area, which you can **right-click** to **exit** the program. When its **見** icon is visible in the system tray, miEru is active and will scan the active window when it detects hotkey presses—see usage below.

Should you want to use miEru as it was intended to be used, you'll need to install several browser addons, and optionally some hotkey software, to take full advantage of its capabilities.

>**Note:** Should the included API key be expired by the time you begin using miEru yourself, you'll need to create your own—don't worry, it's very easy to do, and free if you're only using the service personally. Check the [**Vision API setup**](https://github.com/ChocoChopin/miEru/blob/master/readme.md#vision-api-setup) section below for details.

## Browser addons
###### *By your powers combined...*
Browser addons provide critical augmentations to miEru's core functionality. **Clipboard Inserter** is used to get Japanese text from miEru into your browser, and **rikaikun/Rikaichamp** are used to analyze the text and define words and expressions. **Open-as-Popup** conveniently turns your browser window into a borderless one for easy viewing.

* **Clipboard Inserter** – Scans the clipboard, and when it detects an update, inserts the result into the &lt;body&gt; of a local HTML file as a &lt;p&gt;aragraph. Open one of the included template HTML files (located in the **/miEru/CSS Files/** directory) in your browser (you can drag and drop for convenience, and furthermore create a bookmark), and then click the **Toggle clipboard inserter** button installed by the addon, which you'll then see overlayed with **ON**. To make it a little snappier, open its addon/extension options by right-clicking the icon and selecting **Options**, and lower the polling interval from **300ms** to the lowest possible setting of **100ms**—this means it checks for new clipboard contents every tenth of a second rather than every third of a second. This addon is available for both Chrome and Firefox.  
  * [Clipboard Inserter for Chrome](https://chrome.google.com/webstore/detail/clipboard-inserter/deahejllghicakhplliloeheabddjajm?hl=en)  
  * [Clipboard Inserter for Firefox](https://addons.mozilla.org/en-US/firefox/addon/clipboard-inserter/)  
  
* **rikaikun** – A hover dictionary for Chrome, itself a port of Rikaichan. After installation, simply click the **理** icon it creates, and you'll see it overlayed with **On**. Note that sometimes, you might need to click the icon to activate rikaikun even when the **On** overlay is already visible. It's recommended that you open its extension options page (or simply right-click its icon and select **Options**)  and set its **popup delay** to **1ms**, so that it responds instantly when hovering. From here, you may also choose to disable all of the **Displayed information** checkboxes under **Kanji Dictionary**; I find that "Kanji components" is the only useful field. Note rikaikun's keyboard shortcuts shown on this page. When hovering over text, you can press the **Shift** key to change the displayed information, moving between the definition of a detected word or phrase, the information for the individual kanji selected, or the name dictionary (when applicable name kanji are detected). You can also press the **C** key to copy any hovered text.  
  * [rikaikun for Chrome](https://chrome.google.com/webstore/detail/rikaikun/jipdnfibhldikgcjhfnomkfpcebammhp?hl=en)

* **Rikaichamp** – A hover dictionary for Firefox, itself a port of rikaikun. The above guidelines for rikaikun also apply to Rikaichamp, as its functionality and options are largely identical.  
  * [Rikaichamp for Firefox](https://addons.mozilla.org/en-US/firefox/addon/rikaichamp/)

* **Open-as-Popup** – Transforms the current browser window or tab into a separate window without browser UI elements, ideal for eliminating distractions and focusing on text. Once you install the addon, it'll create a unique-looking [icon](https://prnt.sc/tog0zt) ([Firefox](https://prnt.sc/tog1gf)) with a green arrow—click this to activate the current window or tab, and if you'd like to return the popup window back to where it was, you can right-click within it and [select](https://prnt.sc/tog1zn) **Toggle Open-as-Popup**.  
  * [Open-as-Popup for Chrome](https://chrome.google.com/webstore/detail/open-as-popup/ncppfjladdkdaemaghochfikpmghbcpc?hl=en)
  * [Popup window for Firefox](https://addons.mozilla.org/en-US/firefox/addon/popup-window/)

## Usage
###### *When the only tool you have is an OCR API, everything looks like parsable text*
miEru is activated by a keyboard **capture hotkey combination**—by default, this is **Ctrl + F12**, but can be changed by modifying the **hotkey_to_scan_active_window** parameter in **/miEru/UGT/config.txt**. When miEru detects this combo, it takes a screenshot of the active window, sends the screenshot to the **Vision API**, receives the textual result of the API call, parses the result, and then forwards it to the clipboard for viewing in the browser window.

### Set up the browser window
An empty local HTML file will work, but retro JRPG-styled window templates are included in **/miEru/CSS Files/**. Notably, these files contain carefully-designed CSS code to ensure text is displayed in a form optimal for the way miEru presents it. You can easily edit them yourself and style text to your liking. Simply drag and drop the desired HTML file into a browser window, and it'll open as a new tab. From there, enable **Clipboard Inserter** and **rikaikun/Rikaichamp**, optionally turn the window into a popup using **Open-as-Popup**, and you're ready for immersive learning.

### Begin capturing
Run the content you wish to capture—typically, a retro game running in an emulator, or a PC game with Japanese text—and press the **capture hotkey**. You'll see the text captured by the API appear in the browser window you prepared—typically, each call takes under two seconds, sometimes as little as one, but speed can vary depending on API server load and complexity of the scanned image. Note that the desired window must be selected and active for it to be captured—**rikaikun** will still work even if the browser window is inactive, so you can hover over text without deselecting the desired window. If you're using the included HTML files, captured text will appear at the top of the browser window as to prevent the necessity of scrolling down for each new line of text. 

## Optional tools
###### *To whom it may concern*
Several optional tools can provide extensibility for activating hotkeys. Save yourself the tedium of shuttling between the keyboard and gamepad for every line of text.

* **DS4Win** – If you own a DualShock 4 controller, this might be your preferred way to play retro games, both because of the DS4's unrivaled D-pad and because DS4Win has excellent support for macros and hotkeys, in addition to a staggering number of additional useful features such as gyroscopic mouse control. Its home site provides good documentation, and the application itself is very easy to use. By selecting individual controller buttons within the profile configuraiton, it's possible to create macro assignments for each one; in my own setup, I use the left trigger for the **capture hotkey**, and the right trigger for the **capture hotkey** plus an additional **confirm button press**, slightly delayed. When proceeding through many dialogue boxes, it's often easier to use the latter function to perform a capture and advance to the next dialogue box at the same time. Shown is the DS4Win macro setup used, with the timings manually adjusted for accuracy. Check **Record Delays**, perform the macro, save it, and then click on the timing boxes to adjust them afterward. [Example](https://prnt.sc/to0lt4)
  * [Ryochan's fork of DS4Win](https://ryochan7.github.io/ds4windows-site/)
  
* **AutoHotkey** – Arguably among the most useful Windows utilities ever created, AutoHotkey provides a simple-yet-sophisticated system for creating and using keyboard macros. Not only can its macros be used to interact with the Windows API in almost any way imaginable, for our purposes, AutoHotkey also takes input from connected gamepads, meaning that a **gamepad button** can be macroed to the **capture hotkey**. In this case, its only limitation is that unlike DS4Win, its macros cannot simulate gamepad button input—so you'll need to press the confirm button in addition to the capture button each time. Included in **/miEru/AutoHotkey scripts/** are **Controller hotkey template** and **Gamepad test script**. After installing AutoHotkey, first run the test script, which will produce a tooltip next to the cursor. This provides live feedback about gamepad input. The device itself will appear as **1joy**, and potentially as anything up to **4joy** or more depending on how many gamepads you have configured. Captured inputs will appear as **1joy7**, with the second number corresponding to the button pressed. Run the template script, and then edit it by right-clicking on its system tray/notification area icon. Modify each of the macro entries to reflect the desired device and button as shown [here](https://prnt.sc/to1dsa), save the file in the editor, and then choose **Reload script** from the system tray icon's menu. The configured button will now perform miEru captures. Exit the test script using its own system tray icon.  
  * [AutoHotkey](https://www.autohotkey.com/)

## Configuration options
###### *For those who like to switch things up*
miEru's functionality is simple and straightforward, but nonetheless, there're several important options you can configure depending on the circumstance.

#### Preserve spacing
By default, miEru removes spaces from Japanese text; **Vision** actively inserts spaces into text it processes, and usually does so grammatically correctly, but often enough, spaces will be inserted in the middle of words or phrases, rendering **rikaikun** unable to detect them properly. For **kana-only** games, it may prove useful to preserve spaces instead. To enable this feature, navigate to **/miEru/UGT/**, open **config.txt**, and find the line **preserveSpacing|**; change **0** to **1**, then save the file.

#### Junk detection
**Vision** will often see random characters where there aren't any, and it'll usually detect the window buttons as "OX" or some version thereof. miEru filters these chunks of text out if they're below a specified length in bytes. The **junkLength|** parameter allows you to change the minimum required size for dialogue. The default setting is 8, and this filters nearly all such junk while preserving virtually all dialogue detection.

#### Keyword filtering
**Vision** detects the text of title bars, menu bars, and status bars as well. This text is often long enough to make it past the junk filter. If you wish to filter out these blocks of text specifically, you can specify up to three keywords using the **titlebarName|**, **menubarName|**, and **statusbarName|** parameters in **config.txt**. Be verbose—any block of text *containing* the entire keyword will be filtered out. For example, "Paint" will filter out any block containing that whole word, but "P" will filter out any block containing any instance of the letter "P". These parameters are case-sensitive.

## Known issues
###### *Caveat emptor*
Even with the power of 21st century robot vision at your behest, you'll encounter some quirks sooner or later. Fortunately, none of these problems are serious, and they should only rarely impede your ability to enjoy your content.

#### Inconsistent character recognition
Occasionally, you'll notice that the same character is interpreted in two different ways, seemingly arbitrarily. You'll just have to use your human vision in such cases.
![Alt](https://iili.io/dIuP44.png "&quot;Madou&quot;? &quot;Haidou&quot;? Little from column A, little from column B?")
> Google's **Vision API** is remarkably accurate—probably nearly 99% accurate—but even it is occasionally brought to its knees by the horrors of 16-bit-era kanji

#### No recognition
In some instances, **Vision** won't pick up anything at all. In this screencap, text filtering has been entirely disabled—the only things seen are the title bar and window buttons. Oddly, if the screencap itself is zoomed in on and scanned, recognition is accurate. The mind of the bot is inscrutable. Try resizing the window and performing a capture again.
![Alt](https://iili.io/dTHxlj.png)
> "成功"? More like 故障.

## Vision API setup
miEru uses Google Cloud's **Vision API** to perform OCR on the active window, the results of which miEru then conveys to the clipboard. This requires an **API key**, which is associated with a Google account. Users of the API are permitted a number of free API calls per month, and are charged (only with permission) for any calls made beyond that limit. Google offers $300 of free Cloud credit upon signup. For convenience's sake, an **API key** is included with this distribution, which was made especially for it—should its free $300 credit eventually dry up, you'll need to create your own key. This is trivially easy to do, only requires a payment method (which will likely never be charged, provided the key is only for your own personal use), and is explained in detail below.

* Log in to your Google account and open [this page](https://cloud.google.com/vision/docs/before-you-begin)

* [Click "Get started for free"](https://prnt.sc/tnwnjd)

* [Agree and continue](https://prnt.sc/tnvh6x)

* [Activate free $300 credit by adding payment method](https://prnt.sc/tnvitn) 

* [Agree to the terms and continue](https://prnt.sc/tnvjqy) 

* [Note that there's no charge unless automatic billing is enabled](https://prnt.sc/tnvlpa) 

* Vision is [always-free](https://cloud.google.com/free/docs/gcp-free-tier#always-free) per month below a certian number of calls. For more information, refer to https://cloud.google.com/vision/pricing

* [1400 calls, less than $1](https://prnt.sc/tnw3dz) 

* [Go to the project selector page.](https://prnt.sc/tnw8ib) It appears that Google automatically added some dummy projects to my account, but if it doesn't add them to yours, simply click "create project", type in a name, and you're good to go. 

* [Enable the Vision API](https://prnt.sc/tnw9rr) 

* [Select the project you created, click "Continue"](https://prnt.sc/tnwafv) 

* [All we need is an API key, so click "API key"](https://prnt.sc/tnwbaj) 

* [It really shouldn't matter what you name your key. Click "Create".](https://prnt.sc/tnwccu)

* [Copy the key to your clipboard with this button](https://prnt.sc/tnwpzz) 

After you've generated your API key, you'll need to navigate to the UGT folder within the miEru directory, and open **config.txt**. Find the line **google_api_key|**, and paste the key directly after the pipe, replacing the existing entry. Save, and you're finished.


## Special thanks
* Contains code written by Seth A. Robinson (seth@rtsoft.com) twitter: @rtsoft - [Codedojo](https://www.codedojo.com/), Seth's blog
* Based on project [Ultimate Game Translator](https://github.com/SethRobinson/UGT)
