#!/usr/bin/python

from datetime import datetime
def localTime():
	return str(datetime.now())

def setupLog():
	global logfile 
	
	logfile = open("./upgrade_tasks_root.log", "wa+")
	
setupLog()
logfile.write("%s 321\n" %localTime())
logfile.write("%s 654\n" %localTime())
