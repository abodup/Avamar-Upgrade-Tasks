#!/usr/bin/python
import os
import sys

from datetime import datetime

############### Start localTime() ###############
def localTime():
	return str(datetime.now())
############### End localTime() ###############
############### Start getInput() ###############
def getInput(question):

	sys.stdout.write(question)
	input = raw_input()
	return input 
    
############### getInput() ###############

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

############### Start extraChecks() ###############

def extraChecks():
	
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
	
	
	
############### End extraChecks() ###############

extraChecks()
