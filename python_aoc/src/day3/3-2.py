path = "python_aoc/src/day3/parts.txt"
file = open(path, "r")
lines = file.readlines()

def soln():
    total = 0
    gears = []
    for l in lines:
        for m in range(len(l) - 1):
            if l[m] == "*":
                gears.append([lines.index(l), m])
    for g in gears:
        total += checkRatio(g, lines)
    print(total)

def addc(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def checkRatio(gear, lines):
    numbers_found = 0
    positions = [[0, -1], [0, 1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    numbers = []
    for p in positions:
        temp = addc(gear, p)
        if lines[temp[0]][temp[1]].isdigit():
            numbers.append(extractNumber(lines[temp[0]], temp[1]))
            numbers_found += 1
            if p == [1, 0]:
                positions.remove([1, 1])
                positions.remove([1, -1])
            if p == [-1, 0]:
                positions.remove([-1, 1])
                positions.remove([-1, -1]) 
            if numbers_found > 1:
                return numbers[0]*numbers[1]
    return 0

def extractNumber(line, index):
    num = 0
    pointer = index
    digits = []
    if not line[pointer].isdigit():
        print(line[pointer ] +  " is not a number.")
        return TypeError
    while pointer > 0 and line[pointer - 1].isdigit():
        pointer -= 1
    while pointer < len(line) - 1 and line[pointer].isdigit():
        digits.append(int(line[pointer]))
        pointer += 1
    for i in range(len(digits)):
        num += int(int(digits[i]) * pow(10, int(len(digits) - i - 1)))
    return num

soln()






