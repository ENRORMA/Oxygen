#!/bin/python3
import os
def CreateConfig():
	HomeDirectory = os.path.expanduser("~")
	if os.path.exists(HomeDirectory + "/.config/ENRORMA/Oxygen/Config") == True:
		pass
	else:
		os.mkdir(HomeDirectory + "/.config/ENRORMA")
		os.mkdir(HomeDirectory + "/.config/ENRORMA/Oxygen")
		#create file and fill with config stuff idk
	#use configparser to config file
CreateConfig()