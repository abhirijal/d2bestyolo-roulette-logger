from selenium import webdriver

# fetch round hash
def gethash(driver):
	hashen = driver.find_element_by_id('roundHash')
	chash = hashen.text	
	return chash

# fetch current points
def getpoints(driver):
	pointsen = driver.find_elements_by_class_name('user-coin')
	return pointsen[0].text

# get username
def getusername(driver):
	unameen = driver.find_elements_by_xpath('//*[@id="your-id"]/span[1]')
	usernm = unameen[0].text
	return usernm

# get color from number
def getcol(num):
	num = int(num)
	if num == 0:
		color = "G"
	elif num <= 7:
		color = "B"
	else:
		color = "R"
	return color

# place bet ( experimental )
def placebet(driver,color,value):
	driver.find_element_by_id('coins-input-value').send_keys(value)
	driver.find_elements_by_xpath('//*[@id="all-lottery"]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/ul/li[1]')[0].click()

