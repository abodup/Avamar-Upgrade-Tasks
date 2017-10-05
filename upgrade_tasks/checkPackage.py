############### Start checkPackage() ###############
def checkPackages(package, packageChecksum):
	cond = False
	while not cond:
		### Check Package Exists
		while not os.path.isfile("/usr/local/avamar/src/" + package):
			printBoth(package + " File doesn't exists at /usr/local/avamar/src")
			question = "please place the %s file under the specified location, press yes to continue or press no to abort" %package
			if not query_yes_no(question): sys.exit()
		printBoth(package + " File Found")
		##### Checksum of the file ####
		printBoth("checking Checksum of " + package)
		output = cmdOut("sha256sum /usr/local/avamar/src/" + package)
		checksum = output.split()[0]
		printBoth(checksum)
		if checksum == packageChecksum:
			cond = True
			printBoth(package + " checksum OK" )
		else: 
			printBoth(package + " checksum is not correct")
			question = "please download the %s file again, press yes to check for files again, or press no to abort" %package
			if not query_yes_no(question): sys.exit()
############### End checkPackage() ###############
