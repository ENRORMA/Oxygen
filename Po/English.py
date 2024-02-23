#!/bin/python3
def Works(a,b,c):
	print(f"zero {a} one {b} two {c}")

def Print_Error_Unknown_Instruction_pass_1(Instruction, Line):
	quit(f"Unknown Instruction \"{Instruction}\" on line {Line}.")