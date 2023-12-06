def getInt(x):
    return int(x)

def getMappedNumber(input, mappy):
    # print(input)
    for m in mappy: 
        nums = m.split()
        ints = list((map(getInt, nums)))
        if ints[1] > input or input > ints[1] + ints[2] - 1:
            continue
        else:
            return ints[0] + (input - ints[1])
    return input
        
        
def source_init(input):
    source = input[0]
    source = source.split(":")
    source = source[1]
    source.replace('\n', ' ')
    return source.split()
        
def solution():
    path = "python_aoc/src/day5/maps.txt"
    file = open(path, "r")
    maps = []
    lines = file.readlines()
    source_numbers = source_init(lines)
    lines.pop(0)
    current_map = []
    for l in lines:
        if not l[0].isdigit():
            if len(current_map) != 0:
                maps.append(current_map)
            current_map = []
            continue 
        current_map.append(l)
    maps.append(current_map)

    print(maps)
    number = 1234567890123
    for s in source_numbers:
        temp = getInt(s)
        for m in maps:
            temp = getMappedNumber(temp, m)
        if temp < number and temp :
            number = temp
    print(number)
        

solution()
