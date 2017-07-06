"""Solution for https://www.codewars.com/kata/ranking-poker-hands/train/python."""

from operator import itemgetter
from collections import defaultdict

RESULT = ["Loss", "Tie", "Win"]

SUITS = {
    'S': ('Spades', 1),
    'H': ('Hearts', 1),
    'D': ('Diamonds', 1),
    'C': ('Clubs', 1)
}

RANKS = {
    'A': ('Ace', 14),
    '2': ('Two', 2),
    '3': ('Three', 3),
    '4': ('Four', 4),
    '5': ('Five', 5),
    '6': ('Six', 6),
    '7': ('Seven', 7),
    '8': ('Eight', 8),
    '9': ('Nine', 9),
    'T': ('Ten', 10),
    'J': ('Jack', 11),
    'Q': ('Queen', 12),
    'K': ('King', 13)
}

MADE_HANDS = {
    'straight flush': 9,
    '4 of a kind': 8,
    'full house': 7,
    'flush': 6,
    'straight': 5,
    'set': 4,
    'two pair': 3,
    'one pair': 2,
    'high card': 1
}

class PokerHand(object):
    """Create an object representing a Poker Hand based on an input of a 5 char
    string which represents the best 5 card combination from the player's hand
    and board cards.

    Attributes:
        high_card: a list of high cards in play in sorted order, highest card first
        In play means that if a hand contins a pair of Aces, the Ace is no longer
        in play for the high card.

        vals: a list of card's values

        suits: a list of card's suits

        hand: a sorted list of tuples representing face value and card value ordered
        by highest card in descending order

        hand_value: the sum of all made hands

    Methods:
        compare_with(self, villain): takes in Hero's Hand (self) and Villain's
        Hand (villain) and compares both hands according to rules of Texas Hold'em.
        Returns one of 3 strings (Win, Loss, Tie) based on wether Hero's hand
        is better than villain's hand.
    Helper Methods:
        _is_straight(self): returns True if hand is a straight
        _is_flush(self): returns True if hand is a flush
        _has_set(self): returns True if hand contains a set
        _has_two_pair(self): returns True if hand is a 2 pair hand
        _has_pair(self): returns True if hand is a one pair hand
        """

    def __init__(self, hand):
        """Initialize a poker hand based on a 10 character string input representing
        5 cards.
        """
        hand = hand.replace(' ', '')
        # self.high_card =
        self.vals = [c for c in hand if c in RANKS.keys()]
        self.suits = [c for c in hand if c in SUITS.keys()]
        self.hand = sorted([(c, RANKS[c][1]) for c in self.vals], key=itemgetter(1), reverse=True)
        self.val_cnt = defaultdict(int)


    def compare_with(self, other):
        """Return one of 3 outcomes from result const."""
        pass

    def _is_straight(self):
        """Return True if hand is a straight."""
        previous_card = sorted(self.hand, key=itemgetter(1))[0][1] - 1
        for card in sorted(self.hand, key=itemgetter(1)):
            if previous_card + 1 != card[1]: return False
            previous_card = card[1]
        return True

    def _is_flush(self):
        """Return True if hand is a flush."""
        return True if len(set(self.suits)) == 1 else False

    def get_card_values(self):
        """Fill dict val_cnt with card combinations to determine 4 of a kinds,
        full houses, sets, 2pairs and pairs."""
        for card in self.vals:
            self.val_cnt[card] += 1

    def get_made_hand_value(self):
        """Set a value for overall hand value of all summed up individual made
        hands."""
        pass

    def _has_2pair(self):
        """Return value for 2pair if hand has made hand value of 2pair, else return 0."""
        if not self.val_cnt: self.get_card_values()
        if sorted(self.val_cnt.items(), key=lambda x: x[1], reverse=True).pop(0)[1] == 2:
            if sorted(self.val_cnt.items(), key=lambda x: x[1], reverse=True).pop(0)[1] == 2:
                return 3
        return 0