#!/usr/bin/python
import os
from datetime import datetime

############### Start latestProactiveCheck() ###############
def latestProactiveCheck():
	message ="""
##################################################################
#                 Start latestProactiveCheck                     #
##################################################################
"""
	printLog(message)
	pcsLatestVersion = "4.52"
	if not os.path.isdir("/home/admin/proactive_check"):
		printBoth("proactive_check directory doesn't exist")
		printLog("Setting Effective user and group id to admin - 500")
		os.seteuid(500)
		os.setegid(500)
		os.makedirs("/home/admin/proactive_check")
		os.seteuid(0)
		os.setegid(0)
		printBoth("proactive_check directory created")
	else: printBoth("Found proactive_check directory")
	if not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
		printBoth("proactive_checks.pl doesn't exist")
		printBoth("trying to download the latest proactive_check.pl")
		#add timeout and check if no ftp
		output = cmdOut('sudo -u admin curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt --connect-timeout 30 -P - -O ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl 2>&1')
		while output.split('\r')[-1].split(" ")[0] != '100':
			printLog("Couldn't download proactive_check.pl, maybe ftp is not enabled")
			question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
			if not query_yes_no(question): sys.exit() 	
		while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
			printLog("Check if proactive_check.pl file is downloaded")
			question = """can't find the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
			if not query_yes_no(question): sys.exit() 
		
		cmd('sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl')
		printBoth("Latest proactive_check.pl downloaded")
	else:
		printBoth("proactive_checks.pl already file exists")
		printLog("Checking proactive_check.pl version is latest")
		output = cmdOut('sudo -u admin /home/admin/proactive_check/proactive_check.pl --version')
		printBoth("Latest proactive_check.pl version is %s" %pcsLatestVersion)
		while output[-5:-1] != pcsLatestVersion:
			printBoth("proactive_check.pl script version is %s which is not the latest" %output[-5:-1])
			printBoth("trying to download the latest proactive_check.pl")
			#add timeout and check if no ftp
			output = cmdOut('sudo -u admin curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt --connect-timeout 30 -P - -O ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl 2>&1')
			while output.split('\r')[-1].split(" ")[0] != '100':
				printLog("Couldn't download proactive_check.pl, maybe ftp is not enabled")
				question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
				if not query_yes_no(question): sys.exit()
			#PRINT SOMETHING		
			while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
				printLog("Check if proactive_check.pl file is downloaded")
				question = """can't find the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
				if not query_yes_no(question): sys.exit()
			output = cmdOut('sudo -u admin /home/admin/proactive_check/proactive_check.pl --version')
			cmd('sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl')
			printBoth("Latest proactive_check.pl downloaded")
		printBoth("proactive_check.pl script version is %s which is the latest" %output[-5:-1])
		printBoth("Latest script is present")
	message ="""
##################################################################
#                  End latestProactiveCheck                      #
##################################################################
"""
	printLog(message)
############### End latestProactiveCheck() ###############


##########################TESTING##########################
################Helpers###########

############### Start localTime() ###############
def localTime():
	return str(datetime.now())
############### End localTime() ###############

############### Start setupLog() ###############
def setupLog():
	global log 
	os.system("touch upgrade_tasks.log")
	os.system("chmod a+rw upgrade_tasks.log")
	log = open("./upgrade_tasks.log", "wa")
	text = """
##################################################################
#                      Log File Created                          #
##################################################################
"""
	log.write("%s %s"%(localTime(), text))
############### End setupLog() ####################

############## Start printLog() ##############
def printLog(message):
	log.write("%s %s \n" %(localTime(), message))
############## Start printLog() ##############

############## Start printBoth() ##############
def printBoth(message):
	log.write("%s %s \n" %(localTime(), message))
	print message
############## End printBoth() ##############

############### Start cmd() ###############
def cmd(command):
		printLog("Command: %s" %command)
		os.system(command)
############### End cmd() ####################

############### Start comdOut() ###############
def cmdOut(command):
	printLog("Command: %s" %command)
	output = os.popen(command).read()
	printLog("Output: %s" %output)
	return output
############### End cmdOut() ####################

def test():
	setupLog()
	latestProactiveCheck()
test()