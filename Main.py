#!/bin/python3

#Python Version:	3.10
#Author:			ENRORMA
#License:			GPL3
#Oxygen Version:	0.1

import os
import sys
from Modules.ReadFile import *
from Modules.ParsePass1 import ParsePass1
from Po.Language import *

#temporary
SourceFileName = "source"

#Works(0,1,2)


#stage 1 assembling
SourceFileContent = ReadFile(SourceFileName)
SourceFileParse1Content = ParsePass1(SourceFileContent)