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

dinning_hall = Room('Dinning Room')
dinning_hall.set_description('A large room with ornate golden decoration on each wall')

ballroom = Room('Ballroom')
ballroom.set_description('A large room where people dance')

kitchen.link_room(dinning_hall, 'south')
dinning_hall.link_room(ballroom, 'west')

# kitchen.describe()