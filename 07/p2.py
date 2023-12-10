from enum import Enum
from copy import deepcopy

card_point_map = {'T': 10,
                  'J': 0,
                  'Q': 11,
                  'K': 12,
                  'A': 13}


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
        # print(self.cards)

        joker_count = self.cards.count(0)
        non_jokers = deepcopy(self.cards)
        while non_jokers.count(0) > 0:
            non_jokers.remove(0)
        # print(joker_count)
        # print(non_jokers)

        def five_kind():
            if len(non_jokers) > 0:
                return (non_jokers.count(non_jokers[0]) + joker_count) == 5
            else:
                return True

        def four_kind():
            if len(non_jokers) > 1:
                return ((non_jokers.count(non_jokers[0]) + joker_count) == 4 or
                        (non_jokers.count(non_jokers[1]) + joker_count) == 4)
            else:
                return True

        def three_kind():
            if len(non_jokers) > 2:
                for card in non_jokers:
                    if (non_jokers.count(card) + joker_count) == 3:
                        return True
                return False
            else:
                return True

        def pair():
            if len(non_jokers) > 3:
                for card in non_jokers:
                    if (non_jokers.count(card) + joker_count) == 2:
                        return True
                return False
            else:
                return True

        def full_house():
            # if there is more than 1 joker, priority goes to 4 of a kind
            # w/ 1 joker, must have 2 pairs
            if joker_count == 1:
                # search for 2 pair
                for card in non_jokers:
                    if non_jokers.count(card) != 2:
                        return False
                return True
            elif joker_count == 0:
                # search for full house normally
                for i, card1 in enumerate(self.cards):
                    if self.cards.count(card1) == 3:
                        for card2 in self.cards:
                            if self.cards.count(card2) == 2:
                                return True
                        return False
                return False
            else:
                return False

        def two_pair():
            # two pair will never be picked w/ jokers
            if joker_count == 0:
                pairs = []
                for card in self.cards:
                    if self.cards.count(card) == 2:
                        pairs.append(card)
                return len(pairs) > 2
            else:
                return False

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

        return f"{self.type}: {string}"


with open("input.txt") as file:
    hands = []
    for line in file:
        hands.append(Hand(line.strip()))

    hands.sort()

    total = 0
    for i, hand in enumerate(hands, start=1):
        total += i*hand.bid

    print(total)
