#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        Enter description
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
    
1. Take a sequence of integers and a value that is being searched for.
2. Iterate over the length of the list, using position to keep track of the item in the list being looked at.
3. If the item at the position in the sequence is equal to the value being searched for, return the position.
4. If the entire sequence has been iterated over, and the value has not been found, then return False.
"""
# from random import randint, random
import random

sequence = []
for x in range(0, 101):
    sequence.append(x)
random.shuffle(sequence)

find_me = 50

print()
if find_me not in sequence:
    print('You are out of range, you need to input a number between 0 and 100')
else:
    for position in range(len(sequence)):
        if find_me == sequence[position]:
            print(sequence[position], 'was found at index', str(position))
        else:
            pass

