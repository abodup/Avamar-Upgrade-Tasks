################## Start clearRepo() ####################
def clearRepo():
	print "Checking if avinstaller repo is clear"
	#check /data01/avamar/repo/tmp
	if  len(os.listdir("/data01/avamar/repo/packages/")) > 0:
		if os.path.isdir("/usr/local/avamar/src/oldAvps/") == False
			os.mkdir("/usr/local/avamar/src/oldAvps/")
			if os.path.isdir("/usr/local/avamar/src/oldAvps") == False:
				printBoth("Can't create oldAvps directory to put avps currently present in the avinstaller in it")
				printBoth("Print please Consult with RPS SME to clear the Avinstaller Repo")
				sys.exit()
	
			os.system("mv /data01/avamar/repo/packages/* /usr/local/avamar/src/oldAvps")
			if len(os.listdir("/data01/avamar/repo/packages")) > 0:
				printBoth("Can't copy avps currently preset in the avinstaller")
				printBoth("Print please Consult with RPS SME to clear the Avinstaller Repo")
				sys.exit()
				
			else: printBoth("Avinstaller Repo cleared successfully")
	else: printBoth("Avinstaller Repo is already Clear"	)
################## End clearRepo() ####################
