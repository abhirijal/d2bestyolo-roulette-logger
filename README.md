# d2bestyolo-roulette-logger
A Python Selenium bot which records roulette wins from D2BY. Uses chromium as selenium web driver.

## More info please?
This bot is for dota2bestlogs the current roulette color into a text file log.txt. This text file may be useful to analyze it's pattern which means $$$ XD. Work IN PROGRESS

## Requirments
 - Python 3
 - Selenium
 - Chromium web driver ( BELOW Chrome v73.0. Included in the repo )

## How to use.
Edit your credentials in auth.txt file. After the first run, you are free to delete the contents of this file BUT DO NOT DELETE THE FILE ITSELF. Your cookies are stored securely in cookies.txt

# How to view the recorded log?
 - See log.txt . Or you can specify your own file in localio.py

## How to change accounts?
 - Delete the cookies.txt file
 - Edit the auth.txt file
 
## How to disable headless mode?
Add # to line 16 in index.py

 

