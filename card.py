#!/usr/bin/python3

import collections
import socket


Card = collections.namedtuple('card', ['rand', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rand, suit) for suit in self.suits
                       for rand in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        """实现__getitem__之后这个类变得可迭代了。"""
        return self._cards[position]


fd = FrenchDeck()

print(len(fd))

print(fd[1])


c = Card(rand='1', suit='hearts')
print(c)
print('hello')

print('test magit')
