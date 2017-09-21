############### Start extraChecks() ###############

def extraChecks():
	
	print "Starting Extra Checks"
	
	print "Checking Avamar Internal Root & MCUser Password"
	passwd = False 
	while not passwd:
		rootPass = getInput("Enter Avamar Internal Root Password: ")
		f = os.popen("avmgr logn --id=root --password=%s 2>&1" %rootPass)
		lines = f.read().split('\n')
		if lines[0][0] == '1' : 
			passwd = True
			print "Correct Avamar Internal Root Password "
			
		else:
			print "Incorrect Avamar Internal Root Password"
	
	passwd = False 
	while not passwd:
		MCUserPass = getInput("Enter MCUser Password: ")
		f = os.popen("avmgr logn --id=MCUser --password=%s 2>&1" %MCUserPass)
		lines = f.read().split('\n')
		if lines[0][0] == '1' : 
			passwd = True
			print "Correct Avamar MCUser Password "
			
		else:
			print "Incorrect Avamar MCUser Password"

	f = os.popen("egrep 'smtp|sender' /usr/local/avamar/var/mc/server_data/prefs/mcserver.xml 2>&1")
	lines = f.read().split('\n')
	smtp = lines[0].split()[-2].split('=')[1].translate(None,'"')
	sender = lines[1].split()[-2].split('=')[1].translate(None,'"')
	
	print "SMTP host is" + smtp
	print "email sender is" + sender
	
############### End extraChecks() ###############
