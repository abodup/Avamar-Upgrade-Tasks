############### Start main() ###############
def main():
	setupLog()
	prePostTech, targetVersion , revNo, currentVersion = getArgs()
	if prePostTech == "preUpgrade":
		printBoth("Executing PreUpgrade Tasks")
		#verifyRevNo is correct
		#verify Files are present
		latestProactiveCheck()
		os.system("sudo -u admin /home/admin/proactive_check/proactive_check.pl "+arg)
		f = os.popen('sudo -u cat hc_results.txt')
		print "Health checks Results\n ", f.read()
		question = """Depending on the output of the health checks, if the health checks are clean press yes to continue
if health checks are not clean press no to exit"""
		if not query_yes_no(question): sys.exit()
		#stopBackupMaintSched()
		#extraChecks()


	elif prePostTech == "postUpgrade":
		printBoth("Executing PostUpgrade Tasks")
		#preUpgradeTasks()
	message ="""
##################################################################
#                  End upgrade_tasks.py Script                   #
##################################################################
"""
	printLog(message)
############### End main() ###############
