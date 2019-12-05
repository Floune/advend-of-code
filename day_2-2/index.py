import numpy as np
import math
import functools

def integerize(value):
	return int(value)


def resolveOpCode(array, noun, verb):
	size = len(array)
	array[1] = noun
	array[2] = verb
	i = 0
	while i < size:
		one = array[i + 1]
		two = array[i + 2]
		result = array[i + 3]
		if (array[i] == 1):
			array[result] = array[one] + array[two]
		elif (array[i] == 2):
			array[result] = array[one] * array[two]
		else:
			return array
		i += 4
	return array


def findOp(intValues):
	theOne = 19690720
	noun = 0
	verb = 0
	while noun <= 99:
		verb = 0
		while verb <= 99:
			if (resolveOpCode(intValues[:], noun, verb)[0] == theOne):
				return [noun, verb]
			verb += 1
		noun += 1

	return 'not found...'

def main():
	values = []
	with open('data.txt') as file:
		values = file.read().split(',')
	intValues = list(map(integerize, values))
	print(findOp(intValues))
	
main()