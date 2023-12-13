def getExpectedValue(reading) -> int:
    list = [reading]
    result = 0
    while sum(reading) != 0:
        temp = nextLayer(reading)
        list.append(temp)
        reading = temp
    for l in list[::-1]:
        result = l[0] - result
    return result
    
def nextLayer(reading) -> list:
    lst = []
    for i in range((len(reading) - 1)):
        lst.append((reading[i + 1] - reading[i]))
    lst = [0] if len(reading) < 3 else lst
    return lst
def solution2():
    path = "python_aoc/src/day9/readings.txt"
    file = open(path, "r")
    lines = file.readlines()
    total = 0
    for l in lines:
        l = list(map(int, l.split()))
        total += getExpectedValue(l)
    print(total)

solution2()