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

def helpersTest():
	setupLog()
	printLog("Print in log only, starting helpersTest()")
	printBoth("print in both, starting helpersTest()")
	cmd("status.dpn")
	output = cmdOut("dpnctl status 2>&1")
	print output
	
helpersTest()