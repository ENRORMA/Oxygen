#!/bin/python3

#Python Version:	3.10
#Author:			ENRORMA
#License:			GPL3
#Oxygen Version:	0.1

import os
import sys
from Modules.ReadFile import *
from Modules.ParsePass1 import *

#temporary
SourceFileName = "source"

#language stuff
Language = "English"

LanguageImport = f"from Po.{Language} import *"
#check if language exists
try:
	exec(LanguageImport)
except Exception:
	quit("Unsupported Language")

exec(LanguageImport)

Works(0,1,2)


#stage 1 assembling
SourceFileContent = ReadFile(SourceFileName)
SourceFileParse1Content = ParsePass1(SourceFileContent)