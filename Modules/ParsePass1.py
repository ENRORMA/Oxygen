def ParsePass1(LocalSourceFileContent):
    LocalSourceLines = LocalSourceFileContent.split("\n")
    LineCount = len(LocalSourceLines)
    LineCounter = 0
    while LineCounter < LineCount:
        LineCounter += 1
        Line = LocalSourceLines[:1]
        print(Line)
        Line = "".join(Line)
        CommentCheck = Line.lstrip()[:1]
        if CommentCheck != "#":
            GoodLines = LocalSourceLines[:1]
        LocalSourceLines = LocalSourceLines[1:]
    #print(GoodLines)