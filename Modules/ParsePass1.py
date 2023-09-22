def ParsePass1(SourceFileContent):
    LineCount = len(SourceFileContent)
    LineNumber = 0
    OutputList = []
    while LineNumber < LineCount:
        LineInput = SourceFileContent[LineNumber]
        LineNumber += 1
        WordCount = len(LineInput)
        WordNumber = 0
        while WordNumber < WordCount:
            IsAddress = False
            IsComment = False
            IsNumber = False
            WordInput = LineInput[WordNumber]
            WordNumber += 1
            print(WordInput)
            match WordInput:
                case "jmp":
                    print("du hurensohn")
                    OutputList += [WordInput]
                case _:
                    CharInput = WordInput[:1]
                    match CharInput:
                        case "#":
                            IsComment = True
                            WordNumber = WordCount + 1
                        case "$":
                            IsAddress = True
                            OutputList += [WordInput]
                        case _:
                            try:
                                int(WordInput)
                                IsNumber = True
                                OutputList += [WordInput]
                            except Exception:
                                #add error message here
                                pass
            print(f"is address {IsAddress}")
            print(f"is comment {IsComment}")
            print(f"is number {IsNumber}")
        print("")
        print(OutputList)