#!/usr/bin/python
import os
############### Start cmd() ###############
def cmd(command):
		printLog("Command: %s" %command)
		os.system(command)
############### End cmd() ####################

