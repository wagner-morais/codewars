"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-hands/."""

import re
from collections import Counter

LOOKUP = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    }

def get_cards(hand):
    """Return a list with string representation of a given 7 card hand."""
    card_str_no_suits = ''.join([c if ord(c) < 128 else '' for c in hand])
    cards = [LOOKUP[c] if not c.isnumeric() else int(c) for c in card_str_no_suits]
    return cards

def get_suits(hand):
    """Return a list with the suits of the hand."""
    pattern = re.compile('♠|♣|♥|♦')
    return list(re.findall(pattern, hand))

def get_pokerscore(hand):
    """Return a unique value representing overall hand strength."""
    c = Counter(hand)
    a = sorted(hand, key=lambda x: (c[x], x), reverse=True)
    return a[0]<<16|a[1]<<12|a[2]<<8|a[3]<<4|a[4]

def rank_hand(hand):
    """Return a tuple with index representing hand strength and final 5 card hand."""
    pass

def calc_index(cs, ss):
    """Return the integer index representing the strenght of the hand for a given 5 card hand and suits."""
    v = 0
    for card in enumerate(cs):
        o = int(pow(2, card * 4))
        v += o*((v // o & 15) + 1)
    if v % 15 != 5:
        v %= 15
        return v - 1
    else:
        s = 1<<cs[0]|1<<cs[1]|1<<cs[2]|1<<cs[3]|1<<cs[4]
    v -= 3 if (s/(s&-s) == 31) or (s == 0x403c) else 1
    return v - -5 if ss[0] == ss[0]|ss[1]|ss[2]|ss[3]|ss[4] * s == 0x7c00 else 1

    

