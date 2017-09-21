############### Start healthChecks() ###############		
def healthChecks(arg, latestCheck = False):
	
	if latestCheck:
		latestProactiveCheck()
	os.system("/home/admin/proactive_check/proactive_check.pl "+arg)
	f = os.popen('cat hc_results.txt')
	print "Health checks Results\n ", f.read()
############### End healthChecks() ###############		
