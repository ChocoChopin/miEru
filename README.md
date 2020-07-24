# miEru

**miEru** (見える) *v.i.* to be seen; to be in sight  [Japanese]

miEru is a language-learning tool that does one thing extremely well: optically recognize text in the active window, and then send that text to the Windows clipboard.

This opens up a wealth of possibilities, chief of which for language learners is the ability to analyze scanned text with browser-based hover dictionaries such as Rikaikun.

Now, you can play your favorite games, classic or contemporary, in their original language and use them as a learning resource. Or you might just get through them where you otherwise couldn't. Things that are old become new again through the eyes of a student. 

# Setup




* Clipboard Inserter - Scans the clipboard, and when it detects an update, it inserts the result into the <body> of a local HTML file as a <p>aragraph. Open one of the included template HTML files in Chrome and enable the addon, or edit the CSS code of one of them to create your own. 
https://chrome.google.com/webstore/detail/clipboard-inserter/deahejllghicakhplliloeheabddjajm?hl=en


miEru uses Google Cloud's Vision API to perform OCR on the active window, and then convey the results of each call to the clipboard.


* Contains code written by Seth A. Robinson (seth@rtsoft.com) twitter: @rtsoft - Codedojo, Seth's blog
