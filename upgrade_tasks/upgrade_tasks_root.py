#!/usr/bin/python

import sys
import os
import re
from datetime import datetime

############### Start main() ###############

def main():
	getArgs():
#	if preUpgrade:
#		preUpgradeTasks()
#	elif postUpgrade:
#		preUpgradeTasks()


############### End main() ###############


##################### HELPERS ###############################

############### Start localTime() ###############
def localTime():
	return str(datetime.now())
############### End localTime() ###############

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
############### Start getArgs() ###############

def getArgs():
	
	##### Get Current Version ###
	logfile.write("%s Getting Current Version \n" %localTime())
	f = os.popen("rpm -qa | grep dpnserver")
	output = f.read()
	logfile.write("%s Command: rpm -qa | grep dpnserver \n" %localTime())
	logfile.write("%s Output: %s \n" %(localTime(), output))
	
	currentVersion= output.split("\n")[0].split("-",1)[1]
	logfile.write("%s currentVersion = %s\n" %(localTime(), currentVersion))
	
	
	
	#check the script has argument 1
	if len(sys.argv) < 2:
		print "Missing Argument, please use --preupgrade=, --postupgrade= or --techconsult="
		sys.exit()
	
	sys.exit
	if sys.argv[1].startswith("--preupgrade="):
		
		#check the script has argument 2
		if len(sys.argv) < 3:
			print "Missing Argument, please use --rev="
			sys.exit()
		
		prePostTech = "preUpgrade"
		targetVersion = re.split('=', sys.argv[1])[1]
		## get Rev
		if sys.argv[2].startswith("--rev="):
			revNo = re.split('=', sys.argv[2])[1]
		else:
			print "Invalid command line argument", sys.argv[2]	
			print "with preupgrade you need to specify RCM revision package number with --rev="
			sys.exit()
		
		argsFile= open("arguments.txt", "w")
		argsFile.write("%s %s %s %s \n " %(prePostTech, targetVersion, revNo, currentVersion))
		argsFile.close()
		return(prePostTech, targetVersion , revNo, currentVersion)	
	elif sys.argv[1].startswith("--postupgrade="):
		prePostTech = "postUpgrade"
		
	elif sys.argv[1].startswith("--techconsult="):
		prePostTech = "techConsult"
		
	else:
	
		print "Invalid command line argument", sys.argv[1]
		print "Please use--preupgrade=, --postupgrade= or --techconsult="
		sys.exit()

		
	
############### End getArgs() ###############		

prePostTech, targetVersion , revNo, currentVersion = getArgs()

print prePostTech
print targetVersion
print revNo
print currentVersion




def preUpgradeTasks():
	
	print "Starting Pre-upgrade tasks for version", targetVersion
	
	avaimFull = "avaim_FULL_7.4.1-58_1.tgz"
	avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev4.tgz"
	extractUpgradeFiles(avaimFull, avaimRCM)
	#extraSteps()

############### Start extraSteps() ###############
def extractUpgradeFiles(avaimFull, avaimRCM):
	
	fullCheckCond = False
	rcmCheckCond = False
	fullChecksum = "896050a0b296fa9c5f78036e1a1b6238a464fd4ce8d49c6884aa998ae04e2b94"
	rcmChecksum = "59e0d0c5733c60bb81e0116183c6322131cccbdeb237a96d5b53c45089b1f767"

	#### Empty /data01 ####
	
	##################
	
	#### Loop to check avaimFULL file exists and checksum is clean ####
	while not fullCheckCond:
		
		#### Empty /data01
		
		
		##### Check avaimFull exist ####
		while not os.path.isfile("/usr/local/avamar/src/" + avaimFull):
			print avaimFull + " File doesn't exists at /usr/local/avamar/src"
			question = "please place the file under the specified location, press yes to continue or press no to abort"
			if not query_yes_no(question): sys.exit()
		print avaimFull + " File Found"
		
		##### Check SHA256SUM of avaimFull file ####
	
		print "checking Checksum of " + avaimFull
		f = os.popen("sha256sum /usr/local/avamar/src/" + avaimFull)
		checksum = f.read().split()[0]
		print checksum
		if checksum == fullChecksum:
			fullCheckCond = True
			print avaimFull + " checksum OK" 
		else: 
			print avaimFull + " checksum is not correct"
			question = "please download the %s file again, press yes to check for files again, or press no to abort" %avaimFull
			if not query_yes_no(question): sys.exit()
		
	#### Extracting avaimFull
	print "Extracting " + avaimFull
	os.system("tar xzvf /usr/local/avamar/src/avaim_FULL_7.4.1-58_1.tgz -C /usr/local/avamar/src")
	question = "Is Avinstaller upgrade required"
	if query_yes_no(question, default = "no"):
		os.system("mv /usr/local/avamar/src/avaim_FULL_7.4.1-58_1/other_avps/UpgradeAvinstaller-7.4.1-58.avp /data01/avamar/repo/packages")
		print "UpgradeAvinstaller-7.4.1-58.avp File copied to repo packages"
		print "Please go ahead and upgrade the avinstaller"
		
	else:
		print "Skipping Avinstaller upgrade step"
	
	os.system("mv /usr/local/avamar/src/avaim_FULL_7.4.1-58_1/mv2repo/AvamarUpgrade-7.4.1-58.avp /data01/avamar/repo/packages")
	print "AvamarUpgrade-7.4.1-58.avp File copied to repo packages"
	
	question = "Do you want to include UpgradeClientDownloads as callable package with the upgrade"
	if query_yes_no(question, default = "yes"):
	
		os.system("mv /usr/local/avamar/src/avaim_FULL_7.4.1-58_1/other_avps/UpgradeClientDownloads-7.4.1-58.avp /data01/avamar/repo/packages")
		print "UpgradeClientDownloads-7.4.1-58.avp File copied to repo packages"
		
	#### Loop to check avaimFULL file exists and checksum is clean ####
	while not rcmCheckCond:
		
		##### Check avaimRCM exist ####
		
		while not os.path.isfile("/usr/local/avamar/src/" + avaimRCM):
			print avaimRCM + " File doesn't exists at /usr/local/avamar/src"
			question = """please place the file under the specified location, press yes to continue or press no to abort"""
			if not query_yes_no(question): sys.exit()
		print avaimRCM + " File Found"
		
		##### Check SHA256SUM of avaimRCM file ####
	
		print "checking Checksum of " + avaimRCM
		f = os.popen("sha256sum /usr/local/avamar/src/" + avaimRCM)
		checksum = f.read().split()[0]
		print checksum
		if checksum == rcmChecksum:
			rcmCheckCond = True
			print avaimRCM + " checksum OK" 
		else: 
			print avaimRCM + " checksum is not correct"
			question = "please download the %s file again, press yes to check for files again, or press no to abort" %avaimRCM
			if not query_yes_no(question): sys.exit()
		
		os.system("tar xzvf /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev4.tgz -C /usr/local/avamar/src")
		print "Copying callable files of " + avaimRCM
		os.system("mv /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev4/AvPlatformOsRollup_2017-Q1-v9.avp /data01/avamar/repo/package")
		print "AvPlatformOsRollup_2017-Q1-v9.avp  -OS SECURITY PATCH-File copied to repo packages"
		os.system("mv /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev4/AvamarHotfix-7.4.1-58_HF278715.avp /data01/avamar/repo/package")
		print "AvamarHotfix-7.4.1-58_HF278715.avp -GSAN HOTFIX- File copied to repo packages"
		
		### Optional Packages ### 
		question = "Is AdsGen4sPowerSupplyRedundancy-HF260924.avp Installation needed as callable package"
		if query_yes_no(question, default = "no"):
			os.system("mv /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev4/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp /data01/avamar/repo/packages")
			print "AdsGen4sPowerSupplyRedundancy-HF260924.avp copied to repo packages"
		
		question = "Is gen4s-ssd-1000day-hotfix-282000.avp -Micron SSD FIrmware Update- Installation needed as callable package"
		if query_yes_no(question, default = "no"):
			os.system("mv /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev4/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp /data01/avamar/repo/packages")
			print "gen4s-ssd-1000day-hotfix-282000.avp -Micron SSD FIrmware Update copied to repo packages"

		question = "Gen4tPlatformSupportUpdate-HF274401.avp Installation needed as callable package"
		if query_yes_no(question, default = "no"):
			os.system("mv /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev4/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp /data01/avamar/repo/packages")
			print "Gen4tPlatformSupportUpdate-HF274401.avp copied to repo packages"
			
		print "Open Avinstaller and Start the upgrade When Ready"
		
############### Start extraSteps() ###############		
		
		
############### Start extraSteps() ###############

def extraSteps():

	print "Archiving package-survey* to  Rollups_Survey_Save.tgz "
	os.system("tar czvf /data01/avamar/var/Rollups_Survey_Save.tgz -P /data01/avamar/var/package-survey*")
	print "Removing package-survey*"
	os.system("rm -f /data01/avamar/var/package-survey*")
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
main()