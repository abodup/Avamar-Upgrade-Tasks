#!/usr/bin/python
import os
import sys


def main():
	print "Please enter target version"
	targetVersion = raw_input()
	(avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads,  avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory) = packageFiles(targetVersion)
	print avaimFULL + "\n" + checksumFULL + "\n" + avinstallerFile + "\n" + upgradeFile + "\n" + customerHandoverScript + "\n" + UpgradeClientDownloads + "\n" + avaimRCM + "\n" + checksumRCM + "\n"
	print "Mandatory callable fixes = "
	print callableFixesMandatory
	print "\n"
	print "Mandatory non callable fixes = "
	print notCallableFixesMandatory
	print "\n"
	print "Optional callable fixes = "
	print callableFixesOptional

def packageFiles(targetVersion):
	avaimFULL = ""
	checksumFULL = ""
	checksumFULL = ""
	avinstallerFile = ""
	upgradeFile = ""
	customerHandoverScript = ""
	UpgradeClientDownloads = ""
	avaimRCM = ""
	checksumRCM = ""
	callableFixesMandatory = []
	callableFixesOptional = []
	notCallableFixesMandatory = []
	
		
########Version 7.1.1-145, onlyIfNeeded folder starts at Rev16########
########Customer Handover mail starts at Rev7########	
	if targetVersion ==  "7.1.1-145":
		avaimFULL = "avaim_FULL_7.1.1-145_1.tgz"
		checksumFULL = "a32a21dcb25158a7df761ac004cc4b1a"
		avinstallerFile = "UpgradeAvinstaller-7.1.1-145.avp"
		upgradeFile = "AvamarUpgrade-7.1.1-145.avp"
		customerHandoverScript = "avaim_FULL_7.1.1-145_1/scripts/customer_handover_v5.0.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.1.1-145.avp"
		
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.1.1-145_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo
		
		if revNo == "1":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev1.tgz"
				checksumRCM = "439c97968fdf3f2816662ec08a2e653187380f42f9295a8e70e9374462a7afd3"
				callableFixesMandatory = ["AvPlatformOsRollup_2014-Q4-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = [""]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "2":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev2.tgz"
				checksumRCM = "7218b202d1c5b92a59a37ebdc588ce49e2db31f274c3bae05a5244a660582f23"
				callableFixesMandatory = ["AvPlatformOsRollup_2014-Q4-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_229688.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()				

		elif revNo == "3":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev3.tgz"
				checksumRCM = "c93b9739d223ac707759948b909d1ee69f76ad965508482f7a8960092534efc3"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_231762.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "4":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev4.tgz"
				checksumRCM = "c9e23c5cf56730d0f3402436b7ff27acd1b4b87396a0801af4c361f1ec462968"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_235000.avp", "Hotfix234581-7.1.1-145.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "5":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev5.tgz"
				checksumRCM = "bde7814c2f11addc3c3652c7b0cae9cef55638f20af917795df2376c3899e4ce"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_235000.avp", "Hotfix234581-7.1.1-145.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "6":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev6.tgz"
				checksumRCM = "cc57c7ddbfc88124f135f8691e9e74f37a9331cf1c9cceafea2356aaac4bccf4"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_240802.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
			
		elif revNo == "7":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev7.tgz"
				checksumRCM = "1f2f3b0136af7f05ed6da79eff7a911d100e77b942d627409ffac6a3afc05d87"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "8":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev8.tgz"
				checksumRCM = "68a60caa9c1da1c69e169e433e84b99738da3f32e78e5f634c5009a19d00f559"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
				
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "9":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev9.tgz"
				checksumRCM = "60f286c9979f7a777ee70d95830c042c3bcd1379bd20f73110fe5a5cdac8f7c6"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "10":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev10.tgz"
				checksumRCM = "c8c91fc52836c488b7b83b2fcb81ebccd02b371212069121bc0eed3054a66020"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "11":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev11.tgz"
				checksumRCM = "a7d407fbd902f4ac13dda354ec5b5b643d0fc6fc9fc60213a3bebd9681704ad4"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_241892.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()				
				
		elif revNo == "12":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev12.tgz"
				checksumRCM = "eee16139334b52c83661cb41c60e7795c5e8b637da64153f973dbf9f20ccdab5"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "13":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev13.tgz"
				checksumRCM = "ded7bbbd4a7d2106c7ab3a8053f6ef35921abcbf07c8f81e1382760cb8746bac"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "14":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev14.tgz"
				checksumRCM = "569e92036e246b86c4ab296a8e3193ee111aa371f8199b3975237fdba83fee7c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "16":
			avaimRCM = "avaim_RCM_Updates_7.1.1-145_Rev16.tgz"
			checksumRCM = "04a4b1d1c3ae46cbf159e7fbcab923b5178a30450bc161af52bbcd0bc924be3b"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF199778.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = ["v7_1_1_145_HF_258017.avp", "v7_1_1_145_HF_235341.avp", "Hotfix234581-7.1.1-145.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		elif revNo == "15":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()
		
		else:
			print "Please download a valid Revision and try again."
			sys.exit()		
			
########Version 7.1.2-21, onlyIfNeeded folder starts at Rev16########
########Customer Handover mail starts at Rev4########	
	elif targetVersion == "7.1.2-21":
		avaimFULL = "avaim_FULL_7.1.2-21_1.tgz"
		checksumFULL = "14acc5da8aef98bee63aac72d9461dc7"
		avinstallerFile = "UpgradeAvinstaller-7.1.2-21.avp"
		upgradeFile = "AvamarUpgrade-7.1.2-21.avp"
		customerHandoverScript = "customer_handover_v5.1.sh"
		UpgradeClientDownloads = "avaim_FULL_7.1.2-21_1/scripts/UpgradeClientDownloads-7.1.2-21.avp"
		
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.1.2-21_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo
		
		if revNo == "1":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev1.tgz"
				checksumRCM = "b2161c2cdd3dbb304934e9bbc495e0753bfc1f6ddf87f9a5accd79cd17325d01"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		elif revNo == "2":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev2.tgz"
				checksumRCM = "f33a7a500b8832812de5fd76eb51918e4b311b733a38a1ce1dc7c20e89c5bfbe"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		elif revNo == "3":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev3.tgz"
				checksumRCM = "18a3cb853f197a080b120f1817bce53cf35a5afe0d2c3ae1074d8f5300bc6915"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_241549.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
						
		elif revNo == "4":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev4.tgz"
				checksumRCM = "f645bbdeac54eac373886cb6fbf9abcaf6ff9eaea9f0f258a7c31b91e0f25cd0"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_244284.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
										
		elif revNo == "5":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev5.tgz"
				checksumRCM = "cbe48efbb3b54e3f8289fca38053b94502246584a034fc8b5c81a1ba584c1ce4"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_244284.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
										
		elif revNo == "6":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev6.tgz"
				checksumRCM = "ec79bfb70b5a6b4d0a7ffa967aca671dbaa47851c6bf991c79a61af2902e9eda"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247657.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
														
		elif revNo == "7":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev7.tgz"
				checksumRCM = "bd0432da6c94b75e6f14fa571920652757b87793969525b8db4cc9b2bc8ab4e0"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247657.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																		
		elif revNo == "8":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev8.tgz"
				checksumRCM = "3d715db6f64eb8eb1ea3fe9d12fe18eda751b4fa9528cf150ed82dea38a12f20"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247565.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																						
		elif revNo == "9":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev9.tgz"
				checksumRCM = "0f1416a80f71de39374b305e3a0baf8ca2c1e4504d5cd71c7fd4b25acb4f1416"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_247565.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																										
		elif revNo == "10":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev10.tgz"
				checksumRCM = "9bebbeadbf8547e997c56f9f85daa6249290267d463a6b4aa14135044de98bb3"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_250666.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																														
		elif revNo == "11":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev11.tgz"
				checksumRCM = "456c88b5cc24039076d87b0080b79b51858ec215a517feb510ee81536d47f8fa"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_250666.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																																		
		elif revNo == "12":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev12.tgz"
				checksumRCM = "526122786bc92d6e5e94063f9bcd6b03a94e9c79e1d53cc6bfb5f48880957c18"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_255459.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																																						
		elif revNo == "13":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev13.tgz"
				checksumRCM = "cce27f6f3f8f6b71fab8af68be77caecc1301b132b0fd55d64ff7425d51e6427"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_255459.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																																										
		elif revNo == "14":
			question = "Latest Revision is 16, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev14.tgz"
				checksumRCM = "459b8209ea2c721dc7dca09dd10db50b82a6db1b36d798561c060de8e0e5ba62"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.1.2-21_HF244875.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_1_2_21_HF_255459.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
																																														
		elif revNo == "16":
			avaimRCM = "avaim_RCM_Updates_7.1.2-21_Rev16.tgz"
			checksumRCM = "6cb828681a75ce359c40056ab74311623572fbfe8a2a95d93e16f6f9af805aef"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.1.2-21_HF275857.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF199778.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = ["v7_1_2_21_HF_271927.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		elif revNo == "15":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()
		
		else:
			print "Please download a valid Revision and try again."
			sys.exit()
		
########Version 7.2.0-401, onlyIfNeeded folder starts at Rev14########
########Customer Handover mail starts at Rev2########		
	elif targetVersion == "7.2.0-401":	
		avaimFULL = "avaim_FULL_7.2.0-401_1.tgz"
		checksumFULL = "bb3d10c84fcb344b49bdc0341199a683"
		avinstallerFile = "UpgradeAvinstaller-7.2.0-401.avp"
		upgradeFile = "AvamarUpgrade-7.2.0-401.avp"
		customerHandoverScript = "avaim_FULL_7.2.0-401_1/scripts/customer_handover_v5.1.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.2.0-401.avp"
		
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.2.0-401_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo		
		
		if revNo == "1":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev1.tgz"
				checksumRCM = "f797d1202ec7e6bd757ae74050800295b9c301a9ebe9a104f9fd02a809c6881b"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "2":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev2.tgz"
				checksumRCM = "228387acbf81d2e64b24243d0fad5aed93de64ff8cffd7afac84d122aba55c9c"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "3":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev3.tgz"
				checksumRCM = "9ad5648e2caf6c532f4f1e9451c40e40a2a7f2e29683f37ecac8d4d92aa95daf"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_245396.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "4":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev4.tgz"
				checksumRCM = "84c323242e3648064bb08e3879175e2b531b9ff3496496043e213d93bd2fc30f"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_247126.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "5":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev5.tgz"
				checksumRCM = "57a043531017b01c3c831eed826a303e0412515cff488fe3cc5dfaa7c5b79e66"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_247126.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "6":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev6.tgz"
				checksumRCM = "3a49f655e14ee4132874b84e0f58e92fa882312d552b6d1e2a2abb98d651cd14"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "7":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev7.tgz"
				checksumRCM = "fed7aaec3b1a36f95945f379b37b3fa39d054cacc218acdb802ae125a3e87bdc"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "8":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev8.tgz"
				checksumRCM = "e86ef369e023dcd8ff7d4f10cefabec43298c6f073cf0d4ed74769c80a09cc4a"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "9":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev9.tgz"
				checksumRCM = "4f84599c5f896f499ae532a67ed95b3b21450a939c43c329660adf198292e52d"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "10":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev10.tgz"
				checksumRCM = "b1f5f13c494917a5da7fd637584de41070c81bb9092231151554a9773c34bd7f"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "11":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev11.tgz"
				checksumRCM = "1e1fd41a03ad647cec00edfdf3ec58b6bd63fca6198c59f7a7bd456bcb37dbc8"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"		
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "12":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev12.tgz"
				checksumRCM = "60adcf8ab27340e5c8a8130f99dfdf715ef3a8208fbc195b97f71ec2ba5fb88e"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp", "v7_2_0_401_HF_278332.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "14":
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev14.tgz"
				checksumRCM = "05a5f49d35c32c469e1bcb018ee0055946a6172567ddf2527ab11d6c79fb821a"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF199778.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_279816.avp", "v7_2_0_401_HF_278332.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"

		elif revNo == "13":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()		
		
		else:
			print "Please download a valid Revision and try again."

########Version 7.2.1-32, onlyIfNeeded folder starts at Rev14########
########Customer Handover mail starts at Rev5########				
	elif targetVersion == "7.2.1-32":
		avaimFULL = "avaim_FULL_7.2.1-32_1.tgz"
		checksumFULL = "eaf550f34e17c31e8e777042d1a79ae7"
		avinstallerFile = "UpgradeAvinstaller-7.2.1-32.avp"
		upgradeFile = "AvamarUpgrade-7.2.1-32.avp"
		customerHandoverScript = "avaim_FULL_7.2.1-32_1/scripts/customer_handover_v5.2.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.2.1-32.avp"
		
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.2.1-32_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo
		
		if revNo == "1":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-31_Rev1.tgz"
				checksumRCM = "ef4ff250c597fb04dea91e9639fc53dcf15eb18c56e870494bd081f710ca6a29"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "2":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev2.tgz"
				checksumRCM = "8c6ec8ba75caea245a420c70bd8f09d91dd92fa814519b8137af9024c2304d34"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()			
		
		elif revNo == "3":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev3.tgz"
				checksumRCM = "aa7cc627f59babcbb26bd42b58f54ac09e29873bbd886207134a62f18372011d"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()	
				
		elif revNo == "4":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev4.tgz"
				checksumRCM = "c9f3c03688ad172ca074a03770b956c09c12f823f42bb3601b0949a544d7d1b3"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_248125.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		elif revNo == "5":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev5.tgz"
				checksumRCM = "c0b7169234f1ee158b64f2d659295401b48b5676abe5441af698c95b807c79c3"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_248125.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.3.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		elif revNo == "6":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev6.tgz"
				checksumRCM = "7eefbf94e8e17a8f7c16d4ba378adb80aa1969ad466029e9fba4054e827815b5"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.1-32_HF254389.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "7":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev7.tgz"
				checksumRCM = "d390bd0d229406a15a4372975d426f8d7bb1a8b77e05cb4c06cfc36ccf8d00ba"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.1-32_HF254389.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()			
		
		elif revNo == "9":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev9.tgz"
				checksumRCM = "163002b4b01cf70e6dae1cd38158e69fafa683310cae3e14ec0baeaef17e7c04"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.1-32_HF265294.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		elif revNo == "10":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev10.tgz"
				checksumRCM = "8a7ea7b62b856ad203564a90e55a9d92e9597152396fea4d0ee20eba83f5c14c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.1-32_HF265294.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "11":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev11.tgz"
				checksumRCM = "8ae9215996e4dc3ad84c2e18f0725c7ca4c8cd5b76befdd2e212896c1ec9cc84"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.1-32_HF265294.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
					
		elif revNo == "12":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev12.tgz"
				checksumRCM = "a5e3f7f27b881adc2939c159827171cdfa5fa38768883049b457a9ef484ff467"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.2.1-32_HF265294.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_277897.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "14":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev14.tgz"
				checksumRCM = "cc9da99c9582fb61e52d6a0e071255f8cb7093e5b5bb961f369a182e1585b666"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF249880.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_282216.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "15":
			avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev15.tgz"
			checksumRCM = "bbe9eeb8e26ac72442430b318807810b9165acfd56f8cd4027bd6aaad1c73c34"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp", "v7_2_1_32_HF_261520.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF249880.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = ["v7_2_1_32_HF_284664.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		elif revNo == "8":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()
		
		elif revNo == "13":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()	
		
		else:
			print "Please download a valid Revision and try again."			
			sys.exit()
	
########Version 7.3.0-233, onlyIfNeeded folder starts at Rev10########
########Customer Handover mail starts at Rev1 in scripts########
	elif targetVersion == "7.3.0-233":
		avaimFULL = "avaim_FULL_7.3.0-233_1.tgz"
		checksumFULL = "9ee166a2d28921a8ce1901f4d36dbd50"
		avinstallerFile = "UpgradeAvinstaller-7.3.0-233.avp"
		upgradeFile = "AvamarUpgrade-7.3.0-233.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.3.0-233.avp"
			
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.3.0-233_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo
			
		if revNo == "1":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev1.tgz"
				checksumRCM = "72fa5b32673c9c224a0137cdc974c5a8750efd6751d889201b4b05d034dc403f"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"		
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
					
		elif revNo == "2":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev2.tgz"
				checksumRCM = "6a04f14f15f5dedee6f3e5c011077f25202e2197f1b5adf8f0e045348fe8278e"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
					
		elif revNo == "3":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev3.tgz"
				checksumRCM = "8a99bcaa17a44dbf986d1334c182d56d55f44e7fe0cc092efe9b7a37e184255c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "4":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev4.tgz"
					checksumRCM = "c252c5bc2319ae1c37224ca41d2c69b2ebe6bbe65e9f49b0aa61c78a9b3fc0be"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.3.0-233_HF267305.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
					customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "5":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev5.tgz"
				checksumRCM = "825cf10209b34877a2a4a75c4b110f1595fc0b775398288af0f888f22e514d2b"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.3.0-233_HF269398.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "6":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev6.tgz"
				checksumRCM = "64d4795e222507539b0533e1aa8dd3455e0d13c65f0046643ecbc0c60bc340af"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.3.0-233_HF269398.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "7":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev7.tgz"
				checksumRCM = "1e7b6a928198c4a1ef944658b6ef2366d73497e980fb06a6df4ff3a938960fe2"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.3.0-233_HF269398.avp", "v7_3_0_233_HF_271301.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "8":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev8.tgz"
				checksumRCM = "ad69bde39505c80bd716e734bdff161f4a7672d16a6361e0d2aaececded537c3"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.3.0-233_HF269398.avp", "v7_3_0_233_HF_271301.avp", "v7_3_0_233_HF_278483.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "10":
			avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev8.tgz"
			checksumRCM = "00d35b8fb4464fb8b925483932938291d390f3576d82295e394480e4f7523fe2"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp", "v7_3_0_233_HF_271301.avp", "v7_3_0_233_HF_278483.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = [""]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"	
			
		elif revNo == "9":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()	
		
		else:
			print "Please download a valid Revision and try again."			
			sys.exit()
	
	########Version 7.3.1-125, onlyIfNeeded folder starts at Rev6########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.3.1-125":
		avaimFULL = "avaim_FULL_7.3.1-125_1.tgz"
		checksumFULL = "8695f136d7eecdf1a98032a50fd7a6e9"
		avinstallerFile = "UpgradeAvinstaller-7.3.1-125.avp"
		upgradeFile = "AvamarUpgrade-7.3.1-125.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.3.1-125.avp" 
			
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.3.1-125_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " + revNo
			
		if revNo == "1":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev1.tgz"
				checksumRCM = "51cab07b3c6a753c3316adbdfabc7627d0f0567e4a2ff0e2724cc84cf1e352c1"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "2":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev2.tgz"
				checksumRCM = "08d52bf1b8acdb18dba8f84b7b746b29ec766cc231d5d811d7190ed8e6de081a"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "3":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev3.tgz"
				checksumRCM = "3c01124d7211bcfb4a5f3ffbf8336da4ed8881685797c2e58376c420ade1421b"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_274527.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "4":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev4.tgz"
				checksumRCM = "cc354007f4e88f73e34356c9e100de595bb4e44544cf2ddc9b0e54231acadd6c"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_274527.avp", "v7_3_1_125_HF_278484.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "6":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev6.tgz"
				checksumRCM = "f6f5686df5d74b939eeca4e946afcdecc2df0d65005874729107ebcb117aae33"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		elif revNo == "7":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev7.tgz"
				checksumRCM = "ee18dae44295faa4bd3bc8e5bca80713faafebccb5e295e169f41ba574e22883"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp", "v7_3_1_125_mc_cumulative_201706.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()	

		elif revNo == "8":
			avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev8.tgz"
			checksumRCM = "8ff1e6897354bf4a68520b69ec18e65d18bbb76d25ba77ade1b38303593ad206"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp"]
			notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp", "v7_3_1_125_mc_cumulative_201707.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"

		elif revNo == "5":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()	
		
		else:
			print "Please download a valid Revision and try again."			
			sys.exit()
						
	########Version 7.4.0-242########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.4.0-242":
		avaimFULL = "avaim_FULL_7.4.0-242_1.tgz"
		checksumFULL = "5232fd35e9f495e7040bbb363293a287ba7531e6deb3db518d45905ca9d81bea"
		avinstallerFile = "UpgradeAvinstaller-7.4.0-242.avp"
		upgradeFile = "AvamarUpgrade-7.4.0-242.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.4.0-242.avp"
			
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.4.0-242_Rev*").read()
		output = output.split("\n")
		x = len(output)-2
		new = []
		while (x > 0):
			t = output[x].split(".tgz")[-2].split("Rev")[2]
			new.insert(0, int(t))
			x -= 1
		
		sorted(new, key=int, reverse=True)
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo			
		
		if revNo == "1":
			avaimRCM = "avaim_RCM_Updates_7.4.0-242_Rev1.tgz"
			checksumRCM = "2353b6ada54e7f969b6ec021b13439bedf3b61957a35f6f9779fb262e7a4b59f"
			callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
			callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
			notCallableFixesMandatory = [""]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		else:
			print "Please download a valid Revision and try again."			
			sys.exit()		
		
	########Version 7.4.1-58, onlyIfNeeded folder starts at Rev3########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.4.1-58":
		avaimFULL = "avaim_FULL_7.4.1-58_1.tgz"
		checksumFULL = "896050a0b296fa9c5f78036e1a1b6238a464fd4ce8d49c6884aa998ae04e2b94"
		avinstallerFile = "UpgradeAvinstaller-7.4.1-58.avp"
		upgradeFile = "AvamarUpgrade-7.4.1-58.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.4.1-58.avp"

		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.4.1-58_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo
		
		if revNo == "1":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev1.tgz"
				checksumRCM = "20157e4ce8aebeb126b2eb4e65d9305577927e6fc0064f841b35d0137f73e2f7"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		elif revNo == "2":
			print "This is a recalled revision that can not be used, please download the latest Revision and try again"
			sys.exit()
		
		elif revNo == "3":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev3.tgz"
				checksumRCM = "3701b92b633f3841a290ae5a4259eca3dfa5409c3adbae70e928fab53fe3c898"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_4_1_58_mc_cumulative_201705.avp"] 
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
				
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		elif revNo == "4":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev4.tgz"
				checksumRCM = "59e0d0c5733c60bb81e0116183c6322131cccbdeb237a96d5b53c45089b1f767"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.4.1-58_HF278715.avp", "v7_4_1_58_mc_cumulative_201706.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_4_1_58_HF_285198.avp"]
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "5":
			avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev5.tgz"
			checksumRCM = "fca08b993e7479c122cd39248e94fbccc66a9cd430f347da329da170adf4c783"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.4.1-58_HF278715.avp", "v7_4_1_58_mc_cumulative_201707.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = ["v7_4_1_58_HF_285198.avp"]
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
		
		else:
			print "Please download a valid Revision number"
			sys.exit()
		
	########Version 7.5.0-183, onlyIfNeeded folder starts at Rev1########
	########Customer Handover mail starts at Rev1########
	elif targetVersion == "7.5.0-183":
		avaimFULL = "avaim_FULL_7.5.0-183.tgz"
		checksumFULL = "481f0f39c37ac1ffbc3b1e862ec3337317dcd825d49ee079a67b4a23fdc7483e"
		avinstallerFile = "UpgradeAvinstaller-7.5.0-183.avp"
		upgradeFile = "AvamarUpgrade-7.5.0-183.avp"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.5.0-183.avp"
		
		output = os.popen("ls -lah /usr/local/avamar/src/avaim_RCM_Updates_7.5.0-183_Rev*").read()
		output = output.split("\n")
		x = 0
		new = []
		while (x < len(output)):
			t = output[x]
			if (t):
				t = t.split(".tgz")[-2].split("Rev")[1] 
				t = int(t)
				new.insert(0, t)
				
			x += 1
		
		sorted(new, key=int, reverse=True)
		if not new:
			print "No Revision found"
			sys.exit()			
		revNo = str(new[0]) 
		print "Newest Revision found on this Avamar is:  " +  revNo		
		
		if revNo == "1":
			question = "Latest Revision is 3, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev1.tgz"
				checksumRCM = "e98fd46778ad737e77ee86aa7739f543b53e72796e8802780e7188ec0d74d9d2"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = []
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else: 
				print "Please download the latest Revision and try again."
				sys.exit()
			
		elif revNo == "2":
			question = "Latest Revision is 3, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev2.tgz"
				checksumRCM = "bf8bd1e6f0f47cc1d53469501ff715960ee27817ad3e6bcd7643c846e2a4d8bf"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp"]
				callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = []
				customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			else: 
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "3":
			avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev3.tgz"
			checksumRCM = "cba2e6539ed3bea202f30da072522dc20cb4212277145ef624e26c5a751e8ec3"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "v7_5_0_183_mc_cumulative_201707.avp"]
			callableFixesOptional = ["/only_if_needed/AdsGen4sPowerSupplyRedundancy-HF260924.avp", "/only_if_needed/gen4s-ssd-1000day-hotfix-282000.avp", "/only_if_needed/Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = []
			customerHandoverScript = avaimRCM.split(".tgz")[0] + "/" + "customer_handover_v5.4.sh"
			
		else:	
			print "Please download a valid Revision number"
			sys.exit()
			
	else:
		print "Please download a valid Version number"
		sys.exit()
	
	
	avinstallerFile = avaimFULL.split(".tgz")[0] + "/other_avps/" + avinstallerFile
	upgradeFile = avaimFULL.split(".tgz")[0] + "/mv2repo/" + upgradeFile
	UpgradeClientDownloads = avaimFULL.split(".tgz")[0] + "/other_avps/" + UpgradeClientDownloads
	callableFixesMandatory = [avaimRCM.split(".tgz")[0] + "/" + callableFixesMandatory for callableFixesMandatory in callableFixesMandatory]
	callableFixesOptional = [avaimRCM.split(".tgz")[0] + "/" + callableFixesOptional for callableFixesOptional in callableFixesOptional]
	notCallableFixesMandatory = [avaimRCM.split(".tgz")[0] + "/" + notCallableFixesMandatory for notCallableFixesMandatory in notCallableFixesMandatory]
	
	
	
	########Return Paths for required packages########
	
	return(avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads,  avaimRCM, checksumRCM, callableFixesMandatory, callableFixesOptional, notCallableFixesMandatory) 
	
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
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

############### End query_yes_no() ###############
	
	
main()