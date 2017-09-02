#!/bin/python

try:
    assert 2==2, 'hello'
    assert 2==3, 'world'
except AssertionError as e:
    print(e)