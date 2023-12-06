
def getInt(x):
    return int(x)

def solution(): 
    path = "python_aoc/src/day6/times.txt"
    file = open(path, "r")
    lines = file.readlines()
    time = lines[0].split(":")[1].split()
    dist = lines[1].split(":")[1].split()
    time = list(map(getInt, time))
    dist = list(map(getInt, dist))
    final_answer = 1
    for i, t in enumerate(time):
        d = dist[i]
        for j in range(t):
            if j*(t-j) > d:
                final_answer *= (t - 2 * (j -1) -1)
                print(j)
                print( (t - 2 * (j - 1)))
                break
            else:
                continue
    print(final_answer)

def solution2(): 
    path = "python_aoc/src/day6/times.txt"
    file = open(path, "r")
    lines = file.readlines()
    time = lines[0].split(":")[1]
    dist = lines[1].split(":")[1]
    t = int(time.replace(" ", ""))
    d = int(dist.replace(" ", ""))
    final_answer = 1
    print(t)
    print(d)
    for j in range(t):
        if j*(t-j) > d:
            final_answer *= (t - 2 * (j -1) -1)
            print(j)
            print( (t - 2 * (j - 1)) - 1)
            break
        else:
            continue

solution2()