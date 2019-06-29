import time
import pickle

# writes to the file log.txt

def savetofile(color):
	myfile = open("log.txt","a")
	abc = str(time.ctime())
	text = color + " " + abc + "\n"
	myfile.write(text)
	myfile.close()
