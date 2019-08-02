#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        Calling class methods
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""

from shapes import Triangle, Rectangle, Oval, Paper

rect1 = Rectangle()
rect2 = Rectangle()

# We will use some special methods called setters
# to set the attributes of the object.
rect1.set_width(50)
rect1.set_height(150)
rect1.set_color("yellow")

rect2.set_x(100)
rect2.set_y(100)
rect2.set_width(200)
rect2.set_height(100)
rect2.set_color("blue")

# let’s call another method to draw the Rectangle
# object we have created
rect2.draw()
rect1.draw()

Paper.display()
