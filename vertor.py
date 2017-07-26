#!/usr/bin/python
from math import hypot


class Vertor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vertor({},{})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __str__(self):
        return 'vertor({},{})'.format(self.x, self.y)

    def __add__(self, o):
        return Vertor(self.x + o.x, self.y + o.y)

    def __mul__(self, n):
        return Vertor(self.x * n, self.y * n)


v1 = Vertor(1, 2)
v2 = Vertor(2, 1)

print(v1 + v2)
print(v1 * 2)

print('{}'.format(v1))
print('{}'.format(1))
