

class Hand:
    def __init__(self, cards, bid):
        self.bid = int(bid)
        self.cards = cards
        self.og_cards = cards
        self.dict_cards = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10}
        self.dict_cards_rev = {14: "A", 13: "K", 12: "Q", 0: "J", 10: "T"}
       # self.strength = self.getStrength()

    def getVal(self, chr):
        return int(chr) if int(chr.isdigit()) else self.dict_cards[chr]

    def getCardVal(self, index):
        return self.getVal(self.og_cards[index])

    def getMode(self, str):
        processed_cards = []
        for l in list(str):
            if l.isdigit():
                processed_cards.append(int(l))
            else:
                processed_cards.append(self.dict_cards[l])
        # Make sure if each number is distinct, take the maximum.
        processed_cards.sort(reverse=True)
        md = max(set(processed_cards), key=processed_cards.count)
        if md < 10 and md != 0:
            return md
        else:
            return self.dict_cards_rev[md]
        #return md if md < 10 else self.dict_cards_rev[md]

    def getStrength(self):
        mode = self.getMode(self.cards)
        # PART TWO CODE # Make sure to check for edge cases
        if self.cards == 'JJJJJ':
            return 7
        if mode == 'J':
            thing = self.cards
            thing = thing.replace("J", "")
            mode = self.getMode(thing)
        print(mode)
        mode = str(mode)
        print(self.cards)
        self.cards = self.cards.replace('J', str(mode))
        print(self.cards)
        # # # # # # # # #

        # Only use this line for Part 1 #
        # mode = max(self.cards, key = self.cards.count)
        # # # # # # # # # # # # # # # # #
        
        butt = []
        for l in list(self.cards):
            if l == mode:
                butt.append(l)
        frequency = len(butt)
        match frequency:
            case 1:
                return 1
            case 5:
                return 7
            case 4:
                return 6
            case 2:
                temp = self.cards.replace(mode, "")
                temp = temp.replace(max(temp, key = temp.count), "")
                return 2 if len(temp) == 2 else 3
            case 3:
                temp = self.cards.replace(mode, "")
                return 5 if (temp[0] == temp[1]) else 4
            
def sortSecond(val):
    return val[1]  

# This can be made into a function; this is some goofy ahh logic
def sortSecondaryStrength(val):
    return 100000000 * val[0].getCardVal(0) + 1000000 * val[0].getCardVal(1) + 10000 * val[0].getCardVal(2) + 100 * val[0].getCardVal(3) + 1 * val[0].getCardVal(4)

def solution():
    total_winnings = 0
    final_hands = []
    path = "python_aoc/src/day7/cards.txt"
    file = open(path, "r")
    lines = file.readlines()
    hands = []
    for l in lines:
        h = Hand(l.split()[0], l.split()[1])
        hands.append((h, h.getStrength()))
    hands.sort(key=sortSecond)
    split_hands = [[],[],[],[],[],[],[]]
    for h in hands:
        split_hands[h[1] - 1].append(h)
    for s in split_hands:
        s.sort(key=sortSecondaryStrength)
        final_hands += s
    for i, f in enumerate(final_hands):
        print(str(f[0].og_cards) +  " " + str(f[1]))
        total_winnings += f[0].bid * (i + 1)
    print(total_winnings)

solution()
