def solution1():
    path = "python_aoc/src/day4/lottery.txt"
    file = open(path, "r")
    lines = file.readlines()
    total = 0
    for l in lines:
        my_numbers = set(map(int, l.split(":")[1].split("|")[0].split()))
        winning_numbers = set(map(int, l.split(":")[1].split("|")[1].split()))
        winners = winning_numbers.intersection(my_numbers)
        points = 2**(len(winners) - 1) if len(winners) > 0 else 0
        print(points)
        total += points
    print(total)

class Card:
    def __init__(self, number):
        path = "python_aoc/src/day4/lottery.txt"
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.card_number = number
        self.my_nums = set(map(int, lines[number - 1].split(":")[1].split("|")[0].split()))
        self.winning_nums = set(map(int, lines[number - 1].split(":")[1].split("|")[1].split()))
        self.points = len(self.my_nums.intersection(self.winning_nums))

    def prize_cards(self):
        temp = []
        for i in range(1, self.points + 1):
            temp.append(self.card_number + i)
        return temp


class solution:
    def __init__(self):
        self.total = 0
        self.card_list = []
    
    def getTotalCards(self, input):
        


sol = solution()
sol.getTotalCards(Card(1))



