#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        Since all this bot can do, is add and subtract I think we should
        simplify things for the user by asking which of the two functions
        they would like to use
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""

print("Hi, I am Marvin, your personal calculator bot.")
command = input("press [a]dd, [s]ubtract, [m]ultiply, [t]ip or [d]ivide ")

if command == 'a':
    print("lets add some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 + number2
    output = str(result)
    print(input1 + " + " + input2 + " = " + output)
elif command == 's':
    print("lets subtract some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number1 = int(input1)
    number2 = int(input2)
    result = number1 - number2
    output = str(result)
    print(input1 + " - " + input2 + " = " + output)
elif command == 'm':
    print("lets multiply some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 * number2
    output = str(result)
    print(input1 + " * " + input2 + " = " + output)
elif command == 'd':
    print("lets divide some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 / number2
    output = str(result)
    print(input1 + " / " + input2 + " = " + output)
elif command == 't':
    print("\nLets leave a tip?")
    input1 = input("Bill total £: ")
    input2 = input("Enter tip in %: ")
    number1 = float(input1)
    number2 = float(input2)/100
    result = number1 * number2
    output = round(result, 2)
    print('\nLeave £' + str(output) + ' for a ' + str(input2) +
          '% tip, from a bill totaling £' + str(number1))
else:
    print('I didn\'t understand your choice')

print('\n Thank you \n ~bye')
