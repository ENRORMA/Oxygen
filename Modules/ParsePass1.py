def ParsePass1(LocalSourceFileContent):
	LineList = LocalSourceFileContent.split("\n")
	LineCount = len(LineList)
	LineCounter = 0
	while LineCounter < LineCount:
		LineCounter += 1
		Line = LineList[:1]
		Line = "".join(Line)
		Line = Line.lstrip()
		if Line[:1] != "#":
			InstructionList = Line.split()
			CheckInstruction = "".join(InstructionList[:1])
			match CheckInstruction:
				case "jmp":
					print("yes")
			print(InstructionList)
			print(CheckInstruction)
			print("next")

		LineList = LineList[1:]