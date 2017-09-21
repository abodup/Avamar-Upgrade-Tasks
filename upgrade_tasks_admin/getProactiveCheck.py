############### Start getProactiveCheck() ###############
def getProactiveCheck():
	
	print "trying to download the latest proactive_check.pl"
	os.system('curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O -o /home/admin/proactive_check/proactive_check.pl ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl')
	os.system('chmod a+x /home/admin/proactive_check/proactive_check.pl')
	print "Latest proactive_check.pl downloaded"
	while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
		question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
		if not query_yes_no(question): sys.exit() 
		
############### End getProactiveCheck()###############

