#!/usr/bin/python
############### Start setupLog() ###############
def setupLog():
	global logfile 
	logfile = open("./upgrade_tasks_root.log", "wa+")
############### Start End() ####################
setupLog()
logfile.write("%s 321\n" %localTime())
logfile.write("%s 654\n" %localTime())
