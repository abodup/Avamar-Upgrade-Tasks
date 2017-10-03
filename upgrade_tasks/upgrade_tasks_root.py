#!/usr/bin/python

import os
import sys
import re
from datetime import datetime

############### Start main() ###############
def main():
	setupLog()
	#prePostTech, targetVersion , currentVersion = getArgs()
	#currentFamily - Peter
	#targetFamily - Peter
	if prePostTech == "preUpgrade":
		printBoth("Executing PreUpgrade Tasks")
		#verifyRevNo is correct
		#verify Files are present
		#latestProactiveCheck()
		cmd("sudo -u admin /home/admin/proactive_check/proactive_check.pl --preupgrade=%s" %targetVersion)
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

############### Start extractCopyAvps() ###############
def extractCopyAvps(currentFamily, currentVersion, targetFamily, targetVersion, avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads, avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory):
		
	clearRepo()
	checkExtractPackage(avaimFULL, checksumFULL)
	checkExtractPackage(avaimRCM, checksumRCM)
	
	if aviUpgradeNeeded(currentFamily, currentVersion, targetFamily, targetVersion):
		printBoth("Avinstaller upgrade is needed to " + targetVersion)
		cmd("mv /usr/local/avamar/src/" + avinstallerFile + " /data01/avamar/repo/packages")
		printBoth(avinstallerFile + " File copied to Avinstaller Repo and ready, please go to GUI")
		question = "whenever Avinstaller upgrade done please press yes to continue"
		cond = True
		while cond
			if query_yes_no(question):
				if cmd("avinstaller.pl --version") == targetVersion:
					printBoth("Avinstaller version checked and you can go to Avamar server upgrade")
					cond = False
				else: printBoth("please check the Avinstaller upgrade again")
			else: printBoth("please check the Avinstaller upgrade again")
	else:
		printBoth("You can go to Avamar server upgrade")
	
	cmd("mv /usr/local/avamar/src/" + upgradeFile + " /data01/avamar/repo/packages")
	printBoth(upgradeFile + " is being moved now to /data01/avamar/repo/packages")
	
	clientVer = cmdOut("ls /usr/local/avamar/var/avi/server_data/package_data/ | grep UpgradeClientDownloads-")
	clientVer1 = clientVer.split("_")[0].split("-",1)[1][0:-4]
	#UpgradeClientDownloads-7.2.1-32.avp_1496764981077 -> UpgradeClientDownloads-7.2.1-32.avp -> 7.2.1-32.avp -> 7.2.1-32
	if clientVer1 != targetVersion:
		question = "UpgradeClientDownloads pacakge needed, if you would like to add it now with server upgrade, please press yes."
		if query_yes_no(question):
			cmd("mv /usr/local/avamar/src/" + UpgradeClientDownloads + " /data01/avamar/repo/packages")
			printBoth(UpgradeClientDownloads + " is being moved now to /data01/avamar/repo/packages")
		else: printBoth("please don't forget to move the package after upgrade.")
	else: printBoth(UpgradeClientDownloads + " already installed before, you don't need to include.")
		
	length=0
	while (length < len(callableFixesMandatory)):
		cmd("mv /usr/local/avamar/src/" + callableFixesMandatory[length] + " /data01/avamar/repo/packages")
		printBoth(callableFixesMandatory[length] + " is being moved now to /data01/avamar/repo/packages")
		length += 1

	length=0
	while (length < len(callableFixesOptional)):
		question = "would you like to add " + callableFixesOptional(length) + " with the server upgrade as a callable package?"
		if query_yes_no(question):
			cmd("mv /usr/local/avamar/src/" + callableFixesOptional[length] + " /data01/avamar/repo/packages")
			printBoth(callableFixesOptional[length] + " is being moved now to /data01/avamar/repo/packages")
			length += 1
		else: length += 1
############### End extractCopyAvps() ##########################################
		

################## Start clearRepo() ####################
def clearRepo():
	print "Checking if avinstaller repo is clear"
	#check /data01/avamar/repo/tmp
	if  len(os.listdir("/data01/avamar/repo/packages/")) > 0:
		if os.path.isdir("/usr/local/avamar/src/oldAvps/") == False
			os.mkdir("/usr/local/avamar/src/oldAvps/")
			if os.path.isdir("/usr/local/avamar/src/oldAvps") == False:
				printBoth("Can't create oldAvps directory to put avps currently present in the avinstaller in it")
				printBoth("Print please Consult with RPS SME to clear the Avinstaller Repo")
				sys.exit()
	
			os.system("mv /data01/avamar/repo/packages/* /usr/local/avamar/src/oldAvps")
			if len(os.listdir("/data01/avamar/repo/packages")) > 0:
				printBoth("Can't copy avps currently preset in the avinstaller")
				printBoth("Print please Consult with RPS SME to clear the Avinstaller Repo")
				sys.exit()
				
			else: printBoth("Avinstaller Repo cleared successfully")
	else: printBoth("Avinstaller Repo is already Clear"	)
################## End clearRepo() ####################
		
		
############### Start checkExtractPackage() ###############
def checkExtractPackage(package, packageChecksum):
	cond = False
	while not cond:
		### Check Package Exists
		while not os.path.isfile("/usr/local/avamar/src/" + package):
			printBoth(package + " File doesn't exists at /usr/local/avamar/src")
			question = "please place the %s file under the specified location, press yes to continue or press no to abort" %package
			if not query_yes_no(question): sys.exit()
		printBoth(package + " File Found")
		##### Checksum of the file ####
		printBoth("checking Checksum of " + package)
		output = cmdOut("sha256sum /usr/local/avamar/src/" + package)
		checksum = output.split()[0]
		printBoth(checksum)
		if checksum == packageChecksum:
			cond = True
			printBoth(package + " checksum OK" )
		else: 
			printBoth(package + " checksum is not correct")
			question = "please download the %s file again, press yes to check for files again, or press no to abort" %package
			if not query_yes_no(question): sys.exit()
		
	#### Extracting avaimFull
	printBoth("Extracting " + package)
	cmd("tar xzvf /usr/local/avamar/src/%s -C /usr/local/avamar/src" %package)
############### End checkExtractPackage() ###############












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