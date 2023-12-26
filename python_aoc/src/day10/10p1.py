def solution_1():
    path = "python_aoc/src/day10/maze.txt"
    file = open(path, "r")
    lines = file.readlines()
    start = search_s(lines)
    cur = start
    valid_positions = [start]
    last = start
    steps = 0
    while (cur != start or steps == 0):
        # Manually entering first move
        if cur == start:
            cur = addVec(cur, [0, -1])
            last = start
        else: 
            temp = cur
            valid_positions.append(cur)
            cur = getNextPostion(cur, lines, last)
            last = temp
        steps += 1

    print(getAreaInRow(lines, valid_positions))


def search_s(matrix) -> list:
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if column == 'S':
                return [i, j]

def addVec(a, b) -> list:
    return [a[0] + b[0], a[1] + b[1]]

def getNextPostion(entry, matrix, last_move) -> list:
    down = [1, 0]
    up = [-1, 0]
    left = [0, -1]
    right = [0, 1]
    match matrix[entry[0]][entry[1]]:
        case '|':
            return addVec(entry, up) if  addVec(entry, up) != last_move else addVec(entry, down)
        case '-':
            return addVec(entry, left) if  addVec(entry, left) != last_move else addVec(entry, right)
        case 'J':
            return addVec(entry, up) if  addVec(entry, up) != last_move else addVec(entry, left)
        case 'L':
            return addVec(entry, up) if  addVec(entry, up) != last_move else addVec(entry, right)
        case '7':
            return addVec(entry, down) if  addVec(entry, down) != last_move else addVec(entry, left)
        case 'F':
            return addVec(entry, down) if  addVec(entry, down) != last_move else addVec(entry, right)


# Based on point in polygon ray-casting algorithm: https://en.wikipedia.org/wiki/Point_in_polygon
def getAreaInRow(matrix, indexes) -> int:
    area = 0
    row = []
    segments_passed = 0
    last_pipe = ''
    for i, row in enumerate(matrix):
        segments_passed = 0
        for j, r in enumerate(row):
            if [i, j] in indexes:
                if r == 'J' and last_pipe == 'F':
                    segments_passed += 1
                if r == '7' and last_pipe == 'L':
                    segments_passed += 1
                if r == '|':
                    segments_passed += 1
                if r not in ['-', 'J', '7', '|']:
                    last_pipe = r               
            elif segments_passed % 2 == 1:
                area += 1
    return area



solution_1()