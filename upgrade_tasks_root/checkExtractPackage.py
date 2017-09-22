def checkExtractPackage(package, packageChecksum):
	cond = False
	while not cond:
		### Check Package Exists
		while not os.path.isfile("/usr/local/avamar/src/" + package):
			print package + " File doesn't exists at /usr/local/avamar/src"
			question = "please place the %s file under the specified location, press yes to continue or press no to abort" %package
			if not query_yes_no(question): sys.exit()
		print package + " File Found"
		
		##### Checksum of the file ####
	
		print "checking Checksum of " + package
		f = os.popen("sha256sum /usr/local/avamar/src/" + package)
		checksum = f.read().split()[0]
		print checksum
		if checksum == packageChecksum:
			cond = True
			print package + " checksum OK" 
		else: 
			print package + " checksum is not correct"
			question = "please download the %s file again, press yes to check for files again, or press no to abort" %package
			if not query_yes_no(question): sys.exit()
		
	#### Extracting avaimFull
	print "Extracting " + package
	os.system("tar xzvf /usr/local/avamar/src/%s -C /usr/local/avamar/src" %package)
