def clearRepo():
	print "Checking if avinstaller repo is clear"
	
	if  len(os.listdir("/data01/avamar/repo/packages/")) > 0:
		if os.path.isdir("/usr/local/avamar/src/oldAvps/") == False
			os.mkdir("/usr/local/avamar/src/oldAvps/")
			if os.path.isdir("/usr/local/avamar/src/oldAvps") == False:
				print "Can't create oldAvps directory to put avps currently present in the avinstaller in it"
				print "Print please Consult with RPS SME to clear the Avinstaller Repo"
				sys.exit()
	
			os.system("mv /data01/avamar/repo/packages/* /usr/local/avamar/src/oldAvps")
			if len(os.listdir("/data01/avamar/repo/packages")) > 0:
				print "Can't copy avps currently preset in the avinstaller"
				print "Print please Consult with RPS SME to clear the Avinstaller Repo"
				sys.exit()
				
			else: print "Avinstaller Repo cleared successfully"
	else: print "Avinstaller Repo is already Clear"	
##################
