############### Start curlFile() ####################
def curlFile(link, destinationFileName, user="root"):

	printBoth("Trying to download %s to destination %s as user=%s" %(link, destinationFileName, user))
	output = cmdOut('sudo -u %s curl -o %s --disable-eprt --connect-timeout 30 -P - -O %s 2>&1' %(user, destinationFileName, link))
	if output.split('\r')[-1].split(" ")[0] == '100':
		printBoth("Download Successful")
		return True
	else:
		printBoth("Download not successful maybe FTP is not enabled on this Avamar server, or the Avamar Server is not connected to the internet")
		return False
############### End curlFile() ####################