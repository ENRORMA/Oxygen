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
					OutputList += [WordInput]
				case "dec":
					OutputList += [WordInput]
				case "mov":
					OutputList += [WordInput]
				case "push":
					OutputList += [WordInput]
				case "pop":
					OutputList += [WordInput]
				case "jmp":
					OutputList += [WordInput]
					# put code here to get output if input "jmp 20" output should be "mov 20 $pc \n jmp"
					# figure out how to scedule additions to the output list in the future
				case "jnz":
					OutputList += [WordInput]
				case "jov":
					OutputList += [WordInput]
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
								# add error message here
								print("Something went wrong")
								pass
			print(f"is address {IsAddress}")
			print(f"is comment {IsComment}")
			print(f"is number {IsNumber}")
	print("")
	print(OutputList)
