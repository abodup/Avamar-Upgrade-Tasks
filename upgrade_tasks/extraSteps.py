############### Start extraSteps() ###############
def extraSteps():
	
	printBoth("Starting Extra Checks")
	
	printBoth("Checking Avamar Internal Root & MCUser Password")
	passwd = False 
	while not passwd:
		rootPass = getInput("Enter Avamar Internal Root Password: ")
		output = cmdOut("avmgr logn --id=root --password=%s 2>&1" %rootPass)
		lines = output.split('\n')
		if lines[0][0] == '1' : 
			passwd = True
			print "Correct Avamar Internal Root Password "
			
		else:
			print "Incorrect Avamar Internal Root Password"
	
	passwd = False 
	while not passwd:
		MCUserPass = getInput("Enter MCUser Password: ")
		output = cmdOut("avmgr logn --id=MCUser --password=%s 2>&1" %MCUserPass)
		lines = output.split('\n')
		if lines[0][0] == '1' : 
			passwd = True
			print "Correct Avamar MCUser Password "
			
		else:
			printBoth("Incorrect Avamar MCUser Password")

	output = cmdOut("egrep 'smtp|sender' /usr/local/avamar/var/mc/server_data/prefs/mcserver.xml 2>&1")
	smtp = output.split('\n')[0].split()[-2].split('=')[1].translate(None,'"')
	sender = output.split('\n')[1].split()[-2].split('=')[1].translate(None,'"')
	
	printBoth("SMTP host is " + smtp)
	printBoth("email sender is" + sender)	
############### End extraSteps() ###############
