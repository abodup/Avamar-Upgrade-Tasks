############### Start curlFile() ####################
def curlFile(link, destinationFileName, user="root"):
	#add timeout and check if no ftp
	output = cmdOut('sudo -u %s curl -o %s --disable-eprt --connect-timeout 30 -P - -O %s 2>&1' %(user, destinationFileName, link))
	if output.split('\r')[-1].split(" ")[0] == '100':
		return True
	else: return False
############### End curlFile() ####################