import time
import pickle



def savetofile(color):
	myfile = open("log.txt","a")
	abc = str(time.ctime())
	text = color + " " + abc + "\n"
	myfile.write(text)
	myfile.close()