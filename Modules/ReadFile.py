#!/bin/python3
def ReadFile(LocalFileName):
    with open(LocalFileName, "r") as file:
        LocalFileContent = file.read().splitlines()
        Lines = len(LocalFileContent)
        LineNumber = 0
        OutputWordList = []
        OutputLineList = []
        while LineNumber < Lines:
            Line = LocalFileContent[LineNumber]
            Line = Line.split()
            #print(Line)
            LineNumber += 1
            WordNumber = 0
            WordCount = len(Line)
            while WordNumber < WordCount:
                Word = Line[WordNumber]
                WordNumber += 1
                #print(Word)
                OutputWordList += [Word]
                if WordNumber == WordCount:
                    OutputLineList += [OutputWordList]
                    OutputWordList = []
        print(OutputLineList)
    return LocalFileContent