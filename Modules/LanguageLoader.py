#!/bin/python3
import os
import configparser
from pathlib import Path
def LoadLanguage():
	HomeDirectory = os.path.expanduser("~")
	ModuleDirectory = os.path.abspath(os.path.dirname(__file__))
	config = configparser.ConfigParser()
	config.read(HomeDirectory + "/.config/ENRORMA/Oxygen/Config")
	Language = config["User Settings"]["Language"]
	try:
		os.remove(f"{ModuleDirectory}/../Po/Language.py")
	except Exception:
		pass
	Path(f"{ModuleDirectory}/../Po/Language.py").symlink_to(f"{ModuleDirectory}/../Po/{Language}.py")