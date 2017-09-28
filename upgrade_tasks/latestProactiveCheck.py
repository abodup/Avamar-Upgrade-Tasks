############### Start latestProactiveCheck() ###############
def latestProactiveCheck():
	message ="""
##################################################################
#                 Start latestProactiveCheck                     #
##################################################################
"""
	printLog(message)
	pcsLatestVersion = "4.52"
	printBoth("Latest proactive_check.pl version is %s" %pcsLatestVersion)
	if not os.path.isdir("/home/admin/proactive_check"):
		printBoth("proactive_check directory doesn't exist")
		#as used admin
		os.makedirs("/home/admin/proactive_check")
		# return to root
		printBoth("proactive_check directory created")
	else: printBoth("Found proactive_check directory")
	if not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
		printBoth("proactive_checks.pl doesn't exist")
		printBoth("trying to download the latest proactive_check.pl")
		printLog("Command: sudo -u admin curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl")
		os.system('sudo -u admin curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl')
		printLog("Command: sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl")
		os.system('sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl')
		
		while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
			printLog("Check if proactive_check.pl file is downloaded")
			question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
			if not query_yes_no(question): sys.exit() 
			
		printBoth("Latest proactive_check.pl downloaded")
	else:
		printBoth("proactive_checks.pl already file exists")
		printLog("Checking proactive_check.pl version is latest")
		printLog("Command: sudo -u admin /home/admin/proactive_check/proactive_check.pl --version")
		f = os.popen('sudo -u admin /home/admin/proactive_check/proactive_check.pl --version')
		output = f.read()
		printLog("Output: %s" %output)
		if output[-5:-1] != pcsLatestVersion:
			printBoth("proactive_check.pl script version is %s which is not the latest" %output[-5:-1])
			printBoth("trying to download the latest proactive_check.pl")
			os.system('curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O -o /home/admin/proactive_check/proactive_check.pl ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl')
			os.system('chmod a+x /home/admin/proactive_check/proactive_check.pl')
			print "Latest proactive_check.pl downloaded"
			while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
				question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
				if not query_yes_no(question): sys.exit() 

			print "Latest script is present"
	message ="""
##################################################################
#                  End latestProactiveCheck                      #
##################################################################
"""
	printLog(message)
############### End latestProactiveCheck() ###############
