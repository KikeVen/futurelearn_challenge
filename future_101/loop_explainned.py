#!/usr/bin/env python
# -*- coding: utf-8 -*-

# create an empty list, `shopping`, to hold the final list
shopping = []

# Assign an input request to the how_many variable
how_many = input("how many items of shopping do you have? ")
# change the input type to an interger by using the int() function
# re-assign it to the same `how_many` variable
how_many = int(how_many)

# Using a for loop, iterate `how_many` times, and execute
# the code with-in the loops scope 0 to `how_many` times
for item_number in range(how_many):
    # assign input to the `item` variable
    item = input("what is item number " + str(item_number) + "? ")
    # Append the `shopping` list with the `item`
    shopping.append(item)

# print the contents of the `shopping` list
print(shopping)
