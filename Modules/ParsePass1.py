def ParsePass1(LocalSourceFileContent):
	LineList = LocalSourceFileContent.split("\n")
	LineCount = len(LineList)
	LineCounter = 0
	while LineCounter < LineCount:
		LineCounter += 1
		Line = LineList[:1]
		Line = "".join(Line)
		Line = Line.lstrip()
		print(Line)
		if Line[:1] != "#":
			print("nein")
		else:
			print("ja")
		LineList = LineList[1:]

		#GoodLines += CheckedLine