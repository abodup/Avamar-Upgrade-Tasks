#!/usr/bin/python

import sys
import re
import os


############### Start getArgs() ###############
def getArgs():
	if not os.path.isfile("arguments.txt"):
		print "Couldn't file arguments.txt file which has the arguments saved in the admin run"
		print "Make sure the admin and the root script are on the same directory"
		print "Make sure upgrade_tasks_admin.py script runs cleanly before running the upgrade_tasks_root.py"
		sys.exit()
	
	argsFile= open("arguments.txt", "r")
	args = argsFile.read().split(" ")
	argsFile.close()
	
	prePostTech = args[0]
	targetVersion = args[1]
	revNo = args[2]
	currentVersion = args[3]	
	return(prePostTech, targetVersion , revNo, currentVersion)	
############### End getArgs() ###############		

prePostTech, targetVersion , revNo ,currentVersion= getArgs()

print prePostTech
print targetVersion
print revNo
print currentVersion