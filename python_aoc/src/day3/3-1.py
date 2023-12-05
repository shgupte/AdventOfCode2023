path = "python_aoc/src/day3/parts.txt"
file = open(path, "r")
lines = file.readlines()
coords = []

def solution():
    total = 0

    for l in lines:
        for m in range(len(l) - 1):
            if ord(l[m]) != 46 and not l[m].isdigit():
                coords.append([lines.index(l), m])
    for l in lines:
        m = 0
        while m < len(l):
            temp = []
            adjacent = False
            num = 0
            if l[m].isdigit():
                temp.append(l[m])
                if isAdj([lines.index(l), m], coords):
                    adjacent = True
                while(l[m+1].isdigit()):
                    if isAdj([lines.index(l), m + 1],coords):
                       adjacent = True
                    temp.append(l[m+1])
                    m += 1
            for i in range(len(temp)):
                num += int(int(temp[i]) * pow(10, int(len(temp)-i-1)))
            if adjacent:
                total += num
            m += 1
    print(total)


def isAdj(input, const):
    for c in const:
        if abs(input[0] - (c[0])) < 2 and (abs(input[1] - c[1]) < 2):
            return True
        else:
            continue
    return False

solution()



