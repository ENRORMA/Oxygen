def ParsePass1(LocalSourceFileContent):
    LocalSourceLines = LocalSourceFileContent.split("\n")
    Line = LocalSourceLines[:1]
    Line = "".join(Line)
    print(Line)