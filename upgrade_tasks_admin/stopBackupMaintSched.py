############### Start stopBackupMaintSched() ###############

def stopBackupMaintSched():

	# check if maintenence activities are running
	print "check if maintenence activities are running"
	f = os.popen("status.dpn | egrep -A 2 checkpoint")
	lines = f.read().split('\n')
	if lines[0][-3:-1] == 'OK':
		print "checkpoint 'OK'"
	if lines[1][-3:-1] == 'OK':
		print "GC 'OK'"
	if lines[0][-3:-1] == 'OK':
		print "hfscheck 'OK'"
	if (lines[0][-3:-1] == 'OK') and (lines[1][-3:-1] == 'OK') and (lines[2][-3:-1] == 'OK'):
		print "Stopping Maintenence Scheduler"
		os.system("dpnctl stop maint")
		os.system("dpnctl stop sched")
	
	f = os.popen("dpnctl status maint 2>&1")
	lines = f.read().split('\n')
	schedStatus = False
	while lines[-2].split()[-1]!= 'suspended.':
		question = """couldn't stop the Maintenece scheduler
please try manually and when done Press yes to continue or press no to quit"""
		if not query_yes_no(question): sys.exit() 
		f = os.popen("dpnctl status  2>&1")
		lines = f.read().split('\n')	
	
	f = os.popen("dpnctl status sched 2>&1")
	lines = f.read().split('\n')
	schedStatus = False
	while lines[-2].split()[-1]!= 'down.':
		question = """couldn't stop the Backup scheduler
please try manually and when done Press yes to continue or press no to quit"""
		if not query_yes_no(question): sys.exit() 
		f = os.popen("dpnctl status  2>&1")
		lines = f.read().split('\n')	

	
	print "Backup and Maintenence scheduler are down"
	
	
############### End stopBackupMaintSched() ###############
