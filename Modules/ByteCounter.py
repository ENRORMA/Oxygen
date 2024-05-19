#!/bin/python3
from Po.Language import *
def CheckIfInt(Input, Count, Operands):
	if Count == 1:
		if Input[Count + 1][:1] == "$":
			return False
	if Count == 2:
		if Input[Count + 2][:1] == "$":
			return False
	return True

def ByteCounter(Input):
	Count = 0
	Bytes = 0
	Word = Input[Count]
	while Count != len(Input):
		match Input[Count]:
			case "xor":
				Bytes += 2
				Count += 3
				if CheckIfInt(Input, Count, 2) == True:
					Bytes += 1
				else:
					Bytes += 8
			case "and":
				Bytes += 2
				Count += 3
				if CheckIfInt(Input, Count, 2) == True:
					Bytes += 1
				else:
					Bytes += 8
			case "or":
				Bytes += 2
				Count += 3
				if CheckIfInt(Input, Count, 2) == True:
					Bytes += 1
				else:
					Bytes += 8
			case "not":
				Bytes += 3
				Count += 3
			case "add":
				Bytes += 2
				Count += 3
				if CheckIfInt(Input, Count, 2) == True:
					Bytes += 1
				else:
					Bytes += 8
			case "sub":
				Bytes += 2
				Count += 3
				if CheckIfInt(Input, Count, 2) == True:
					Bytes += 1
				else:
					Bytes += 8
			case "inc":
				Bytes += 2
				Count += 2
			case "dec":
				Bytes += 2
				Count += 2
			case "mov":
				Bytes += 2
				Count += 3
				if CheckIfInt(Input, Count, 2) == True:
					Bytes += 1
				else:
					Bytes += 8
			case "jmp":
				Count += 1
				Bytes += 1
			case "jnz":
				Bytes += 1
				Count += 1
			case "jov":
				Bytes += 1
				Count += 1
			case "halt":
				Bytes += 1
				Count += 1
			case "nop":
				Bytes += 1
				Count += 1
			case "int":
				Bytes += 1
				Count += 1
	print(Bytes)
	return(bytes)