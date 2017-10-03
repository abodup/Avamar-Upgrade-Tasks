#!/usr/bin/python

import os
import sys
import re
from datetime import datetime

############### Start main() ###############
def main():
	setupLog()
	currentFamily = "7.2"
	currentVersion = "7.2.1-32"
	targetFamily = "7.4"
	targetVersion = "7.4.1-32"
	avaimFULL = "avaim_FULL_7.4.1-58_1.tgz"
	checksumFULL = "896050a0b296fa9c5f78036e1a1b6238a464fd4ce8d49c6884aa998ae04e2b94"
	avinstallerFile = "avaim_FULL_7.4.1-58_1/other_avps/UpgradeAvinstaller-7.4.1-58.avp"
	upgradeFile = "avaim_FULL_7.4.1-58_1/mv2repo/AvamarUpgrade-7.4.1-58.avp"
	customerHandoverScript = "avaim_RCM_Updates_7.4.1-58_Rev5/customer_handover_v5.4.sh"
	UpgradeClientDownloads = "avaim_FULL_7.4.1-58_1/other_avps/UpgradeClientDownloads-7.4.1-58.avp"
	avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev5.tgz" 
	checksumRCM = "fca08b993e7479c122cd39248e94fbccc66a9cd430f347da329da170adf4c783"
	callableFixesMandatory = ["avaim_RCM_Updates_7.4.1-58_Rev5/AvamarHotfix-7.4.1-58_HF278715.avp", "avaim_RCM_Updates_7.4.1-58_Rev5/v7_4_1_58_mc_cumulative_201707.avp", "avaim_RCM_Updates_7.4.1-58_Rev5/AvPlatformOsRollup_2017-Q1-v9.avp"]
	callableFixesOptional = ["avaim_RCM_Updates_7.4.1-58_Rev5/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "avaim_RCM_Updates_7.4.1-58_Rev5/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "avaim_RCM_Updates_7.4.1-58_Rev5/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
	notCallableFixesMandatory = ["avaim_RCM_Updates_7.4.1-58_Rev5/AvamarHotfix-7.4.1-58_HF278715.avp"]	
	extractCopyAvps(currentFamily, currentVersion, targetFamily, targetVersion, avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads, avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory)
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


############### Start aviUpgradeNeeded() ###############
def aviUpgradeNeeded(currentFamily, currentVersion, targetFamily, targetVersion):
	if os.system("avinstaller.pl --version") == targetVersion:
		return False
	elif (currentFamily == "6.1" or currentFamily == "7.0" or currentVersion == "7.1.0-370") and (targetFamily == "7.1" or targetFamily == "7.2"):
		return True
	elif (currentFamily == "7.1") and (targetFamily == "7.3"):
		return True
	else: return False
############### End aviUpgradeNeeded() ###############










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
		os.system(command)
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
	#add timeout and check if no ftp
	output = cmdOut('sudo -u %s curl -o %s --disable-eprt --connect-timeout 30 -P - -O %s 2>&1' %(user, destinationFileName, link))
	if output.split('\r')[-1].split(" ")[0] == '100':
		return True
	else: return False
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

main()