!/usr/bin/python
import os
import sys


def packageFiles(targetVersion,revNo):
	
	if targetVersion ==  "7.1.1-145":
		if revNo == "1":
			print "Latest Revision is 16 are you sure you want to continue with this RCM Revision Package" 
		elif revNo =="2"		
	elif targetVersion == "7.1.2-21":
	
########Version 7.2.0-401, onlyIfNeeded folder starts at Rev14########	
	elif targetVersion == "7.2.0-401":	
		avaimFULL = "avaim_FULL_7.2.0-401_1.tgz"
		checksumFULL = "4157a8149defc2b994eaa1d190f17c5e"
		avinstallerFile = "UpgradeAvinstaller-7.2.0-401.avp"
		upgradeFile = "AvamarUpgrade-7.2.0-401.avp"
		customerHandoverScript = "customer_handover_v5.1.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.2.0-401.avp"
		
		if revNo == "1":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev1.tgz"
				checksumRCM = ""
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q2-v8.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "2":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev2.tgz"
				checksumRCM = "9a483b55bc7acdc47391d6bc42fa982bc070a1fae9a4d3c5f96a9e6e6fc1b542"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				customerHandoverScript = "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "3":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev3.tgz"
				checksumRCM = "82a6787a2980d1758a611e11d2639e3b7051e1f298c66f8100fb85406290b35d"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_245396.avp"]
				customerHandoverScript = "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "4":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev4.tgz"
				checksumRCM = "ec50ad9056ab892e0035e3eae38cda31e4f80a0ce9e2bccff2c69a66175bb7da"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_247126.avp"]
				customerHandoverScript = "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "5":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev5.tgz"
				checksumRCM = ""
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_247126.avp"]
				customerHandoverScript = "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "6":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev6.tgz"
				checksumRCM = "1a7dea4fa16dc92d74a07663ff46986006b279ce0a91c55ef194a7e9c85b7dee"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = "customer_handover_v5.2.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "7":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev7.tgz"
				checksumRCM = "H73554fc8a8aae9b198ff34b009d3c9b3d5f05300eb2dd092da280dd47c7f4bea"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = "customer_handover_v5.3.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "8":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev8.tgz"
				checksumRCM = "a1135774b0f09c1d8c520f5e0dc25d8a51189ce31fbc03529d526b75b6f2aae6"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250387.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "9":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev9.tgz"
				checksumRCM = ""
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "10":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev10.tgz"
				checksumRCM = "8d4d92cf6fc76961a63befc369290d4475f8684f87e0ecfda75961a5f2287fa6"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "11":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev11.tgz"
				checksumRCM = "fb4e6fa48b73a48f1d87f53688f07855e4fba0af1e92075a4305d19a65984d33"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"		
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "12":
			question = "Latest Revision is 14, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev12.tgz"
				checksumRCM = "2fc3c3ea40345d6cb4f8edfd5f4b00f85ca3c73838052a627dbe454a39cfb6c2"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.2.0-401_HF250901.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_250725.avp", "v7_2_0_401_HF_278332.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
				
		if revNo == "14":
				avaimRCM = "avaim_RCM_Updates_7.2.0-401_Rev14.tgz"
				checksumRCM = "79c774e66cf8f1e9c33f6f31c80ffac98c017eef5c4119661ce74101ea713e20"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_2_0_401_HF_279816.avp", "v7_2_0_401_HF_278332.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"

		if revNo == "13":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()		
		
		else:
			print "Please enter a valid Revision and try again."

########Version 7.2.1-32, onlyIfNeeded folder starts at Rev14########			
	elif targetVersion == "7.2.1-32":
		avaimFULL = "avaim_FULL_7.2.1-32_1.tgz"
		checksumFULL = "2946bdeb7c47582bb5860712aeec96d2"
		avinstallerFile = "UpgradeAvinstaller-7.2.1-32.avp"
		upgradeFile = "AvamarUpgrade-7.2.1-32.avp"
		customerHandoverScript = "customer_handover_v5.2.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.2.1-32.avp"
		
		if revNo == "1":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-31_Rev1.tgz"
				checksumRCM = "c0456dd294f64ca23c83bba6c39bd180d92dd6db68704217b0c0bc35fb5e9218"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF199778.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		if revNo == "2":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev2.tgz"
				checksumRCM = ""
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q3-v4.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()			
		
		if revNo == "3":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev3.tgz"
				checksumRCM = "e1c581a09e3259d7dc528a6c63f7cd5b65beacdac1bff46a3cdb3dc583f54239"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()	
				
		if revNo == "4":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev4.tgz"
				checksumRCM = "8e70a51b604c4db1208465a5b5faffce2c7991dc859925fc327df658e9ffd70d"
				callableFixesMandatory = ["AvPlatformOsRollup_2015-Q4-v7.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_248125.avp"]
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		if revNo == "5":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev5.tgz"
				checksumRCM = "dbdd5638f321d7652104f94eacb6409e3ef25f22b4d46f2d55ea794340e79ffc"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_248125.avp"]
				customerHandoverScript = "customer_handover_v5.3.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		if revNo == "6":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev6.tgz"
				checksumRCM = "a31946e8343359daae24e49665aa671dcd3e1ef4794eae7d5e42f537f8a4d093"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp", "AvamarHotfix-7.2.1-32_HF254389.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		if revNo == "7":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev7.tgz"
				checksumRCM = "bf64ac3781e8bb0314789f32187d5997b6f22a911c505db6a8cc41ec0bd9a976"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.1-32_HF254389.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()			
		
		if revNo == "9":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev9.tgz"
				checksumRCM = "86754492141683d71f9ba81b8238775c37a3e9c1330bc29d4c2eee76f10e7849"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.2.1-32_HF265294.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
		
		if revNo == "10":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev10.tgz"
				checksumRCM = "eee59c00b290a39b140b7718b35009e49e8213ca198cca1665198a889a292f2f"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.1-32_HF265294.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		if revNo == "11":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev11.tgz"
				checksumRCM = "63deb7af774f6905df945aad682c4bd36ba974c714d8adb8cb34fbd3b8a10ec3"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.2.1-32_HF265294.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_250967.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()
					
		if revNo == "12":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev12.tgz"
				checksumRCM = "d862acd33337d92ca7ea965cec66cd3e168f6f801f7723f35a197b5316ad2dc5"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.2.1-32_HF265294.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_277897.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		if revNo == "14":
			question = "Latest Revision is 15, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev14.tgz"
				checksumRCM = "0c160172bea9dac013e2444589155ebc08293476614d44f6b1a1da4abc80d5ad"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp", "v7_2_1_32_HF_261520.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_2_1_32_HF_282216.avp"]
				customerHandoverScript = "customer_handover_v5.4.sh"
			else:
				print "Please download the latest Revision and try again."
				sys.exit()

		if revNo == "15":
			avaimRCM = "avaim_RCM_Updates_7.2.1-32_Rev15.tgz"
			checksumRCM = "5bbcb5296b1c3637ca70d30906f416c8938222831942a1d8296a01fcb374bd44"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.2.1-32_HF278646.avp", "v7_2_1_32_HF_261520.avp"]
			callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = ["v7_2_1_32_HF_284664.avp"]
			customerHandoverScript = "customer_handover_v5.4.sh"
		
		if revNo == "8":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()
		
		if revNo == "13":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()	
		
		else:
			print "Please enter a valid Revision and try again."			
			sys.exit()
	
########Version 7.3.0-233, onlyIfNeeded folder starts at Rev10########	
	elif targetVersion == "7.3.0-233":
		avaimFULL = "avaim_FULL_7.3.0-233_1.tgz"
		checksumFULL = "162f5ba81993056226cfc690eb312c0a"
		avinstallerFile = "UpgradeAvinstaller-7.3.0-233.avp"
		upgradeFile = "AvamarUpgrade-7.3.0-233.avp"
		customerHandoverScript = "customer_handover_v5.4.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.3.0-233.avp"
			
			if revNo == "1":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev1.tgz"
					checksumRCM = "6a9cc24ff160815bc102832e58127aaa0632821c0b398aa7bff25b6a50da1fc4"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q1-v2.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()
					
			if revNo == "2":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev2.tgz"
					checksumRCM = "687cd61820caf6b6852a06ecbf79a1f900b808e96fdf5949015f9dad139bc516"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()
					
			if revNo == "3":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev3.tgz"
					checksumRCM = "689040ade19879b3cb8f4f6e5f68a2f963b09964849fc97a40b3f4a8b5ff1de8"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "4":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev4.tgz"
					checksumRCM = "d01acdd80965d0df7d17a0d2ec2ea949e2442dbf8a631f34bbdff3e778d4c75a"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.3.0-233_HF267305.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "5":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev5.tgz"
					checksumRCM = "841ad3b5852ae1b1a15e064946e65ba6bb91c13da6cfa9d5890d2f323cb601b2"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp", "AvamarHotfix-7.3.0-233_HF269398.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "6":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev6.tgz"
					checksumRCM = "c21e0cb8b1b84997c65414f8f31e222812bfe3092ba8ef6c6b05fd49da89341a"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.3.0-233_HF269398.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "7":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev7.tgz"
					checksumRCM = "be544c10c2a8e53bea88bda825161b2ebea951276b756be7666c900e57c3b956"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp", "AvamarHotfix-7.3.0-233_HF269398.avp", "v7_3_0_233_HF_271301.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "8":
			question = "Latest Revision is 10, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev8.tgz"
					checksumRCM = "132e350aad464395d62918f578971a5a3775b30b37327bdf7ead385df17bcc85"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp", "AvamarHotfix-7.3.0-233_HF269398.avp", "v7_3_0_233_HF_271301.avp", "v7_3_0_233_HF_278483.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "10":
				avaimRCM = "avaim_RCM_Updates_7.3.0-233_Rev8.tgz"
				checksumRCM = "60c60bc2574d40f5ecb726fea12396e7b3265c2f7745cb7129a930fe17790501"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp", "v7_3_0_233_HF_271301.avp", "v7_3_0_233_HF_278483.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "Gen4tPlatformSupportUpdate-HF274401.avp", "gen4s-ssd-1000day-hotfix-282000.avp"]
				notCallableFixesMandatory = [""]
			
			if revNo == "9":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()	
		
		else:
			print "Please enter a valid Revision and try again."			
			sys.exit()
	
	########Version 7.3.1-125, onlyIfNeeded folder starts at Rev6########
	elif targetVersion == "7.3.1-125"
		avaimFULL = "avaim_FULL_7.3.1-125_1.tgz"
		checksumFULL = "457440734e86e3dc5c7b9baa49911712"
		avinstallerFile = "UpgradeAvinstaller-7.3.1-125.avp"
		upgradeFile = "AvamarUpgrade-7.3.1-125.avp"
		customerHandoverScript = "customer_handover_v5.4.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.3.1-125.avp" 
			
			if revNo == "1":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev1.tgz"
					checksumRCM = "faa7f6c1d1fab40adb2c64afc2bc7797bd37a102c1f08596b53033ea4ead5bdf"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q2-v7.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "2":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev2.tgz"
					checksumRCM = "983a30a2a8d22d2c0fdedaec75e48cf7c93a0de1a036e68feb519fc74ff9f965"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = [""]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "3":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev3.tgz"
					checksumRCM = "130a39a3209dbe2ec148675994fd07a170adf683ef446d4f9903ab7d103ea0ae"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = ["v7_3_1_125_HF_274527.avp"]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "4":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev4.tgz"
					checksumRCM = "24daa8b5763393c35fe381bd2b810ead132d83f12440ff338b9ae18631ae32d6"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = ["v7_3_1_125_HF_274527.avp", "v7_3_1_125_HF_278484.avp"]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "6":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev6.tgz"
					checksumRCM = "6a1c98b660060ae91c83f6768d740c8564b09406ca95927fa002bdbb2063cd35"
					callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
					notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp"]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "7":
			question = "Latest Revision is 8, are you sure you want to continue with this RCM Revision Package?"
				if query_yes_no(question):
					avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev7.tgz"
					checksumRCM = "28b29e4a3a92fbb7d38d2465500c43dcd6b63eafbf0e31fef12d3e544240b6a5"
					callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp"]
					callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "Gen4tPlatformSupportUpdate-HF274401.avp", "gen4s-ssd-1000day-hotfix-282000.avp"]
					notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp", "v7_3_1_125_mc_cumulative_201706.avp"]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()	

			if revNo == "8":
				avaimRCM = "avaim_RCM_Updates_7.3.1-125_Rev8.tgz"
				checksumRCM = "630ec4de7f007721d4d15aab3557dbe5318a90bff50c9b126b9f64138a0a8800"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.3.1-125_HF276786.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "Gen4tPlatformSupportUpdate-HF274401.avp", "gen4s-ssd-1000day-hotfix-282000.avp"]
				notCallableFixesMandatory = ["v7_3_1_125_HF_275129.avp", "v7_3_1_125_HF_278484.avp", "v7_3_1_125_mc_cumulative_201707.avp"]
				else:
					print "Please download the latest Revision and try again."
					sys.exit()

			if revNo == "5":
			print "This revision was recalled, please download the latest revision and try again"
			sys.exit()	
		
		else:
			print "Please enter a valid Revision and try again."			
			sys.exit()
						
	########Version 7.4.0-242########
	elif targetVersion == "7.4.0-242"
		avaimFULL = "avaim_FULL_7.4.0-242_1.tgz"
		checksumFULL = "8ece38bc6853e7ee1ba83418acc78d966865d0a1add57107755a31d1547c24b2"
		avinstallerFile = "UpgradeAvinstaller-7.4.0-242.avp"
		upgradeFile = "AvamarUpgrade-7.4.0-242.avp"
		customerHandoverScript = "customer_handover_v5.4.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.4.0-242.avp"
			
			if revNo == "1":
				avaimRCM = "avaim_RCM_Updates_7.4.0-242_Rev1.tgz"
				checksumRCM = "335972bee336bd82b446ba66aae2baab169adcf95424e36a123f6ca1a2f4af1d"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q3-v3.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = [""]
		
		else:
			print "Please enter a valid Revision and try again."			
			sys.exit()		
		
	########Version 7.4.1-58, onlyIfNeeded folder starts at Rev3########
	elif targetVersion == "7.4.1-58":
		avaimFULL = "avaim_FULL_7.4.1-58_1.tgz"
		checksumFULL = "896050a0b296fa9c5f78036e1a1b6238a464fd4ce8d49c6884aa998ae04e2b94"
		avinstallerFile = "UpgradeAvinstaller-7.4.1-58.avp"
		upgradeFile = "AvamarUpgrade-7.4.1-58.avp"
		customerHandoverScript = "customer_handover_v5.4.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.4.1-58.avp"
		
		if revNo == "1":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev1.tgz"
				checksumRCM = "3e4ca2d64deef8493ad93bfe292b158a164b68a2e4f15760cc5501d9f637d3e9"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF249880.avp"]
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
				checksumRCM = "762a2c19213feab414ed66557051c37be5a80584738bde5b86cdc27aae3b7884"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp"]
				notCallableFixesMandatory = ["v7_4_1_58_mc_cumulative_201705.avp"] 
				
			else
				print "Please download the latest Revision and try again."
				sys.exit()
		elif revNo == "4":
			question = "Latest Revision is 5, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev4.tgz"
				checksumRCM = "250848fde1d56f8ecfa1937932d4edfc42c88f134272b7b8704e89a2fbccd89e"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.4.1-58_HF278715.avp", "v7_4_1_58_mc_cumulative_201706.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = ["v7_4_1_58_HF_285198.avp"]
			
			else
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "5":
			avaimRCM = "avaim_RCM_Updates_7.4.1-58_Rev5.tgz"
			checksumRCM = "52e124795fe3d69e2d0867089960cca8586ca37a4046817b4ec9c1758d33d9e9"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "AvamarHotfix-7.4.1-58_HF278715.avp", "v7_4_1_58_mc_cumulative_201707.avp"]
			callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = ["v7_4_1_58_HF_285198.avp"]
		
		else:
			print "Please enter a valid Revision number"
			sys.exit()
		
	########Version 7.5.0-183, onlyIfNeeded folder starts at Rev1########
	elif targetVersion == "7.5.0-183":
		avaimFULL = "avaim_FULL_7.5.0-183.tgz"
		checksumFULL = "896050a0b296fa9c5f78036e1a1b6238a464fd4ce8d49c6884aa998ae04e2b94"
		avinstallerFile = "UpgradeAvinstaller-7.5.0-183.avp"
		upgradeFile = "AvamarUpgrade-7.5.0-183.avp"
		customerHandoverScript = "customer_handover_v5.4.sh"
		UpgradeClientDownloads = "UpgradeClientDownloads-7.5.0-183.avp"
		
		if revNo == "1":
			question = "Latest Revision is 3, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question):
				avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev1.tgz"
				checksumRCM = "db6944cb413a5770b3c4ed24d70f8b5e917aa007985a9541ae1c17862c0d6204"
				callableFixesMandatory = ["AvPlatformOsRollup_2016-Q4-v2.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = []
			else 
				print "Please download the latest Revision and try again."
				sys.exit()
			
		elif revNo == "2":
			question = "Latest Revision is 3, are you sure you want to continue with this RCM Revision Package?"
			if query_yes_no(question);
				avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev2.tgz"
				checksumRCM = "9538b5ee7140c7a0e208e535f557e642f2284a490b26fa0b5ffb5adeea65f61f"
				callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp"]
				callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
				notCallableFixesMandatory = []
			else 
				print "Please download the latest Revision and try again."
				sys.exit()
				
		elif revNo == "3":
			avaimRCM = "avaim_RCM_Updates_7.5.0-183_Rev3.tgz"
			checksumRCM = "37261200db29444a9549f2ec3f98514b0e61339cfbf90bf9498633251da70299"
			callableFixesMandatory = ["AvPlatformOsRollup_2017-Q1-v9.avp", "v7_5_0_183_mc_cumulative_201707.avp"]
			callableFixesOptional = ["AdsGen4sPowerSupplyRedundancy-HF260924.avp", "gen4s-ssd-1000day-hotfix-282000.avp", "Gen4tPlatformSupportUpdate-HF274401.avp"]
			notCallableFixesMandatory = []
			
		else:	
			print "Please enter a valid Revision number"
			sys.exit()
			
	else:
		print "Please enter a valid Version number"
		sys.exit()
	


	########Return Paths for required packages########
	return(avaimFULL, avaimRCM, fileNames)
	
	output avaimFULL, checksumFULL, avinstallerFile, upgradeFile, customerHandoverScript, UpgradeClientDownloads,  avaimRCM, checksumRCM, collableFixesMandatory, callableFixesOptional, notCallableFixesMandatory 
	
	avaim_Full_7.4.1/mv2repo/AvamarUpgrade, avaim_Full_7.4.1/others/UpgradeClientDownloads, 
	