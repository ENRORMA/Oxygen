#!/bin/python3

def ReadFile(LocalFileName):
    with open(LocalFileName, "r") as file:
        LocalFileContent = file.read().splitlines()
        Lines = len(LocalFileContent)
        LineNumber = 0
        while LineNumber < Lines:
            Line = LocalFileContent[LineNumber]
            Line = Line.split()
            print(Line)
            LineNumber += 1
            WordNumber = 0
            WordCount = len(Line)
            while WordNumber < WordCount:
                Word = Line[WordNumber]
                print(Word)
                WordNumber += 1
    return LocalFileContent