from Po.Language import *
def ParsePass1(SourceFileContent):
	LineCount = len(SourceFileContent)
	LineNumber = 0
	OutputList = []
	SceduleList = []
	Output = []
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
				case "xor":
					OutputList += [WordInput]
				case "and":
					OutputList += [WordInput]
				case "or":
					OutputList += [WordInput]
				case "not":
					OutputList += [WordInput]
				case "add":
					OutputList += [WordInput]
				case "sub":
					OutputList += [WordInput]
				case "inc":
					OutputList += ["add"]
					SceduleList += [[1, 1], [2, LineInput[WordNumber]]]
				case "dec":
					OutputList += ["sub"]
					SceduleList += [[1, 1], [2, LineInput[WordNumber]]]
				case "mov":
					OutputList += [WordInput]
				case "push":
					OutputList += [WordInput]
				case "pop":
					OutputList += [WordInput]
				case "jmp":
					SceduleList += [[0, "mov"], [1, "$pc"], [2, "jmp"]]
				case "jnz":
					SceduleList += [[0, "mov"], [1, "$pc"], [2, "jnz"]]
				case "jov":
					SceduleList += [[0, "mov"], [1, "$pc"], [2, "jov"]]
				case "halt":
					OutputList += [WordInput]
				case "nop":
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
								Print_Error_Unknown_Instruction_pass_1(WordInput, LineNumber)
								pass
			#calculate the scedule list
			SceduleListCounter = 0
			while len(SceduleList) != SceduleListCounter:
				if SceduleList[SceduleListCounter][0] == 0:
					OutputList += [SceduleList[SceduleListCounter][1]]
					SceduleList.pop(SceduleListCounter)
					SceduleListCounter += -1
				else:
					SceduleList[SceduleListCounter][0] += -1
				SceduleListCounter += 1
			print(f"is address {IsAddress}")
			print(f"is comment {IsComment}")
			print(f"is number {IsNumber}")
		if len(OutputList) != 0:
			Output += [OutputList]
		OutputList = []
	print("")
	print(Output)