def preUpgradeTasks():
	
	prePostTech, targetVersion , revNo ,currentVersion= getArgs()
	print "Starting Pre-upgrade tasks for version", targetVersion
	packageFiles(targetVersion)
	
	
	

	
	avaimFull = "avaim_FULL_7.4.1-58_1.tgz"
	avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev4.tgz"
	extractUpgradeFiles(avaimFull, avaimRCM)
