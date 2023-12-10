def dayTwo1(): 
    text = open("python_aoc/src/day2/games.txt", "r")
    lines = text.readlines()
    counter = 0
    total = 5050
    for l in lines:
        counter +=1
        k = l.replace(" ", "")
        k = k[6:]
        print(k)
        print(total)
        for m in range(len(k) - 2):
                if (k[m].isdigit() and  k[m+1].isdigit()):
                     if (ord(k[m + 1]) - 48 > 2 and k[m + 2] == "r" ):
                          print("fail")
                          total-= lines.index(l) + 1
                          break
                     elif (ord(k[m + 1]) - 48 > 3 and k[m + 2] == "g" ):
                          print("fail")
                          total-= lines.index(l) + 1
                          break
                     elif (ord(k[m + 1]) - 48 > 4 and k[m + 2] == "b" ):
                          print("fail")
                          total-= lines.index(l) + 1
                          break 
                     elif (int(k[m]) > 1):
                          print("fail")
                          total-= lines.index(l) + 1
                          break 


    print(total)

dayTwo1()
