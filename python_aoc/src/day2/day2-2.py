def dayTwo2(): 
    text = open("python_aoc/src/day2/games.txt", "r")
    lines = text.readlines()
    
    total = 0
    for l in lines:
        highestBlue = 0
        highestRed = 0
        highestGreen = 0
        k = l.replace(" ", "")
        k = k[6:]
        for m in range(len(k) - 1):
            if (not k[m].isdigit()):
                continue
            if (k[m].isdigit and k[m+1] == "b"):
                if extractNumber(k, m) > highestBlue:
                    highestBlue = extractNumber(k, m)
                    continue
            elif (k[m].isdigit and k[m+1] == "r"):
               if extractNumber(k, m) > highestRed:
                    highestRed = extractNumber(k, m)
                    continue
            elif (k[m].isdigit and k[m+1] == "g"):
                if extractNumber(k, m) > highestGreen:
                    highestGreen = extractNumber(k, m)
                    continue
        total += highestGreen*highestBlue*highestRed
    print(total)




def extractNumber(line, index):
    num = 0
    pointer = index
    digits = []
    if not line[pointer].isdigit():
        print("not a number")
        print(line[pointer])
        return TypeError
    while pointer > 0 and line[pointer - 1].isdigit():
        print()
        pointer -= 1
    while pointer < len(line) - 1 and line[pointer].isdigit():
        digits.append(int(line[pointer]))
        pointer += 1
    for i in range(len(digits)):
        num += int(int(digits[i]) * pow(10, int(len(digits) - i - 1)))
    return num

dayTwo2()