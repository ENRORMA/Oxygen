#!/bin/python3

def ReadFile(LocalFileName):
    with open(LocalFileName, "r") as file:
        LocalFileContent = file.read()
    return LocalFileContent