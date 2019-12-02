import numpy as np
import math
import functools

def integerize(value):
	return int(value)


def resolveOpCode(array, noun, verb):
	tmp = array
	size = len(array)
	tmp[1] = noun
	tmp[2] = verb
	i = 0
	while i < size:
		one = tmp[i + 1]
		two = tmp[i + 2]
		result = tmp[i + 3]
		if (tmp[i] == 1):
			tmp[result] = tmp[one] + tmp[two]
		elif (array[i] == 2):
			tmp[result] = tmp[one] * tmp[two]
		else:
			return tmp
		i += 4
	return tmp


def findOp():
	return [1, 2]

def main():
	values = []
	with open('data.txt') as file:
		values = file.read().split(',')
	intValues = list(map(integerize, values))
	print(findOp())

main()