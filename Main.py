#!/bin/python3

#Python Version:	3.10
#Author:			ENRORMA
#License:			GPL3
#Oxygen Version:	0.1

import os
import sys

from Modules.CreateConfig import *
from Modules.LanguageLoader import *

#temporary
SourceFileName = "source"

#config and language set up
CreateConfig()
LoadLanguage()
from Po.Language import *

#import modules here because it has to be created first
from Modules.ReadFile import *
from Modules.ParsePass1 import *
from Modules.ByteCounter import *

#stage 1 assembling
Input = ReadFile(SourceFileName)
Parsed1 = ParsePass1(Input)
BytesCounted = ByteCounter(Parsed1)