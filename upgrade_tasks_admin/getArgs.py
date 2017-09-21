#!/usr/bin/python

import os
import sys
import re

############### Start getArgs() ###############
def getArgs():
	
	##### Get Current Version ###
	f = os.popen("rpm -qa | grep dpnserver")
	currentVersion= f.read().split("\n")[0].split("-",1)[1]
	
	
	
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

