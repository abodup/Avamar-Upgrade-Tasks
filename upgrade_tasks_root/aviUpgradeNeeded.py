def aviUpgradeNeeded(currentFamily, currentVersion, targetVersion):
	if (currentFamily == "6.1" or currentFamily == "7.0" or currentVersion == "7.1.0-370") and (targetFamily == "7.1" or targetFamily == "7.2"):
		return True
	
	elif (currentFamily == "7.1") and (targetFamily == "7.3"):
		return True
	else: return False