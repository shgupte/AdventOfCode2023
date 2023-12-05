# Day 1 Problem 2023
def reverse(input):
    return input [::-1]

def lookForNum(input):
    for i in range(len(input)):
        value = ord(input[i]) - 48
        if (value <= 9 and value >= 0):
            return ord(input[i]) - 48
        else:
            continue
        
def dayOne1(): 
    total = 0
    text = open("python_aoc/src/day1/calibration.txt", "r")
    lines = text.readlines()
    for l in lines:
        total += 10*lookForNum(l) + 1*lookForNum(reverse(l))
    print(total)

dayOne1()
        


