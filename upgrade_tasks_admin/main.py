#!/usr/bin/python

import sys
import os

preUpgrade =  True
postUpgrade = False
targetVersion = "7.4.1"


############### Start main() ###############

def main():
	if preUpgrade:
		preUpgradeTasks()
	elif postUpgrade:
		preUpgradeTasks()
	
############### End main() ###############
