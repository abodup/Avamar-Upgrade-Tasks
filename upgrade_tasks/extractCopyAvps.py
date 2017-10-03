############### Start extractCopyAvps() ###############
def extractCopyAvps(currentFamily, currentVersion, targetFamily, targetVersion, avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads, avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory):
		
	clearRepo()
	checkExtractPackage(avaimFULL, checksumFULL)
	checkExtractPackage(avaimRCM, checksumRCM)
	
	if aviUpgradeNeeded(currentFamily, currentVersion, targetFamily, targetVersion):
		printBoth("Avinstaller upgrade is needed to " + targetVersion)
		cmd("mv /usr/local/avamar/src/" + avinstallerFile + " /data01/avamar/repo/packages")
		printBoth(avinstallerFile + " File copied to Avinstaller Repo and ready, please go to GUI")
		question = "whenever Avinstaller upgrade done please press yes to continue"
		cond = True
		while cond
			if query_yes_no(question):
				if cmd("avinstaller.pl --version") == targetVersion:
					printBoth("Avinstaller version checked and you can go to Avamar server upgrade")
					cond = False
				else: printBoth("please check the Avinstaller upgrade again")
			else: printBoth("please check the Avinstaller upgrade again")
	else:
		printBoth("You can go to Avamar server upgrade")
	
	cmd("mv /usr/local/avamar/src/" + upgradeFile + " /data01/avamar/repo/packages")
	printBoth(upgradeFile + " is being moved now to /data01/avamar/repo/packages")
	
	clientVer = cmdOut("ls /usr/local/avamar/var/avi/server_data/package_data/ | grep UpgradeClientDownloads-")
	clientVer1 = clientVer.split("_")[0].split("-",1)[1][0:-4]
	#UpgradeClientDownloads-7.2.1-32.avp_1496764981077 -> UpgradeClientDownloads-7.2.1-32.avp -> 7.2.1-32.avp -> 7.2.1-32
	if clientVer1 != targetVersion:
		question = "UpgradeClientDownloads pacakge needed, if you would like to add it now with server upgrade, please press yes."
		if query_yes_no(question):
			cmd("mv /usr/local/avamar/src/" + UpgradeClientDownloads + " /data01/avamar/repo/packages")
			printBoth(UpgradeClientDownloads + " is being moved now to /data01/avamar/repo/packages")
		else: printBoth("please don't forget to move the package after upgrade.")
	else: printBoth(UpgradeClientDownloads + " already installed before, you don't need to include.")
		
	length=0
	while (length < len(callableFixesMandatory)):
		cmd("mv /usr/local/avamar/src/" + callableFixesMandatory[length] + " /data01/avamar/repo/packages")
		printBoth(callableFixesMandatory[length] + " is being moved now to /data01/avamar/repo/packages")
		length += 1

	length=0
	while (length < len(callableFixesOptional)):
		question = "would you like to add " + callableFixesOptional[length] + " with the server upgrade as a callable package?"
		if query_yes_no(question):
			cmd("mv /usr/local/avamar/src/" + callableFixesOptional[length] + " /data01/avamar/repo/packages")
			printBoth(callableFixesOptional[length] + " is being moved now to /data01/avamar/repo/packages")
			length += 1
		else: length += 1
############### End extractCopyAvps() ##########################################
