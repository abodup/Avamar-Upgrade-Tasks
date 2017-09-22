#!/usr/bin/python
import os
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


setupLog()

f= os.popen("avinstaller.pl --version")
output = f.read()
log.write("%s hi\n" %localTime())
log.write("%s Hey\n" %localTime())
log.write("%s %s"%(localTime(), output))
