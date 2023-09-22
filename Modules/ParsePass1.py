def ParsePass1(SourceFileContent):
    LineCount = len(SourceFileContent)
    LineNumber = 0
    while LineNumber < LineCount:
        LineInput = SourceFileContent[LineNumber]
        LineNumber += 1
        WordCount = len(LineInput)
        WordNumber = 0
        while WordNumber < WordCount:
            WordInput = LineInput[WordNumber]
            WordNumber += 1
            print(WordInput)