############### Start stopBackupMaintSched() ###############

def stopBackupMaintSched():
	
	message ="""
##################################################################
#                 Start stopBackupMaintSched                     #
##################################################################
"""
	printLog(message)
	# check if maintenence activities are running
	printBoth("check if maintenence activities are running")
	output = cmdOut("sudo -u admin status.dpn | egrep -A 2 checkpoint")
	lines = output.split('\n')
	if lines[0][-3:-1] == 'OK':
		printBoth("checkpoint 'OK'")
	if lines[1][-3:-1] == 'OK':
		printBoth("GC 'OK'")
	if lines[0][-3:-1] == 'OK':
		printBoth("hfscheck 'OK'")
	if (lines[0][-3:-1] == 'OK') and (lines[1][-3:-1] == 'OK') and (lines[2][-3:-1] == 'OK'):
		printBoth("Stopping Maintenence Scheduler")
		cmdOut("sudo -u admin dpnctl stop maint")
	output = cmdOut("sudo -u admin dpnctl status maint 2>&1")
	while output.split('\n')[-2].split()[-1]!= 'suspended.':
		question = """couldn't stop the Maintenece scheduler
please try manually and when done Press yes to continue or press no to quit"""
		if not query_yes_no(question): sys.exit() 
		output = cmdOut("sudo -u admin dpnctl status  2>&1")	
	
	printBoth("Stopping Backup Scheduler")
	cmdOut("sudo -u admin dpnctl stop sched")
	output = cmdOut("sudo -u admin dpnctl status sched 2>&1")
	while output.split('\n')[-2].split()[-1]!= 'down.':
		question = """couldn't stop the Backup scheduler
please try manually and when done Press yes to continue or press no to quit"""
		if not query_yes_no(question): sys.exit() 
		output = cmdOut("sudo -u admin dpnctl status sched 2>&1")
		printBoth("Backup and Maintenence schedulers are down")
	message ="""
##################################################################
#                  End latestProactiveCheck                      #
##################################################################
"""
	printLog(message)
############### End stopBackupMaintSched() ###############
