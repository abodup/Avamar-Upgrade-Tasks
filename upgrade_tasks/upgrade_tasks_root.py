#!/usr/bin/python

import os
import sys
import re
from datetime import datetime




############### Start main() ###############
def main():
	setupLog()
	prePostTech, targetVersion , revNo, currentVersion = getArgs()
	if prePostTech == "preUpgrade":
		printBoth("Executing PreUpgrade Tasks")
		preUpgradeTasks()
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