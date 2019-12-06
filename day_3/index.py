import numpy as np
import math
import functools

def makeMap():
	grid = []
	i = 0
	while i < 40000:
		j = 0
		grid.append([])
		while j < 40000:
			grid[i].append('.')
			j += 1
		i += 1
	return grid


def printMap(map):
	for row in map:
		print(row, '\n')


def findDirection(instruction):
	return instruction[:1]

def findDistance(instruction):
	return int(instruction[1:])

def move(direction, distance):
	if (len(map) / 2 < distance):
		return False

def checkSize(map, distance):
	return ((len(map) / 2) > int(distance) )

def checkCollision(machin, symbol):
	return (machin == 'O')

def placeSnake(snake1, map, symbol):
	steps = 0
	maybe = []
	start = [20000, 20000]
	map[start[0]][start[1]] = 'X'
	pos = start[:]
	for instruction in snake1:
		count += 1
		direction = findDirection(instruction)
		distance = findDistance(instruction)
		if (direction == 'R'):
			pos[1] += 1
			for i in range(int(pos[1]), int(pos[1]) + distance):
				if symbol == '0' and checkCollision(map[pos[0]][i], symbol) == True:
					maybe.append([start, pos[0], i])
					map[pos[0]][i] = '+'
				else:
					map[pos[0]][i] = symbol
				pos[1] = i
				step += 1
			
		if (direction == 'U'):
			pos[0] -= 1
			for j in range(int(pos[0]), int(pos[0]) - distance, -1):
				if symbol == '0' and checkCollision(map[j][pos[1]], symbol) == True:
					maybe.append([start, j, pos[1]])
					map[j][pos[1]] = '+'
				else:
					map[j][pos[1]] = symbol
				pos[0] = j
				step += 1

		if (direction == 'L'):
			pos[1] -= 1
			for k in range(int(pos[1]), int(pos[1]) - distance, -1):
				if symbol == '0' and checkCollision(map[pos[0]][k], symbol) == True:
					maybe.append([start, pos[0], k])
					map[pos[0]][k] = '+'
				else:
					map[pos[0]][k] = symbol
				pos[1] = k
				step += 1

		if (direction == 'D'):
			pos[0] += 1
			for l in range(int(pos[0]), int(pos[0]) + distance):
				if symbol == '0' and checkCollision(map[l][pos[1]], symbol) == True:
					maybe.append([start, l, pos[1]])
					map[l][pos[1]] = '+'
				else:
					map[l][pos[1]] = symbol
				pos[0] = l
				step += 1

	return maybe

def calculateDistance(result):
	startX = result[0][1]
	startY = 40000 - result[0][0]
	finishX = result[2]
	finishY = 40000 - result[1]
	print(startX, startY)
	print(finishX, finishY)
	return (abs(startX - finishX) + abs(startY - finishY))

def main():
	maybeUltimate = []
	values = []
	with open('datas.txt') as file:
		values = file.read().split('\n')
	snake1 = values[0].split(',')
	snake2 = values[1].split(',')
	map = makeMap()
	result0 = placeSnake(snake1, map, 'O')
	result1 = placeSnake(snake2, map, '0')
	result = result1 + result0
	if result == False:
		print('Pas de collision')
		exit()
	for perhaps in result:
		isIt = calculateDistance(perhaps)
		if isIt < 0:
			isIt = -isIt
		maybeUltimate.append(isIt)
	print(maybeUltimate)

main()