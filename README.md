# d2bestyolo-roulette-logger
A Python Selenium bot which records roulette wins from D2BY. Uses chromium as the web driver.

## More info please?
This bot is for dota2bestyolo's roulette game. It has only 3 possible colors. It logs the current roulette color into a text file log.txt. This text file may be useful to analyze it's pattern / to check if the game actually stands up to it's 'fairness'. Work IN PROGRESS

## Requirments
 - Python 3
 - Selenium
 - Chromium web driver ( BELOW Chrome v73.0. Included in the repo )

## How to use.
 - Edit your credentials in auth.txt file. After the first run, you are free to delete the contents of this file BUT DO NOT DELETE
 THE FILE ITSELF. Your cookies are stored securely in cookies.txt.
  - Open index.py


# How to view the recorded log?
 - See log.txt . Or you can specify your own file in localio.py

## How to change accounts?
 - Delete the cookies.txt file
 - Edit the auth.txt file
 
## How to disable headless mode?
Add # to line 16 in index.py

Please note : I do not promote or encourage any kind of gambling habit. This bot was just made to record the roulette game with the effort to know how fair the game is.

 

