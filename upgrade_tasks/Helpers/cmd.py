############### Start cmd() ###############
def cmd(command):
		printLog("Command: %s" %command)
		os.system("%s 2>&1 | tee -a upgrade_tasks.log" %s)
############### End cmd() ####################

