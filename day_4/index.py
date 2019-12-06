import re

def main():
	#265275, 781584
	maybe = []
	for i in range(265275, 781584):
		if check(i):
			maybe.append(i)
	print('maybee', len(maybe), maybe)

def check(number):
	return hasAtLeastTwoEtc(number) and neverDecreases(number)

def hasAtLeastTwoEtc(number):
    num = str(number)
    matches = re.findall('00+|22+|33+|44+|55+|66+|77+|88+|99+', num)
    if matches and min([len(match) for match in matches]) == 2:
        return True
    else:
        return False

def neverDecreases(number):
	stringou = str(number)
	for i in range(0, len(stringou) - 1):
		if int(stringou[i]) > int(stringou[i + 1]):
			return False
	return True


main()