############### Start extraSteps() ###############

def extraSteps():

	print "Archiving package-survey* to  Rollups_Survey_Save.tgz "
	os.system("tar czvf /data01/avamar/var/Rollups_Survey_Save.tgz -P /data01/avamar/var/package-survey*")
	print "Removing package-survey*"
	os.system("rm -f /data01/avamar/var/package-survey*")
############### End extraSteps() ###############
