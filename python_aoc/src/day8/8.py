from math import lcm

def solution1():
    path = "python_aoc/src/day8/nodes.txt"
    file = open(path, "r")
    lines = file.readlines()
    directions = lines.pop(0)
    print(directions)
    lines.pop(0)
    nodes = []
    for l in lines:
        tname = l.split('=')[0].strip()
        tleft = l.split('=')[1].replace('(', "").replace(')', "").strip().split(',')[0]
        tright = l.split('=')[1].replace('(', "").replace(')', "").strip().split(',')[1].strip()
        nodes.append([tname, tleft, tright])
    current_node = searchNode('AAA', nodes)
    iterator = 0
    steps = 0
    while(current_node[0]!= 'ZZZ'):
        if (iterator > 20000):
            break
        iterator_mod = iterator % (len(directions) - 1)
        direction = directions[iterator_mod]
        current_node = searchNode(current_node[1], nodes) if direction == 'L' else searchNode(current_node[2], nodes)
        iterator += 1
        print(current_node[0])
    print(iterator)


def searchNode(node_name, list):
    i = 0
    while list[i][0] != node_name:
        i += 1
    return list[i]

# Why do I not first have to check if the thing is even cycling? Do we just trust??? This one i probably would have had some trouble with if i didnt see the lcm thing
def solution2():
    path = "python_aoc/src/day8/nodes.txt"
    file = open(path, "r")
    lines = file.readlines()
    directions = lines.pop(0)
    print(directions)
    lines.pop(0)
    nodes = []
    a_nodes = []
    cycles = []
    for l in lines:
        tname = l.split('=')[0].strip()
        tleft = l.split('=')[1].replace('(', "").replace(')', "").strip().split(',')[0]
        tright = l.split('=')[1].replace('(', "").replace(')', "").strip().split(',')[1].strip()
        nodes.append([tname, tleft, tright])
        if tname[2] == 'A':
            a_nodes.append([tname, tleft, tright])
    for a in a_nodes:
        current_node = searchNode(a[0], nodes)
        iterator = 0
        steps = 0
        while(current_node[0][2] != 'Z'):
            direction = directions[iterator % (len(directions) - 1)]
            current_node = searchNode(current_node[1], nodes) if direction == 'L' else searchNode(current_node[2], nodes)
            iterator += 1
        cycles.append(iterator)
    print(lcm(*cycles))

solution2()