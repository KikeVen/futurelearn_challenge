#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        call the class Room() module
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""
from room import Room

kitchen = Room('Kitchen')
kitchen.set_description('A dank and dirty room buzzing with flies.')

dining_hall = Room('Dinning Room')
dining_hall.set_description('A large room with ornate golden decoration on each wall')

ballroom = Room('Ballroom')
ballroom.set_description('A large room where people dance')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(ballroom, 'west')

dining_hall.get_details()

# kitchen.describe()