from selenium import webdriver


def seperaterows(driver,tlist):
	pointsrwen = driver.find_elements_by_xpath('//*[@id="all-lottery"]/div[1]/div[2]/div[1]/div[3]/ul')[0]
	pointsrw = pointsrwen.text
	row = pointsrw
	fvalue = "false"
	nspace = 0
	for i in range(len(row)):
		cdigit = row[i:i+1]
		if cdigit == " ":
			nspace = nspace + 1
	
    # if nspace = 9 then store all the values:
	cspace = 0
	arn = 1
	atot = 0
	if nspace == 9:
		for i in range(len(row)):
			cdigit = row[i:i+1]
			if cdigit == " ":
				if cspace == 0:
					digit = row[:i]
					cspace = i
					tlist[arn] = digit
					arn = arn + 1
				else:
					digit = row[cspace+1:i]
					cspace = i
					tlist[arn] = digit
					arn = arn + 1
		if arn == 10:
			for i in range(len(row),1,-1):
				cdigit = row[i-1:i]
				if cdigit == " " and fvalue == "false":
					digit = row[i:]
					tlist[arn] = digit
					fvalue = "true"
	# elseif other values:
	else:
		for i in range(10,1,-1):
			tlist[i] = tlist[i-1]
		
		for j in range(10,1,-1):
			a = len(tlist[j])
			atot = atot + a

		aftot = atot + nspace
		faftot = len(row) - aftot
		fletter = row[:faftot]
		tlist[1] = fletter

	status = "true"

	#additional checks
	if nspace == 0:
		lastlet = tlist[10]
		lastletlen = len(lastlet)
		clastlet = row[len(row)-lastletlen:]
		if lastlet == clastlet:
			status = "true"
		else:
			status = "false"



	#testing the stored values
	return tlist,status
