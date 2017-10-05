#!/usr/bin/python
import os
from datetime import datetime

############### Start cmd() ###############
def cmd(command):
		printLog("Command: %s" %command)
		os.system("%s 2>&1 | tee -a upgrade_tasks.log" %command)
############### End cmd() ####################


############## Start printLog() ##############
def printLog(message):
	log = open("./upgrade_tasks.log", "a")
	log.write("%s %s \n" %(localTime(), message))
	log.close()
############## Start printLog() ##############

############### Start localTime() ###############
def localTime():
	return str(datetime.now())
############### End localTime() ###############

cmd("sudo -u admin chmod a+x /home/admin/proactive_check/proactive_check.pl")