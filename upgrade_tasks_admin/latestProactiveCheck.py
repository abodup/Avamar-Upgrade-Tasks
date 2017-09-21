############### Start latestProactiveCheck() ###############
def latestProactiveCheck():

	pcsLatestVersion = "4.52"
	if not os.path.isdir("/home/admin/proactive_check"):
		print "proactive_check directory doesn't exist"
		os.makedirs("/home/admin/proactive_check")
		print "proactive_check directory created"	
	print "Found proactive_check directory"
	
	if not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
		print "proactive_checks.pl doesn't exist"
		print "trying to download the latest proactive_check.pl"
		os.system('curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O -o /home/admin/proactive_check/proactive_check.pl ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl')
		os.system('chmod a+x /home/admin/proactive_check/proactive_check.pl')
		print "Latest proactive_check.pl downloaded"
		while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
			question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
			if not query_yes_no(question): sys.exit() 
		
	else:
		print "proactive_checks.pl already file exists"
		f = os.popen('/home/admin/proactive_check/proactive_check.pl --version')
		if f.read()[-5:-1] != pcsLatestVersion:
			print "This script is not the latest"
			getProactiveCheck()
			print "Latest script is present"

############### End latestProactiveCheck() ###############
