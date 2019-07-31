#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        An introduction to OOP
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""

from turtle import Turtle
from random import randint

bernie = Turtle()
bernie.color('red')
bernie.shape('turtle')
bernie.penup()
bernie.goto(-160, 110)
bernie.pendown()

pete = Turtle()
pete.color('blue')
pete.shape('turtle')
pete.penup()
pete.goto(-160, 80)
pete.pendown()

booker = Turtle()
booker.color('yellow')
booker.shape('turtle')
booker.penup()
booker.goto(-160, 50)
booker.pendown()

harris = Turtle()
harris.color('green')
harris.shape('turtle')
harris.penup()
harris.goto(-160, 20)
harris.pendown()

for movement in range(100):
    bernie.forward(randint(1,5))
    pete.forward(randint(1,5))
    booker.forward(randint(1,5))
    harris.forward(randint(1,5))

input("Press Enter to close")