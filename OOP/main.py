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
kitchen.set_description('a dank and dirty room buzzing with flies.')

dining_hall = Room('Dinning Room')
dining_hall.set_description('a large room with ornate golden decoration on each wall')

ballroom = Room('Ballroom')
ballroom.set_description('a large room where people dance')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

current_room = kitchen

while True:
    print("\n")
    print(current_room.get_details()[0])
    print(current_room.get_details()[1])
    command = input("> ")
    current_room = current_room.move(command)
