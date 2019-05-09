#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Now you have two parts of a program which will create a shopping
list and display it. Your challenge is to combine them together
to create a program which will:

* Ask how many items of shopping are needed.
* Collect the items and store them in a list.
* Loop through the shopping list and display them.
* Show a total at the end so the user can see how many have been added.
"""

shopping = []
count = 0

how_many = input("how many items of shopping do you have ? ")
how_many = int(how_many)


for item_number in range(how_many):
    enumerator = item_number + 1
    item = input("what is item number " + str(enumerator) + " ? ")
    shopping.append(item)

print('-' * 45)
print('# --------- Your shopping list --------- #')
print()
for item in shopping:
    print(item)
    count += 1
print()
print('You have', count, 'items in your shopping list')
