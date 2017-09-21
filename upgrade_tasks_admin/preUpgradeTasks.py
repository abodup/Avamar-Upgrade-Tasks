#!/usr/bin/python

import sys
import os


############### Start preUpgradeTasks() ###############
def preUpgradeTasks():
	
	### getArgs
	prePostTech, targetVersion , revNo ,currentVersion= getArgs()
	print "Starting Pre-upgrade tasks for version", targetVersion
	
	
	healthChecks(arg = "--preupgrade="+targetVersion, latestCheck= True)
	question = """Depending on the output of the health checks, if the health checks are clean press yes to continue
	if health checks are not clean press no to exit"""
	if not query_yes_no(question): sys.exit()
	stopBackupMaintSched()
	extraChecks()
	
############### End preUpgradeTasks() ###############	