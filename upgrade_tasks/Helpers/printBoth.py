############## Start printBoth() ##############
def printBoth(message):
	log = open("./upgrade_tasks.log", "a")
	log.write("%s %s \n" %(localTime(), message))
	log.close()
	print message
############## End printBoth() ##############
