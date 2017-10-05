############### Start aviUpgradeNeeded() ###############
def aviUpgradeNeeded(currentFamily, currentVersion, targetFamily, targetVersion):
	version = cmdOut("avinstaller.pl --version").split("_")[0].split("\t")[2].split("\n")[0]
	if version == targetVersion:
		return False
	elif (currentFamily == "6.1" or currentFamily == "7.0" or currentVersion == "7.1.0-370") and (targetFamily == "7.1" or targetFamily == "7.2"):
		return True
	elif (currentFamily == "7.1") and (targetFamily == "7.3"):
		return True
	else: return False
############### End aviUpgradeNeeded() ###############
