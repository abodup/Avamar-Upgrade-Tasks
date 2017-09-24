############### Start main() ###############
def main():
	setupLog()
	prePostTech, targetVersion , revNo, currentVersion = getArgs()
	if prePostTech == "preUpgrade":
		printBoth("Executing PreUpgrade Tasks")
		preUpgradeTasks()
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
