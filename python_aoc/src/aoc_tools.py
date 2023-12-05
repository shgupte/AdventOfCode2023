def extractNumber(line, index):
    num = 0
    pointer = index
    digits = []
    if not line[pointer].isdigit():
        print("not a number")
        print(line[pointer])
        return TypeError
    while pointer > 0 and line[pointer - 1].isdigit():
        pointer -= 1
    while pointer < len(line) - 1 and line[pointer].isdigit():
        digits.append(int(line[pointer]))
        pointer += 1
    for i in range(len(digits)):
        num += int(int(digits[i]) * pow(10, int(len(digits) - i - 1)))
    return num

