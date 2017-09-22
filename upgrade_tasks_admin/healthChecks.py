############### Start healthChecks() ###############		
def healthChecks(arg, latestCheck = False):
	
	if latestCheck:
		latestProactiveCheck()
	os.system("sudo -u admin /home/admin/proactive_check/proactive_check.pl "+arg)
	f = os.popen('sudo -u cat hc_results.txt')
	print "Health checks Results\n ", f.read()
############### End healthChecks() ###############		
