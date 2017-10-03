#!/usr/bin/python

import os
import sys
import re
from datetime import datetime




############### Start main() ###############
def main():
	setupLog()
	prePostTech, targetVersion , currentVersion = getArgs()
	#currentFamily - Peter
	#targetFamily - Peter
	if prePostTech == "preUpgrade":
		printBoth("Executing PreUpgrade Tasks")
		#verifyRevNo is correct
		#verify Files are present
		latestProactiveCheck()
		os.system("sudo -u admin /home/admin/proactive_check/proactive_check.pl --preupgrade=%s" %targetVersion)
		output = os.popen('sudo -u cat hc_results.txt').read()
		printBoth("Health checks Results\n\n %s" %output)
		question = """Depending on the output of the health checks, if the health checks are clean press yes to continue
if health checks are not clean press no to exit"""
		if not query_yes_no(question): sys.exit()
		avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads,  avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory  = fileNames(targetVersion)
		extractCopyAvps(currentFamily, currentVersion, targetFamily, targetVersion, avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads, avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory)
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

############### Start getArgs() ###############
def getArgs():
	message ="""
##################################################################
#                      Start getArgs                             #
##################################################################
"""
	printLog(message)
	##### Get Current Version ###
	printLog("Getting Current Version")
	printLog("Command: rpm -qa | grep dpnserver")
	f = os.popen("rpm -qa | grep dpnserver")
	output = f.read()
	printLog("Output: %s" %output)
	currentVersion= output.split("\n")[0].split("-",1)[1]
	printLog("currentVersion = %s" %currentVersion)
	#check the script has argument 1
	if len(sys.argv) < 2:
		
		printBoth("Missing Argument, please use --preupgrade=, --postupgrade= or --techconsult=")
		printLog("Terminating upgrade_tasks.py script")
		sys.exit()
	
	if sys.argv[1].startswith("--preupgrade="):
		printLog("Using --preupgrade")
		#check the script has argument 2
		if len(sys.argv) < 3:
			printBoth("Missing Argument, please use --rev=")
			printLog("Terminating upgrade_tasks.py script")
			sys.exit()
		
		prePostTech = "preUpgrade"
		targetVersion = re.split('=', sys.argv[1])[1]
		## get Rev
		if sys.argv[2].startswith("--rev="):
			revNo = re.split('=', sys.argv[2])[1]
			printLog("prePostTech = preUpgrade, Target Version = %s, revNo= %s" %(targetVersion, revNo))
		else:
		
			printBoth("Invalid command line argument " + str(sys.argv[2]))
			printBoth("with preupgrade you need to specify RCM revision package number with --rev=")
			printLog("Terminating upgrade_tasks.py script")
			sys.exit()
		
		printLog("Createing arguments.txt file")
		argsFile= open("arguments.txt", "w")
		printLog("Writing upgrade_tasks script arguments to aruments.txt file")
		argsFile.write("%s %s %s %s \n " %(prePostTech, targetVersion, revNo, currentVersion))
		argsFile.close()
		printLog("Closing arguments.txt")
		message ="""
##################################################################
#                      End getArgs                               #
##################################################################
"""
		printLog(message)
		return(prePostTech, targetVersion , revNo, currentVersion)	
	elif sys.argv[1].startswith("--postupgrade="):
		prePostTech = "postUpgrade"
		
	elif sys.argv[1].startswith("--techconsult="):
		prePostTech = "techConsult"
		
	else:
	
		printBoth("Invalid command line argument " + str(sys.argv[1]))
		printBoth("Please use--preupgrade=, --postupgrade= or --techconsult=")
		printLog("Terminating upgrade_tasks.py script")
		sys.exit()
############### End getArgs() ###############	

############### Start latestProactiveCheck() ###############
def latestProactiveCheck():
	message ="""
##################################################################
#                 Start latestProactiveCheck                     #
##################################################################
"""
	printLog(message)
	pcsLatestVersion = "4.52"
	printBoth("Latest proactive_check.pl version is %s" %pcsLatestVersion)
	#Checking for proactive_check directory
	if not os.path.isdir("/home/admin/proactive_check"):
		printBoth("proactive_check directory doesn't exist")
		os.makedirs("/home/admin/proactive_check")
		printBoth("proactive_check directory created")
	else: printBoth("Found proactive_check directory")
	#Checking for proactive_check.pl file
	if not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
		printBoth("proactive_checks.pl doesn't exist")
		printBoth("trying to download the latest proactive_check.pl")
		printLog("Command: curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl")
		os.system('curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl')
		printLog("Command: chmod a+x /home/admin/proactive_check/proactive_check.pl")
		os.system('chmod a+x /home/admin/proactive_check/proactive_check.pl')
		
		while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
			printLog("Check if proactive_check.pl file is downloaded")
			question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
			if not query_yes_no(question): sys.exit() 
			
		printBoth("Latest proactive_check.pl downloaded")
	else:
		printBoth("proactive_checks.pl already file exists")
		printLog("Checking proactive_check.pl version is latest")
		printLog("Command: /home/admin/proactive_check/proactive_check.pl --version")
		f = os.popen('/home/admin/proactive_check/proactive_check.pl --version')
		output = f.read()
		printLog("Output: %s" %output)
		if output[-5:-1] != pcsLatestVersion:
			printBoth("proactive_check.pl script version is %s which is not the latest" %output[-5:-1])
			printBoth("trying to download the latest proactive_check.pl")
			os.system('curl -o /home/admin/proactive_check/proactive_check.pl --disable-eprt -P - -O -o /home/admin/proactive_check/proactive_check.pl ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl')
			os.system('chmod a+x /home/admin/proactive_check/proactive_check.pl')
			print "Latest proactive_check.pl downloaded"
			while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
				question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
				if not query_yes_no(question): sys.exit() 

			print "Latest script is present"
	message ="""
##################################################################
#                  End latestProactiveCheck                      #
##################################################################
"""
	printLog(message)
############### End latestProactiveCheck() ###############






######################################## Helpers ###################################################
############### Start localTime() ###############
from datetime import datetime
############### Start localTime() ###############
def localTime():
	return str(datetime.now())
############### End localTime() ###############

############### Start setupLog() ###############
def setupLog():
	global log 
	os.system("touch ./tasks.log")
	os.system("chmod a+rw tasks.log")
	log = open("./tasks.log", "wa")
	text = """
##################################################################
#                      Log File Created                          #
##################################################################
"""
	log.write("%s %s\n"%(localTime(), text))	
############### End setupLog() ####################


############## Start printBoth() ##############
def printBoth(message):
	log.write("%s %s \n" %(localTime(), message))
	print message
############## End printBoth() ##############

############## Start printLog() ##############
def printLog(message):
	log.write("%s %s \n" %(localTime(), message))
############## Start printLog() ##############
main()