# miEru

**miEru** (見える) *v.i.* to be seen; to be in sight  [Japanese]

miEru is a Windows-based language-learning tool that does one thing extremely well: optically recognize text in the active window, and then send that text to the Windows clipboard.

This opens up a wealth of possibilities, chief of which for language learners is the ability to analyze scanned text with browser-based hover dictionaries such as Rikaikun.

Now, you can play your favorite games, classic or contemporary, in their original language and use them as a learning resource. Or you might just get through them where you otherwise couldn't. Things that are old become new again through the eyes of a student. 

## Initial setup
No initial setup of miEru itself is required—simply unzip the miEru directory wherever you'd like to place it, and launch **miEru.exe**. You'll see its **見** icon appear in the system tray/notification area, which you can **right-click** to **exit** the program. When its **見** icon is visible in the system tray, miEru is active and will scan the active window when it detects hotkey presses—see usage below.

Should you want to use miEru as it was intended to be used, you'll need to install several browser addons, and optionally some hotkey software, to take full advantage of its capabilities.

## Browser addons
Browser addons provide critical augmentations to miEru's core functionality. Clipboard Inserter is used to get Japanese text from miEru into your browser, and rikaikun/Rikaichamp are used to analyze the text and define words. Open-as-Popup conveniently turns your browser window into a borderless one for easy viewing.

* **Clipboard Inserter** – Scans the clipboard, and when it detects an update, inserts the result into the &lt;body&gt; of a local HTML file as a &lt;p&gt;aragraph. Open one of the included template HTML files (located in the **/miEru/CSS Files** directory) in your browser (you can drag and drop for convenience, and furthermore create a bookmark), and then click the **Toggle clipboard inserter** button installed by the addon. To make it a little snappier, open its addon/extension options by right-clicking the icon and selecting **Options**, and lower the polling interval from **300ms** to the lowest setting of **100ms**—this means it checks for new clipboard contents every tenth of a second rather than every third of a second. This addon is available for both Chrome and Firefox.
https://chrome.google.com/webstore/detail/clipboard-inserter/deahejllghicakhplliloeheabddjajm?hl=en
https://addons.mozilla.org/en-US/firefox/addon/clipboard-inserter/

* **rikaikun** – A hover dictionary for Chrome, itself a port of Rikaichan. After installation, simply click the **理** icon it creates, and you'll see it overlayed with **On**. Note that sometimes, you might need to click the icon to activate rikaikun even when the **On** overlay is already visible. It's recommended that you open its extension options page (or simply right-click its icon and select **Options**)  and set its **popup delay** to **1ms**, so that it responds instantly when hovering. From here, you may also choose to disable all of the **Displayed information** checkboxes under **Kanji Dictionary**; I find that "Kanji components" is the only useful field. Note rikaikun's keyboard shortcuts shown on this page. When hovering over text, you can press the **Shift** key to change the displayed information, moving between the definition of a detected word or phrase, the information for the individual kanji selected, or the name dictionary (when applicable name kanji are detected). You can also press the **C** key to copy any hovered text.
https://chrome.google.com/webstore/detail/rikaikun/jipdnfibhldikgcjhfnomkfpcebammhp?hl=en

Should the included API key be expired by the time you begin using miEru yourself, you'll need to create your own—don't worry, it's very easy to do, and free if you're only using the service personally. Check the **Vision API setup** section below for details.

### Vision API setup
miEru uses Google Cloud's **Vision API** to perform OCR on the active window, the results of which miEru then conveys to the clipboard. This requires an **API key**, which is associated with a Google account. Users of the API are permitted a number of free calls per month, and are charged (only with permission) for any calls made beyond that limit. Google offers $300 of free Cloud credit upon signup. For convenience's sake, an **API key** is included with this distribution that was made especially for it—should its free $300 credit eventually dry up, you'll need to create your own key. This is trivially easy to do, only requires a payment method (which will likely never be charged provided the key is only for your own personal use), and is explained in detail below.

For more information, refer to https://cloud.google.com/vision/pricing

https://cloud.google.com/vision/docs/before-you-begin Log in to your Google account and open this page

https://prnt.sc/tnwnjd Click "Get started for free"

https://prnt.sc/tnvh6x Agree and continue

https://prnt.sc/tnvitn Activate free $300 credit by adding payment method

https://prnt.sc/tnvjqy

https://prnt.sc/tnvlpa Note that there's no charge unless automatic billing is enabled

https://cloud.google.com/free/docs/gcp-free-tier#always-free Vision is always-free per month below a certian number of calls

https://prnt.sc/tnw3dz I've made more than a thousand calls since development began, used less than $1 of free credit

https://prnt.sc/tnw8ib Go to the project selector page. It appears that Google automatically added some dummy projects to my account, but if it doesn't add them to yours, simply click "create project", type in a name, and you're good to go. 

https://prnt.sc/tnw9rr Enable the Vision API

https://prnt.sc/tnwafv Select the project you created, click "Continue"

https://prnt.sc/tnwbaj All we need is an API key, so click "API key"

https://prnt.sc/tnwccu It really shouldn't matter what you name your key. Click "Create".

https://prnt.sc/tnwpzz Copy the key to your clipboard with this button

After you've generated your API key, you'll need to navigate to the UGT folder within the miEru directory, and open "config.txt". Find the line "google_api_key|", and paste the key directly after the pipe, replacing the existing entry. Save, and you're finished.


## Special thanks
* Contains code written by Seth A. Robinson (seth@rtsoft.com) twitter: @rtsoft - Codedojo, Seth's blog
