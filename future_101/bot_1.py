#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        Using functions with assignment robot. Staying with what we have
        covered in class. although not a very practical, it servers as
        a good example to introduce class.
        Using the operator module: https://docs.python.org/2/library/operator.html
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""
import operator

print()
print("Hi, I am Marvin, your personal utilitarian bot. What would you like to do?")
command = input("press [a]dd, [s]ubtract, [m]ultiply, [t]ip calculator or [d]ivide ")


def main():
    asmd_list = ['a', 's', 'm', 'd']
    if command == 't':
        return tip_calc()
    if command in asmd_list:
        return asmd(command)
    else:
        print()
        print(command, 'is not a choice')


def asmd(argument):
    oper = argument
    print()
    if oper == 'a':
        print("lets add some numbers")
    elif oper == 's':
        print("lets subtract some numbers")
    elif oper == 'm':
        print("lets multiply some numbers")
    elif oper == 'd':
        print("lets divide some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    if oper == 'a':
        result = operator.add(number1, number2)
        output = str(result)
        print(input1 + " + " + input2 + " = " + output)
    elif oper == 's':
        result = operator.sub(number1, number2)
        output = str(result)
        print(input1 + " - " + input2 + " = " + output)
    elif oper == 'm':
        result = operator.mul(number1, number2)
        output = str(result)
        print(input1 + " * " + input2 + " = " + output)
    elif oper == 'd':
        result = operator.truediv(number1, number2)
        output = str(result)
        print(input1 + " / " + input2 + " = " + output)


def tip_calc():
    print("\nLets leave a tip?")
    input1 = input("Bill total £: ")
    input2 = input("Enter tip in %: ")
    number1 = float(input1)
    number2 = float(input2)/100
    result = number1 * number2
    output = round(result, 2)
    print('\nLeave £' + str(output) + ' for a ' + str(input2) +
          '% tip, from a bill totaling £' + str(number1))


main()


print('\n Thank you \n ~bye')
