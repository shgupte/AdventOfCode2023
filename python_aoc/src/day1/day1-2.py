# Day 1 Problem 2023

numbers = [["zero", 0], ["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9]]

def reverse(input):
    return input [::-1]

def lookForNum(input, reverse):
    index = 0
    num = 0
    for i in range(len(input)):
        value = ord(input[i]) - 48
        if (value <= 9 and value >= 0):
            num = ord(input[i]) - 48
            index = i
            break
        else:
            continue
    for i in numbers:
        str = " "
        if (reverse):
            str = i[0][::-1]
        else:
            str = i[0]
        try:
            temp = input.index(str)
            if temp < index:
                index = temp
                num = i[1]
        except:
            continue
    return num

def dayOne2(): 
    total = 0
    text = open("python_aoc/src/day1/calibration.txt", "r")
    lines = text.readlines()
    for l in lines:
        print(l)
        print(10*lookForNum(l, False) + 1*lookForNum(reverse(l), True))
        total += 10*lookForNum(l, False) + 1*lookForNum(reverse(l), True)
    print(total)
    
dayOne2()

