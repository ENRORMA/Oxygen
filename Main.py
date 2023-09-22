#!/bin/python3

#Python Version:	3.10
#Author:		ENRORMA
#License:		GPL3
#Oxygen Version:	0.1

import os
import sys
from Modules.ReadFile import *
from Modules.ParsePass1 import *
SourceFileName = "source"

SourceFileContent = ReadFile(SourceFileName)
SourceFileParse1Content = ParsePass1(SourceFileContent)
