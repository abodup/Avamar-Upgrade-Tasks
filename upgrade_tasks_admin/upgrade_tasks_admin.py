#!/usr/bin/python

import sys
import os

techConsult = False
preUpgrade =  True
postUpgrade = False
targetVersion = "7.4.1"


############### Start main() ###############












def main():
	if preUpgrade:
		preUpgradeTasks()
	elif postUpgrade:
		preUpgradeTasks()
	

############### End main() ###############




############### Start preUpgradeTasks() ###############
def preUpgradeTasks():
	
	print "Starting Pre-upgrade tasks for version", targetVersion
	healthChecks(arg = "--preupgrade="+targetVersion, latestCheck= True)
	question = """Depending on the output of the health checks, if the health checks are clean press yes to continue
	if health checks are not clean press no to exit"""
	if not query_yes_no(question): sys.exit()
	stopBackupMaintSched()
	extraSteps()
	
############### End preUpgradeTasks() ###############	


	
############### Start healthChecks() ###############		
def healthChecks(arg, latestCheck = False):
	
	if latestCheck:
		latestProactiveCheck()
	os.system("/home/admin/proactive_check/proactive_check.pl "+arg)
	f = os.popen('cat hc_results.txt')
	print "Health checks Results\n ", f.read()
############### End healthChecks() ###############		



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

	
############### Start latestProactiveCheck() ###############
def latestProactiveCheck():

	pcsLatestVersion = "4.52"
	
	## Check if /home/admin/proactive_check directory exist
	if not os.path.isdir("/home/admin/proactive_check"):
		print "proactive_check directory doesn't exist"
		os.makedirs("/home/admin/proactive_check")
		print "\n proactive_check directory created"	
	else:
		print "\n Found proactive_check directory"
	
	## Check if /home/admin/proactive_check.pl file exist
	if not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
		print "proactive_checks.pl doesn't exist"
		getProactiveCheck()
		
	else:
		print "/n proactive_checks.pl already file exists"
		f = os.popen('/home/admin/proactive_check/proactive_check.pl --version')
		if f.read()[-5:-1] != pcsLatestVersion:
			print "This script is not the latest"
			getProactiveCheck()
			print "Latest script is present"
			
############### End latestProactiveCheck() ###############


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


############### Start extraSteps() ###############

def extraSteps():
	
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

############### End extraSteps() ###############



############### Start getArgs() ###############
def getArgs():
	print sys.argv[1]
	if not sys.argv[1].startswith("--"):
		print "Invalid command line argument", arg
		sys.exit()
	if sys.argv[1].startswith("--preupgrade="):
		preUpgrade = True
		print preUpgrade
		print postUpgrade
	
	elif sys.argv[1].startswith("--postupgrade="):
		postUpgrade = True
		print preUpgrade
		print postUpgrade

############### End getArgs() ###############		



	

############### Start query_yes_no() ###############
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

############### End query_yes_no() ###############




############### Start getInput() ###############
def getInput(question):

	sys.stdout.write(question)
	input = raw_input()
	return input 
    
############### getInput() ###############



main()