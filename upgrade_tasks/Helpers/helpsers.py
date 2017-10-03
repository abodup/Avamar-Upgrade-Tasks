#!/usr/bin/python
import os
from datetime import datetime

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
