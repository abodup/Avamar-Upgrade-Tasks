#!/usr/bin/python

import os
import re
import sys
from datetime import datetime

############### Start main() ###############
def main():
	
	checkRoot()
	setupLog()
	printBoth("Root user detected, running upgrade_tasks.py")
	
	#Check this is Avamar Utility Node
	
	prePostTech, targetVersion , currentVersion = getArgs()
	
	currentFamily = currentVersion[0:3]
	targetFamily = targetVersion[0:3]
	
	if prePostTech == "preUpgrade":
		printBoth("Executing PreUpgrade Tasks")
		avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads,  avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory  = fileNames(targetVersion)
		checkPackages(avaimFULL, checksumFULL)
		checkPackages(avaimRCM, checksumRCM)		
		latestProactiveCheck()
		cmd("sudo -u admin /home/admin/proactive_check/proactive_check.pl --preupgrade=%s" %targetVersion)
		output = cmdOut('sudo -u cat hc_results.txt')
		# Check if user wants more details
		print "Health checks Results\n\n %s" %output
		question = """Depending on the output of the health checks, if the health checks are clean press yes to continue
#if health checks are not clean press no to exit"""
		if not query_yes_no(question): sys.exit()
		#Write hc_results in sr_notes.txt
		extractCopyAvps(currentFamily, currentVersion, targetFamily, targetVersion, avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads, avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory)
		
		#Write some output to sr_notes
		#SMTP & SENDER to be written in temp files to check on the after the upgrade
		stopBackupMaintSched()
		extraChecks()
		

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
	output= cmdOut("rpm -qa | grep dpnserver")
	currentVersion = output.split("\n")[0].split("-",1)[1]
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
		return(prePostTech, targetVersion , currentVersion)	
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

############### Start checkPackage() ###############
def checkPackages(package, packageChecksum):
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
############### End checkPackage() ###############

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
	printBoth("Extracting " + avaimFULL)
	cmd("tar xzvf /usr/local/avamar/src/%s -C /usr/local/avamar/src" %avaimFULL)	
	printBoth("Extracting " + avaimRCM)
	cmd("tar xzvf /usr/local/avamar/src/%s -C /usr/local/avamar/src" %avaimRCM)	
	
	
	if aviUpgradeNeeded(currentFamily, currentVersion, targetFamily, targetVersion):
		printBoth("Avinstaller upgrade is needed to " + targetVersion)
		cmd("mv /usr/local/avamar/src/" + avinstallerFile + " /data01/avamar/repo/packages")
		printBoth(avinstallerFile + " File copied to Avinstaller Repo and ready, please go to GUI")
		question = "whenever Avinstaller upgrade done please press yes to continue"
		cond = True
		while cond:
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
		question = "would you like to add " + callableFixesOptional[length] + " with the server upgrade as a callable package?"
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
		if os.path.isdir("/usr/local/avamar/src/oldAvps/") == False:
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
		
		
############### Start aviUpgradeNeeded() ###############
def aviUpgradeNeeded(currentFamily, currentVersion, targetFamily, targetVersion):
	version = cmdOut("avinstaller.pl --version").split("_")[0].split("\t")[2].split("\n")[0]
	if version == targetVersion:
		return False
	elif (currentFamily == "6.1" or currentFamily == "7.0" or currentVersion == "7.1.0-370") and (targetFamily == "7.1" or targetFamily == "7.2"):
		return True
	elif (currentFamily == "7.1") and (targetFamily == "7.3"):
		return True
	else: return False
############### End aviUpgradeNeeded() ###############

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

############### Start extraSteps() ###############
def extraSteps():
	
	printBoth("Starting Extra Checks")
	
	printBoth("Checking Avamar Internal Root & MCUser Password")
	passwd = False 
	while not passwd:
		rootPass = getInput("Enter Avamar Internal Root Password: ")
		output = cmdOut("avmgr logn --id=root --password=%s 2>&1" %rootPass)
		lines = output.split('\n')
		if lines[0][0] == '1' : 
			passwd = True
			print "Correct Avamar Internal Root Password "
			
		else:
			print "Incorrect Avamar Internal Root Password"
	
	passwd = False 
	while not passwd:
		MCUserPass = getInput("Enter MCUser Password: ")
		output = cmdOut("avmgr logn --id=MCUser --password=%s 2>&1" %MCUserPass)
		lines = output.split('\n')
		if lines[0][0] == '1' : 
			passwd = True
			print "Correct Avamar MCUser Password "
			
		else:
			printBoth("Incorrect Avamar MCUser Password")

	output = cmdOut("egrep 'smtp|sender' /usr/local/avamar/var/mc/server_data/prefs/mcserver.xml 2>&1")
	smtp = output.split('\n')[0].split()[-2].split('=')[1].translate(None,'"')
	sender = output.split('\n')[1].split()[-2].split('=')[1].translate(None,'"')
	
	printBoth("SMTP host is " + smtp)
	printBoth("email sender is" + sender)	
############### End extraSteps() ###############

##################### START HELPERS #########################
############## Start checkRoot() ##############
def checkRoot():
	
	output = cmdOut("whoami")
	output = output.split("\n")[0]
	if output != "root":
		print"Error: please switch to root account and relaunch the script"
		sys.exit()
############## End checkRoot() ##############

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
	log.close()
############### End setupLog() ####################

############## Start printLog() ##############
def printLog(message):
	log = open("./upgrade_tasks.log", "a")
	log.write("%s %s \n" %(localTime(), message))
	log.close()
############## Start printLog() ##############

############## Start printBoth() ##############
def printBoth(message):
	log = open("./upgrade_tasks.log", "a")
	log.write("%s %s \n" %(localTime(), message))
	log.close()
	print message
############## End printBoth() ##############

############### Start cmd() ###############
def cmd(command):
		printLog("Command: %s" %command)
		os.system("%s 2>&1 | tee -a upgrade_tasks.log" %command)
############### End cmd() ####################

############### Start comdOut() ###############
def cmdOut(command):
	printLog("Command: %s" %command)
	output = os.popen(command).read()
	printLog("Output: %s" %output)
	return output
############### End cmdOut() ####################

############### Start curlFile() ####################
def curlFile(link, destinationFileName, user="root"):

	printBoth("Trying to download %s to destination %s as user=%s" %(link, destinationFileName, user))
	output = cmdOut('sudo -u %s curl -o %s --disable-eprt --connect-timeout 30 -P - -O %s 2>&1' %(user, destinationFileName, link))
	if output.split('\r')[-1].split(" ")[0] == '100':
		printBoth("Download Successful")
		return True
	else:
		printBoth("Download not successful maybe FTP is not enabled on this Avamar server, or the Avamar Server is not connected to the internet")
		return False
############### End curlFile() ####################

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
        #sys.stdout.write(question + prompt)
		printLog("Stopping Question")
		printBoth(question + prompt)
		choice = raw_input().lower()
		printLog("Answer is: %s" %choice)
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			printBoth("Please respond with 'yes' or 'no'\n""(or 'y' or 'n').\n")
			#sys.stdout.write("Please respond with 'yes' or 'no' "
                          #"(or 'y' or 'n').\n")
############### End query_yes_no() ###############
##################### END HELPERS #########################




########################## Start fileNames() #############################
def fileNames(targetVersion):
	message ="""
##################################################################
#                       Start fileNames                          #
##################################################################
"""
	printLog(message)
	avaimFULL = ""
	checksumFULL = ""
	checksumFULL = ""
	avinstallerFile = ""
	upgradeFile = ""
	customerHandoverScript = ""
	UpgradeClientDownloads = ""
	avaimRCM = ""
	checksumRCM = ""
	callableFixesMandatory = []
	callableFixesOptional = []
	notCallableFixesMandatory = []
	
		
########Version 7.1.1-145, onlyIfNeeded folder starts at Rev16########
########Customer Handover mail starts at Rev7########	
	if targetVersion ==  "7.1.1-145":
		avaimFULL = "avaim_FULL_7.1.1-145_1.tgz"
		checksumFULL = "aed65c89fddf77af4c1e82bcbeff96fe21e2e2925969375cbef9629352e14f58"
		avinstallerFile = "UpgradeAvinstaller-7.1.1-145.avp"
		upgradeFile = "AvamarUpgrade-7.1.1-145.avp"
		customerHandoverScript = "avaim_FULL_7.1.1-145_1/scripts/customer_handover_v5.0.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.1.1-145.avp"
		
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.1.1-145_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)
		
		if revNo == "1":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev1.tgz"
				checksumRCM = "439c97968fdf3f2816662ec08a2e653187380f42f9295a8e70e9374462a7afd3"
				callableFixesMandatory = ["AvPlatformOsRollup_2014-Q4-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = [""]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "2":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev2.tgz"
				checksumRCM = "7218b202d1c5b92a59a37ebdc588ce49e2db31f274c3bae05a5244a660582f23"
				callableFixesMandatory = ["AvPlatformOsRollup_2014-Q4-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_229688.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()				

		elif revNo == "3":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev3.tgz"
				checksumRCM = "c93b9739d223ac707759948b909d1ee69f76ad965508482f7a8960092534efc3"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_231762.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "4":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev4.tgz"
				checksumRCM = "c9e23c5cf56730d0f3402436b7ff27acd1b4b87396a0801af4c361f1ec462968"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_235000.avp", "Hotfix234581-7.1.1-145.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "5":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev5.tgz"
				checksumRCM = "bde7814c2f11addc3c3652c7b0cae9cef55638f20af917795df2376c3899e4ce"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_235000.avp", "Hotfix234581-7.1.1-145.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "6":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev6.tgz"
				checksumRCM = "cc57c7ddbfc88124f135f8691e9e74f37a9331cf1c9cceafea2356aaac4bccf4"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_240802.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
			
		elif revNo == "7":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev7.tgz"
				checksumRCM = "1f2f3b0136af7f05ed6da79eff7a911d100e77b942d627409ffac6a3afc05d87"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "8":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev8.tgz"
				checksumRCM = "68a60caa9c1da1c69e169e433e84b99738da3f32e78e5f634c5009a19d00f559"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
				
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "9":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev9.tgz"
				checksumRCM = "60f286c9979f7a777ee70d95830c042c3bcd1379bd20f73110fe5a5cdac8f7c6"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "10":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev10.tgz"
				checksumRCM = "c8c91fc52836c488b7b83b2fcb81ebccd02b371212069121bc0eed3054a66020"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "11":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev11.tgz"
				checksumRCM = "a7d407fbd902f4ac13dda354ec5b5b643d0fc6fc9fc60213a3bebd9681704ad4"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()				
				
		elif revNo == "12":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev12.tgz"
				checksumRCM = "eee16139334b52c83661cb41c60e7795c5e8b637da64153f973dbf9f20ccdab5"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "13":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev13.tgz"
				checksumRCM = "ded7bbbd4a7d2106c7ab3a8053f6ef35921abcbf07c8f81e1382760cb8746bac"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "14":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev14.tgz"
				checksumRCM = "569e92036e246b86c4ab296a8e3193ee111aa371f8199b3975237fdba83fee7c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "16":
			avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev16.tgz"
			checksumRCM = "04a4b1d1c3ae46cbf159e7fbcab923b5178a30450bc161af52bbcd0bc924be3b"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF199778.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		elif revNo == "15":
			printBoth("This revision was recalled, please download the latest revision and try again")
			sys.exit()
		
		else:
			printBoth("Please download a valid Revision and try again.")
			sys.exit()		
			
########Version 7.1.2-21, onlyIfNeeded folder starts at Rev16########
########Customer Handover mail starts at Rev4########	
	elif targetVersion == "7.1.2-21":
		avaimFULL = "avaim_FULL_7.1.2-21_1.tgz"
		checksumFULL = "1800590ea1b4eb02e3e27177b1819255"
		avinstallerFile = "UpgradeAvinstaller-7.1.2-21.avp"
		upgradeFile = "AvamarUpgrade-7.1.2-21.avp"
		customerHandoverScript = "customer_handover_v5.1.sh"
		UpgradeClientDownloads = "avaim_FULL_7.1.2-21_1/scripts/UpgradeClientDownloads-7.1.2-21.avp"
		
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.1.2-21_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)
		
		if revNo == "1":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev1.tgz"
				checksumRCM = "b2161c2cdd3dbb304934e9bbc495e0753bfc1f6ddf87f9a5accd79cd17325d01"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
		
		elif revNo == "2":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev2.tgz"
				checksumRCM = "f33a7a500b8832812de5fd76eb51918e4b311b733a38a1ce1dc7c20e89c5bfbe"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
		
		elif revNo == "3":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev3.tgz"
				checksumRCM = "18a3cb853f197a080b120f1817bce53cf35a5afe0d2c3ae1074d8f5300bc6915"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_241549.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
						
		elif revNo == "4":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev4.tgz"
				checksumRCM = "f645bbdeac54eac373886cb6fbf9abcaf6ff9eaea9f0f258a7c31b91e0f25cd0"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_244284.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
										
		elif revNo == "5":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev5.tgz"
				checksumRCM = "cbe48efbb3b54e3f8289fca38053b94502246584a034fc8b5c81a1ba584c1ce4"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_244284.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
										
		elif revNo == "6":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev6.tgz"
				checksumRCM = "ec79bfb70b5a6b4d0a7ffa967aca671dbaa47851c6bf991c79a61af2902e9eda"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247657.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
														
		elif revNo == "7":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev7.tgz"
				checksumRCM = "bd0432da6c94b75e6f14fa571920652757b87793969525b8db4cc9b2bc8ab4e0"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247657.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																		
		elif revNo == "8":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev8.tgz"
				checksumRCM = "3d715db6f64eb8eb1ea3fe9d12fe18eda751b4fa9528cf150ed82dea38a12f20"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247565.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																						
		elif revNo == "9":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev9.tgz"
				checksumRCM = "0f1416a80f71de39374b305e3a0baf8ca2c1e4504d5cd71c7fd4b25acb4f1416"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247565.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																										
		elif revNo == "10":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev10.tgz"
				checksumRCM = "9bebbeadbf8547e997c56f9f85daa6249290267d463a6b4aa14135044de98bb3"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_250666.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																														
		elif revNo == "11":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev11.tgz"
				checksumRCM = "456c88b5cc24039076d87b0080b79b51858ec215a517feb510ee81536d47f8fa"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_250666.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																																		
		elif revNo == "12":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev12.tgz"
				checksumRCM = "526122786bc92d6e5e94063f9bcd6b03a94e9c79e1d53cc6bfb5f48880957c18"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_255459.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																																						
		elif revNo == "13":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev13.tgz"
				checksumRCM = "cce27f6f3f8f6b71fab8af68be77caecc1301b132b0fd55d64ff7425d51e6427"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_255459.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																																										
		elif revNo == "14":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev14.tgz"
				checksumRCM = "459b8209ea2c721dc7dca09dd10db50b82a6db1b36d798561c060de8e0e5ba62"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_255459.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
																																														
		elif revNo == "16":
			avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev16.tgz"
			checksumRCM = "6cb828681a75ce359c40056ab74311623572fbfe8a2a95d93e16f6f9af805aef"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.1.2-21_HF275857.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF199778.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = ["v7_1_2_21_HF_271927.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		elif revNo == "15":
			printBoth("This revision was recalled, please download the latest revision and try again")
			sys.exit()
		
		else:
			printBoth("Please download a valid Revision and try again.")
			sys.exit()
		
########Version 7.2.0-401, onlyIfNeeded folder starts at Rev14########
########Customer Handover mail starts at Rev2########		
	elif targetVersion == "7.2.0-401":	
		avaimFULL = "avaim_FULL_7.2.0-401_1.tgz"
		checksumFULL = "4157a8149defc2b994eaa1d190f17c5e"
		avinstallerFile = "UpgradeAvinstaller-7.2.0-401.avp"
		upgradeFile = "AvamarUpgrade-7.2.0-401.avp"
		customerHandoverScript = "avaim_FULL_7.2.0-401_1/scripts/customer_handover_v5.1.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.2.0-401.avp"
		
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.2.0-401_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)
		
		if revNo == "1":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev1.tgz"
				checksumRCM = "f797d1202ec7e6bd757ae74050800295b9c301a9ebe9a104f9fd02a809c6881b"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "2":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev2.tgz"
				checksumRCM = "228387acbf81d2e64b24243d0fad5aed93de64ff8cffd7afac84d122aba55c9c"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "3":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev3.tgz"
				checksumRCM = "9ad5648e2caf6c532f4f1e9451c40e40a2a7f2e29683f37ecac8d4d92aa95daf"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_245396.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "4":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev4.tgz"
				checksumRCM = "84c323242e3648064bb08e3879175e2b531b9ff3496496043e213d93bd2fc30f"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_247126.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "5":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev5.tgz"
				checksumRCM = "57a043531017b01c3c831eed826a303e0412515cff488fe3cc5dfaa7c5b79e66"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_247126.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "6":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev6.tgz"
				checksumRCM = "3a49f655e14ee4132874b84e0f58e92fa882312d552b6d1e2a2abb98d651cd14"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "7":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev7.tgz"
				checksumRCM = "fed7aaec3b1a36f95945f379b37b3fa39d054cacc218acdb802ae125a3e87bdc"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "8":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev8.tgz"
				checksumRCM = "e86ef369e023dcd8ff7d4f10cefabec43298c6f073cf0d4ed74769c80a09cc4a"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "9":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev9.tgz"
				checksumRCM = "4f84599c5f896f499ae532a67ed95b3b21450a939c43c329660adf198292e52d"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "10":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev10.tgz"
				checksumRCM = "b1f5f13c494917a5da7fd637584de41070c81bb9092231151554a9773c34bd7f"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "11":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev11.tgz"
				checksumRCM = "1e1fd41a03ad647cec00edfdf3ec58b6bd63fca6198c59f7a7bd456bcb37dbc8"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"		
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "12":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev12.tgz"
				checksumRCM = "60adcf8ab27340e5c8a8130f99dfdf715ef3a8208fbc195b97f71ec2ba5fb88e"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp", "v7_2_0_401_HF_278332.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "14":
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev14.tgz"
				checksumRCM = "05a5f49d35c32c469e1bcb018ee0055946a6172567ddf2527ab11d6c79fb821a"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF199778.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_279816.avp", "v7_2_0_401_HF_278332.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"

		elif revNo == "13":
			printBoth("This revision was recalled, please download the latest revision and try again")
			sys.exit()		
		
		else:
			printBoth("Please download a valid Revision and try again.")

########Version 7.2.1-32, onlyIfNeeded folder starts at Rev14########
########Customer Handover mail starts at Rev5########				
	elif targetVersion == "7.2.1-32":
		avaimFULL = "avaim_FULL_7.2.1-32_1.tgz"
		checksumFULL = "2946bdeb7c47582bb5860712aeec96d2"
		avinstallerFile = "UpgradeAvinstaller-7.2.1-32.avp"
		upgradeFile = "AvamarUpgrade-7.2.1-32.avp"
		customerHandoverScript = "avaim_FULL_7.2.1-32_1/scripts/customer_handover_v5.2.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.2.1-32.avp"
		
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.2.1-32_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)
		
		if revNo == "1":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-31_Rev1.tgz"
				checksumRCM = "ef4ff250c597fb04dea91e9639fc53dcf15eb18c56e870494bd081f710ca6a29"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "2":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev2.tgz"
				checksumRCM = "8c6ec8ba75caea245a420c70bd8f09d91dd92fa814519b8137af9024c2304d34"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()			
		
		elif revNo == "3":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev3.tgz"
				checksumRCM = "aa7cc627f59babcbb26bd42b58f54ac09e29873bbd886207134a62f18372011d"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()	
				
		elif revNo == "4":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev4.tgz"
				checksumRCM = "c9f3c03688ad172ca074a03770b956c09c12f823f42bb3601b0949a544d7d1b3"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_248125.avp"]
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
		
		elif revNo == "5":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev5.tgz"
				checksumRCM = "c0b7169234f1ee158b64f2d659295401b48b5676abe5441af698c95b807c79c3"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_248125.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
		
		elif revNo == "6":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev6.tgz"
				checksumRCM = "7eefbf94e8e17a8f7c16d4ba378adb80aa1969ad466029e9fba4054e827815b5"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.1-32_HF254389.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "7":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev7.tgz"
				checksumRCM = "d390bd0d229406a15a4372975d426f8d7bb1a8b77e05cb4c06cfc36ccf8d00ba"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.1-32_HF254389.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()			
		
		elif revNo == "9":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev9.tgz"
				checksumRCM = "163002b4b01cf70e6dae1cd38158e69fafa683310cae3e14ec0baeaef17e7c04"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.1-32_HF265294.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
		
		elif revNo == "10":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev10.tgz"
				checksumRCM = "8a7ea7b62b856ad203564a90e55a9d92e9597152396fea4d0ee20eba83f5c14c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.1-32_HF265294.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "11":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev11.tgz"
				checksumRCM = "8ae9215996e4dc3ad84c2e18f0725c7ca4c8cd5b76befdd2e212896c1ec9cc84"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.1-32_HF265294.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
					
		elif revNo == "12":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev12.tgz"
				checksumRCM = "a5e3f7f27b881adc2939c159827171cdfa5fa38768883049b457a9ef484ff467"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.2.1-32_HF265294.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_277897.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "14":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev14.tgz"
				checksumRCM = "cc9da99c9582fb61e52d6a0e071255f8cb7093e5b5bb961f369a182e1585b666"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF249880.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_282216.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "15":
			avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev15.tgz"
			checksumRCM = "bbe9eeb8e26ac72442430b318807810b9165acfd56f8cd4027bd6aaad1c73c34"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp", "v7_2_1_32_HF_261520.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF249880.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = ["v7_2_1_32_HF_284664.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		elif revNo == "8":
			printBoth("This revision was recalled, please download the latest revision and try again")
			sys.exit()
		
		elif revNo == "13":
			printBoth("This revision was recalled, please download the latest revision and try again")
			sys.exit()	
		
		else:
			printBoth("Please download a valid Revision and try again.")			
			sys.exit()
	
########Version 7.3.0-233, onlyIfNeeded folder starts at Rev10########
########Customer Handover mail starts at Rev1 in scripts########
	elif targetVersion == "7.3.0-233":
		avaimFULL = "avaim_FULL_7.3.0-233_1.tgz"
		checksumFULL = "162f5ba81993056226cfc690eb312c0a"
		avinstallerFile = "UpgradeAvinstaller-7.3.0-233.avp"
		upgradeFile = "AvamarUpgrade-7.3.0-233.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.3.0-233.avp"
			
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.3.0-233_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)
			
		if revNo == "1":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev1.tgz"
				checksumRCM = "72fa5b32673c9c224a0137cdc974c5a8750efd6751d889201b4b05d034dc403f"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"		
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
					
		elif revNo == "2":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev2.tgz"
				checksumRCM = "6a04f14f15f5dedee6f3e5c011077f25202e2197f1b5adf8f0e045348fe8278e"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
					
		elif revNo == "3":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev3.tgz"
				checksumRCM = "8a99bcaa17a44dbf986d1334c182d56d55f44e7fe0cc092efe9b7a37e184255c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "4":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev4.tgz"
					checksumRCM = "c252c5bc2319ae1c37224ca41d2c69b2ebe6bbe65e9f49b0aa61c78a9b3fc0be"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.3.0-233_HF267305.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
					customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "5":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev5.tgz"
				checksumRCM = "825cf10209b34877a2a4a75c4b110f1595fc0b775398288af0f888f22e514d2b"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.3.0-233_HF269398.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "6":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev6.tgz"
				checksumRCM = "64d4795e222507539b0533e1aa8dd3455e0d13c65f0046643ecbc0c60bc340af"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.3.0-233_HF269398.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "7":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev7.tgz"
				checksumRCM = "1e7b6a928198c4a1ef944658b6ef2366d73497e980fb06a6df4ff3a938960fe2"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.3.0-233_HF269398.avp", "v7_3_0_233_HF_271301.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "8":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev8.tgz"
				checksumRCM = "ad69bde39505c80bd716e734bdff161f4a7672d16a6361e0d2aaececded537c3"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.3.0-233_HF269398.avp", "v7_3_0_233_HF_271301.avp", "v7_3_0_233_HF_278483.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "10":
			avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev8.tgz"
			checksumRCM = "00d35b8fb4464fb8b925483932938291d390f3576d82295e394480e4f7523fe2"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp", "v7_3_0_233_HF_271301.avp", "v7_3_0_233_HF_278483.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = [""]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			
		elif revNo == "9":
			printBoth("This revision was recalled, please download the latest revision and try again")
			sys.exit()	
		
		else:
			printBoth("Please download a valid Revision and try again.")			
			sys.exit()
	
	########Version 7.3.1-125, onlyIfNeeded folder starts at Rev6########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.3.1-125":
		avaimFULL = "avaim_FULL_7.3.1-125_1.tgz"
		checksumFULL = "457440734e86e3dc5c7b9baa49911712"
		avinstallerFile = "UpgradeAvinstaller-7.3.1-125.avp"
		upgradeFile = "AvamarUpgrade-7.3.1-125.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.3.1-125.avp" 
			
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.3.1-125_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " + revNo)
			
		if revNo == "1":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev1.tgz"
				checksumRCM = "51cab07b3c6a753c3316adbdfabc7627d0f0567e4a2ff0e2724cc84cf1e352c1"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "2":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev2.tgz"
				checksumRCM = "08d52bf1b8acdb18dba8f84b7b746b29ec766cc231d5d811d7190ed8e6de081a"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "3":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev3.tgz"
				checksumRCM = "3c01124d7211bcfb4a5f3ffbf8336da4ed8881685797c2e58376c420ade1421b"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_274527.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "4":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev4.tgz"
				checksumRCM = "cc354007f4e88f73e34356c9e100de595bb4e44544cf2ddc9b0e54231acadd6c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_274527.avp", "v7_3_1_125_HF_278484.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "6":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev6.tgz"
				checksumRCM = "f6f5686df5d74b939eeca4e946afcdecc2df0d65005874729107ebcb117aae33"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()

		elif revNo == "7":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev7.tgz"
				checksumRCM = "ee18dae44295faa4bd3bc8e5bca80713faafebccb5e295e169f41ba574e22883"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp", "v7_3_1_125_mc_cumulative_201706.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()	

		elif revNo == "8":
			avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev8.tgz"
			checksumRCM = "8ff1e6897354bf4a68520b69ec18e65d18bbb76d25ba77ade1b38303593ad206"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp", "v7_3_1_125_mc_cumulative_201707.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"

		elif revNo == "5":
			printBoth("This revision was recalled, please download the latest revision and try again")
			sys.exit()	
		
		else:
			printBoth("Please download a valid Revision and try again.")		
			sys.exit()
						
	########Version 7.4.0-242########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.4.0-242":
		avaimFULL = "avaim_FULL_7.4.0-242_1.tgz"
		checksumFULL = "8ece38bc6853e7ee1ba83418acc78d966865d0a1add57107755a31d1547c24b2"
		avinstallerFile = "UpgradeAvinstaller-7.4.0-242.avp"
		upgradeFile = "AvamarUpgrade-7.4.0-242.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.4.0-242.avp"
			
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.4.0-242_Rev*tgz")
		output = output.split("\n")
		x = len(output)-2
		new = []
		while (x > 0):
			t = output[x].split(".tgz")[-2].split("Rev")[2]
			new.insert(0, int(t))
			x -= 1
		
		sorted(new, key=int, reverse=True)
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)			
		
		if revNo == "1":
			avaimRCM = "avaim_RCM_Updates_7.4.0-242_Rev1.tgz"
			checksumRCM = "2353b6ada54e7f969b6ec021b13439bedf3b61957a35f6f9779fb262e7a4b59f"
			callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
			callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
			notCallableFixesMandatory = [""]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		else:
			printBoth("Please download a valid Revision and try again.")			
			sys.exit()		
		
	########Version 7.4.1-58, onlyIfNeeded folder starts at Rev3########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.4.1-58":
		avaimFULL = "avaim_FULL_7.4.1-58_1.tgz"
		checksumFULL = "896050a0b296fa9c5f78036e1a1b6238a464fd4ce8d49c6884aa998ae04e2b94"
		avinstallerFile = "UpgradeAvinstaller-7.4.1-58.avp"
		upgradeFile = "AvamarUpgrade-7.4.1-58.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.4.1-58.avp"

		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)
		
		if revNo == "1":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev1.tgz"
				checksumRCM = "20157e4ce8aebeb126b2eb4e65d9305577927e6fc0064f841b35d0137f73e2f7"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
		
		elif revNo == "2":
			printBoth("This is a recalled revision that can not be used, please download the latest Revision and try again")
			sys.exit()
		
		elif revNo == "3":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev3.tgz"
				checksumRCM = "3701b92b633f3841a290ae5a4259eca3dfa5409c3adbae70e928fab53fe3c898"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_4_1_58_mc_cumulative_201705.avp"] 
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
				
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
		elif revNo == "4":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev4.tgz"
				checksumRCM = "59e0d0c5733c60bb81e0116183c6322131cccbdeb237a96d5b53c45089b1f767"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.4.1-58_HF278715.avp", "v7_4_1_58_mc_cumulative_201706.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_4_1_58_HF_285198.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			
			else:
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "5":
			avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev5.tgz"
			checksumRCM = "fca08b993e7479c122cd39248e94fbccc66a9cd430f347da329da170adf4c783"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.4.1-58_HF278715.avp", "v7_4_1_58_mc_cumulative_201707.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = ["v7_4_1_58_HF_285198.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		else:
			printBoth("Please download a valid Revision number")
			sys.exit()
		
	########Version 7.5.0-183, onlyIfNeeded folder starts at Rev1########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.5.0-183":
		avaimFULL = "avaim_FULL_7.5.0-183.tgz"
		checksumFULL = "896050a0b296fa9c5f78036e1a1b6238a464fd4ce8d49c6884aa998ae04e2b94"
		avinstallerFile = "UpgradeAvinstaller-7.5.0-183.avp"
		upgradeFile = "AvamarUpgrade-7.5.0-183.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.5.0-183.avp"
		
		output = cmdOut("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.5.0-183_Rev*tgz")
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			printBoth("No Revision found")
			sys.exit()			
		revNo = str(new[0]) 
		printBoth("Newest Revision found on this Avamar is:  " +  revNo)		
		
		if revNo == "1":
			question = "Latest Revision is 3, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev1.tgz"
				checksumRCM = "e98fd46778ad737e77ee86aa7739f543b53e72796e8802780e7188ec0d74d9d2"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = []
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else: 
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
			
		elif revNo == "2":
			question = "Latest Revision is 3, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev2.tgz"
				checksumRCM = "bf8bd1e6f0f47cc1d53469501ff715960ee27817ad3e6bcd7643c846e2a4d8bf"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = []
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else: 
				printBoth("Please download the latest Revision and try again.")
				sys.exit()
				
		elif revNo == "3":
			avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev3.tgz"
			checksumRCM = "cba2e6539ed3bea202f30da072522dc20cb4212277145ef624e26c5a751e8ec3"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "v7_5_0_183_mc_cumulative_201707.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = []
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			
		else:	
			printBoth("Please download a valid Revision number")
			sys.exit()
			
	else:
		printBoth("Please download a valid Version number")
		sys.exit()
	
	
	avinstallerFile = avaimFULL.split(".tgz")[0] + "/other_avps/" + avinstallerFile
	upgradeFile = avaimFULL.split(".tgz")[0] + "/mv2repo/" + upgradeFile
	UpgradeClientDownloads = avaimFULL.split(".tgz")[0] + "/other_avps/" + UpgradeClientDownloads
	callableFixesMandatory = [avaimRCM.split(".tgz")[0] + "/" + callableFixesMandatory for callableFixesMandatory in callableFixesMandatory]
	callableFixesOptional = [avaimRCM.split(".tgz")[0] + "/" + callableFixesOptional for callableFixesOptional in callableFixesOptional]
	notCallableFixesMandatory = [avaimRCM.split(".tgz")[0] + "/" + notCallableFixesMandatory for notCallableFixesMandatory in notCallableFixesMandatory]
	
	
	
	########Return Paths for required packages########
	message ="""
##################################################################
#                       End fileNames                            #
##################################################################
"""
	printLog(message)
	return(avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads,  avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory) 
###################### End fileNames() #######################################
main()