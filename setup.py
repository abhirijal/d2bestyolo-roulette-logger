import pickle
from selenium import webdriver

# checks if its the first time
def checkcookies():
	try:
		filelen=pickle.load(open("Cookies.txt","rb"))
	except EOFError:
		filelen = ""
	if len(filelen) == 0:
		return "false"

#else sets up credentials

def setup(cpath,options):
 print ("You're not logged in. Checking auth.txt")
 creds = open("auth.txt","r")
 authline = creds.readline()
 for i in range (len(authline)):
    current_letter = authline[i:i+1]
    if current_letter == ":" :
    	mail = authline[0:i]
    	passwd = authline[i+1:]
    	print ("Success in getting credentials. Loggin in now")
 creds.close()
 driver = webdriver.Chrome(executable_path=cpath, chrome_options=options)  # Optional argument, if not specified will search path.
 driver.get('https://dota2bestyolo.com/user/account/login');
 print ("Opening D2BY")
 driver.find_element_by_id('email').send_keys(mail)
 driver.find_element_by_id('password').send_keys(passwd)
 print ("Loggin in")
 driver.find_element_by_id('login-button').click()
 if driver.find_element_by_id('verifycode') != 0:
 	code = input ("Please enter the code in your email. I am waiting ")
 driver.find_element_by_id('verifycode').send_keys(code)
 driver.find_element_by_id('login-button2').click()
 pickle.dump(driver.get_cookies() , open("Cookies.txt","wb"))
 print("Successfully logged in. Proceeding to the next step")
 driver.quit()
