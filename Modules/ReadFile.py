#!/bin/python3
def ReadFile(FileName):
	with open(FileName, "r") as file:
		FileContent = file.read().splitlines()
		Lines = len(FileContent)
		LineNumber = 0
		OutputWordList = []
		OutputLineList = []
		while LineNumber < Lines:
			Line = FileContent[LineNumber]
			Line = Line.split()
			LineNumber += 1
			WordNumber = 0
			WordCount = len(Line)
			while WordNumber < WordCount:
				Word = Line[WordNumber]
				WordNumber += 1
				OutputWordList += [Word] #white spaces should be removed before this line
				if WordNumber == WordCount:
					OutputLineList += [OutputWordList]
					OutputWordList = []
	return OutputLineList