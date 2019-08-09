#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        class Room() for game design
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print(self.name + "linked rooms:" + repr(self.linked_rooms))

    def get_details(self):
        for direction in self.linked_rooms:
            here = self.name
            here_description = self.get_description()
            room = self.linked_rooms[direction]
            location = "You are currently in the " + here + " the " + room.get_name() + " is " + direction
            description = "The " + here + " is " + here_description
            return location, description

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

