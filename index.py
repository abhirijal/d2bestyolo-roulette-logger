import time
import pickle
import datetime
from selenium import webdriver
from setup import *
from getpoints import *
from functions import *
from localio import *

if checkcookies() == "false":
	setup(cpath,options)

cpath = "/home/user/chromdriver" # chromedriver path 

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
 

startingpoints = 100000 # starting points
nlist = [0,1,2,3,4,5,6,7,8,9,10] # just a dummy list
ppoints_status = "true" # set the points are correct

do = 0 # main loop 
inloop = 0 # inner loop



#main program starts here 
driver = webdriver.Chrome(executable_path=cpath, chrome_options=options)  # chrome webrdriver path.
driver.get('https://dota2bestyolo.com/rules'); # chrome initialize
for cookie in pickle.load(open("Cookies.txt", "rb")): # load the cookies file
	driver.add_cookie(cookie)


while do == 0:
	driver.get('https://dota2bestyolo.com/lottery'); # go to the website


	
	cline, ppoints_status = seperaterows(driver,nlist)
	chash = gethash(driver)
	print ("Hello",getusername(driver))
	print ("You currently have",getpoints(driver),"points")
	while inloop == 0 and ppoints_status == "true" :
		if chash != gethash(driver):
			time.sleep(1)
			nline, ppoints_status = seperaterows(driver,cline)
			color = getcol(nline[1])
			savetofile(color)
			chash = gethash(driver)
			cline = nline
		else:
			time.sleep(2) # sleep until it rolls






