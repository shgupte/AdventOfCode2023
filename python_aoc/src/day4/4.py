# This code is heretical with respect to all principle of programming

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
        self.won_cards = []
        self.my_nums = set(map(int, lines[number - 1].split(":")[1].split("|")[0].split()))
        self.winning_nums = set(map(int, lines[number - 1].split(":")[1].split("|")[1].split()))
        self.points = len(self.my_nums.intersection(self.winning_nums))

    def prize_cards(self):
        temp = []
        for i in range(1, self.points + 1):
            temp.append(self.card_number + i)
        return temp


def get_card_count(input_card):
    card = input_card
    remaining_prizes = card.prize_cards()
    if len(remaining_prizes) == 0:
        return 1
    for r in remaining_prizes:
        card = Card(r)
        remaining_prizes += card.prize_cards()
    remaining_prizes.sort()
    print(remaining_prizes)
    print("final cards " + str(len(remaining_prizes)))
    return len(remaining_prizes) + 1


def solution2():
    sum = 0
    for i in range(1, 219):
        print(i)
        sum += get_card_count(Card(i))
    print(sum)

def test():
   list = [1, 2, 3, 4]
   list.pop(0)
   print(list)


solution2()
