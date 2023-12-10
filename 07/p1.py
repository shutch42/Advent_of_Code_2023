from enum import Enum

card_point_map = {'T': 10,
                  'J': 11,
                  'Q': 12,
                  'K': 13,
                  'A': 14}


class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __lt__(self, other):
        return self.value < other.value


class Hand:
    def __init__(self, line):
        self.card_letters = [card for card in line.split()[0]]
        self.bid = int(line.split()[1])

        self.cards = []
        for card in self.card_letters:
            if card in card_point_map:
                self.cards.append(card_point_map[card])
            else:
                self.cards.append(int(card))

        def five_kind():
            return self.cards.count(self.cards[0]) == 5

        def four_kind():
            return self.cards.count(self.cards[0]) == 4 or self.cards.count(self.cards[1]) == 4

        def three_kind():
            for card in self.cards:
                if self.cards.count(card) == 3:
                    return True
            return False

        def pair():
            for card in self.cards:
                if self.cards.count(card) == 2:
                    return True
            return False

        def full_house():
            return three_kind() and pair()

        def two_pair():
            pairs = []
            for card in self.cards:
                if self.cards.count(card) == 2:
                    pairs.append(card)

            return len(pairs) > 2

        if five_kind():
            self.type = Type.FIVE_OF_A_KIND
        elif four_kind():
            self.type = Type.FOUR_OF_A_KIND
        elif full_house():
            self.type = Type.FULL_HOUSE
        elif three_kind():
            self.type = Type.THREE_OF_A_KIND
        elif two_pair():
            self.type = Type.TWO_PAIR
        elif pair():
            self.type = Type.ONE_PAIR
        else:
            self.type = Type.HIGH_CARD

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        else:
            for i in range(5):
                if self.cards[i] < other.cards[i]:
                    return True
                elif self.cards[i] > other.cards[i]:
                    return False

            # This line should never be reached
            return False

    def __str__(self):
        string = ""
        for card in self.card_letters:
            string += card

        return string


with open("input.txt") as file:
    hands = []
    for line in file:
        hands.append(Hand(line.strip()))

    hands.sort()

    total = 0
    for i, hand in enumerate(hands, start=1):
        total += i*hand.bid

    print(total)
