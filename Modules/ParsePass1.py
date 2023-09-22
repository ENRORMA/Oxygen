def ParsePass1(SourceFileContent):
    LineCount = len(SourceFileContent)
    LineNumber = 0
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
                case "":
                    pass
                case _:
                    CharInput = WordInput[:1]
                    match CharInput:
                        case "#":
                            IsComment = True
                        case "$":
                            IsAddress = True
                        case _:
                            try:
                                int(WordInput)
                                IsNumber = True
                            except Exception:
                                pass
            print(f"is address {IsAddress}")
            print(f"is comment {IsComment}")
            print(f"is number {IsNumber}")