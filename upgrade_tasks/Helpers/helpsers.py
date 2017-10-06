############## Start checkRoot() ##############
checkRoot():
	
	output = cmdOut("whoami")
	output = output.split("\n")[0]
	if output != "root":
		print"Error: please switch to root account and relaunch the script"
		sys.exit()
############## End checkRoot() ##############

############### Start localTime() ###############
def localTime():
	return str(datetime.now())
############### End localTime() ###############

############### Start setupLog() ###############
def setupLog():
	global log 
	os.system("touch upgrade_tasks.log")
	os.system("chmod a+rw upgrade_tasks.log")
	log = open("./upgrade_tasks.log", "wa")
	text = """
##################################################################
#                      Log File Created                          #
##################################################################
"""
	log.write("%s %s"%(localTime(), text))
	log.close()
############### End setupLog() ####################

############## Start printLog() ##############
def printLog(message):
	log = open("./upgrade_tasks.log", "a")
	log.write("%s %s \n" %(localTime(), message))
	log.close()
############## Start printLog() ##############

############## Start printBoth() ##############
def printBoth(message):
	log = open("./upgrade_tasks.log", "a")
	log.write("%s %s \n" %(localTime(), message))
	log.close()
	print message
############## End printBoth() ##############

############### Start cmd() ###############
def cmd(command):
		printLog("Command: %s" %command)
		os.system("%s 2>&1 | tee -a upgrade_tasks.log" %s)
############### End cmd() ####################

############### Start comdOut() ###############
def cmdOut(command):
	printLog("Command: %s" %command)
	output = os.popen(command).read()
	printLog("Output: %s" %output)
	return output
############### End cmdOut() ####################

############### Start curlFile() ####################
def curlFile(link, destinationFileName, user="root"):
	#add timeout and check if no ftp
	output = cmdOut('sudo -u %s curl -o %s --disable-eprt --connect-timeout 30 -P - -O %s 2>&1' %(user, destinationFileName, link))
	if output.split('\r')[-1].split(" ")[0] == '100':
		return True
	else: return False
############### End curlFile() ####################


############### Start query_yes_no() ###############
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        #sys.stdout.write(question + prompt)
		printLog("Stopping Question")
		printBoth(question + prompt)
        choice = raw_input().lower()
		printLog("Answer is: %s" %choice)
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            printBoth("Please respond with 'yes' or 'no'\n""(or 'y' or 'n').\n")
            #sys.stdout.write("Please respond with 'yes' or 'no' "
                          #"(or 'y' or 'n').\n")
############### End query_yes_no() ###############

############### Start getInput() ###############
def getInput(question):

	sys.stdout.write(question)
	input = raw_input()
	return input 
    
############### getInput() ###############
