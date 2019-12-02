import numpy as np
import math
import functools

def stripn(value):
	return value.strip('\n')

def megaCalcul(value):
	integr = int(value)
	return math.floor((integr // 3)) - 2


def megaMegaCalcul(value):
	remainingFuel = megaCalcul(value)
	total = 0
	while (remainingFuel > 0):
		total = total + remainingFuel
		remainingFuel = megaCalcul(remainingFuel)
	return total

def main():
	values = []
	with open('data.txt') as file:
		values = file.readlines()

	newValues = map(stripn, values)

	finalValues = map(megaMegaCalcul, newValues)
	
	print(np.sum(list(finalValues)))

main()