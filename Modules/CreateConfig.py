#!/bin/python3
import os
import configparser
def CreateConfig():
	HomeDirectory = os.path.expanduser("~")
	if os.path.exists(HomeDirectory + "/.config/ENRORMA/Oxygen/Config") == True:
		pass
	else:
		try:
			os.mkdir(HomeDirectory + "/.config/ENRORMA")
		except Exception:
			pass
		try:
			os.mkdir(HomeDirectory + "/.config/ENRORMA/Oxygen")
		except Exception:
			pass

		config = configparser.ConfigParser()
		config ["User Settings"] = {
			"Language":"English"}
		with open(HomeDirectory + "/.config/ENRORMA/Oxygen/Config", "w") as ConfigFile:
			config.write(ConfigFile)
