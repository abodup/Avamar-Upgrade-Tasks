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
		cmd("mkdir /home/admin/proactive_check")
		cmd("chown admin:admin /home/admin/proactive_check")
		printBoth("proactive_check directory created")
	else: printBoth("/home/admin/proactive_check/ directory exists")
	if not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
		printBoth("proactive_checks.pl doesn't exist")
		curlFile("ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl", "/home/admin/proactive_check/proactive_check.pl", "admin")
		while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
			question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
			if not query_yes_no(question): sys.exit() 			
		cmd('sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl')
	else:
		printBoth("proactive_checks.pl already file exists")
		printBoth("Checking proactive_check.pl owners")
		output =cmdOut("ls -l /home/admin/proactive_check/proactive_check.pl")
		if output.split(" ")[2] != 'admin' or output.split(" ")[3] != 'admin':
			printBoth("Changing proactive_check.pl owner user and group to admin")
			cmd("chown admin:admin /home/admin/proactive_check/proactive_check.pl")
		cmd('sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl')
		printBoth("Checking proactive_check.pl version is latest")
		output = cmdOut('sudo -u admin /home/admin/proactive_check/proactive_check.pl --version')
		printBoth("Latest proactive_check.pl version is %s" %pcsLatestVersion)
		while output[-5:-1] != pcsLatestVersion:
			printBoth("proactive_check.pl script version is %s which is not the latest" %output[-5:-1])
			printBoth("Backing up proactive_check.pl file")
			cmd("mv /home/admin/proactive_check/proactive_check.pl /home/admin/proactive_check/proactive_check.pl.%s" %localTime().replace(' ',''))
			printBoth("trying to download the latest proactive_check.pl")
			curlFile("ftp://avamar_ftp:anonymous@ftp.avamar.com/software/scripts/proactive_check.pl", "/home/admin/proactive_check/proactive_check.pl", "admin")
			while not os.path.isfile("/home/admin/proactive_check/proactive_check.pl"):
				question = """couldn't download the latest proactive_checks.pl 
Please copy the proactive_check.pl manually using vi
Press yes when the proactive_check.pl is ready to continue or press no to quit"""
				if not query_yes_no(question): sys.exit() 			
			cmd('sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl')
			output = cmdOut('sudo -u admin /home/admin/proactive_check/proactive_check.pl --version')
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
def test():
	setupLog()
	latestProactiveCheck()
test()