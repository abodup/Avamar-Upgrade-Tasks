############## Start checkRoot() ##############
def checkRoot():
	
	output = cmdOut("whoami")
	output = output.split("\n")[0]
	if output != "root":
		print"Error: please switch to root account and relaunch the script"
		sys.exit()
############## End checkRoot() ##############
