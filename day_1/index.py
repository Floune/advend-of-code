import numpy as np
import math
import functools

def stripn(value):
	return value.strip('\n')

def megaCalcul(value):
	integr = int(value)
	return math.floor((integr / 3)) - 2

def main():
	values = []
	with open('data.txt') as file:
		values = file.readlines()

	newValues = map(stripn, values)
	finalValues = map(megaCalcul, newValues)
	print(np.sum(list(finalValues)))

main()