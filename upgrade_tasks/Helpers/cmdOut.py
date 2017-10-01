############### Start comdOut() ###############
def cmdOut(command):
	printLog("Command: %s" %command)
	output = os.popen(command).read()
	printLog("Output: %s" %output)
	return output
############### End cmdOut() ####################
