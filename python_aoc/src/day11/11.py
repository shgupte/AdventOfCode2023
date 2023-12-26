import aoc_tools as aoc

def solution_1():
    lines = aoc.extractInput("python_aoc/src/day11/sky.txt")
    reference = lines
    for i, row in enumerate(reference):
        if len(set(row)) == 1:
            lines.insert(i + 1, row)
    lines = zip(*lines[::-1])
    reference = lines
    for i, row in enumerate(reference):
        if len(set(row)) == 1:
            lines.insert(i + 1, row)
    for i in range(3):
        lines = zip(*lines[::-1])
    print(lines)