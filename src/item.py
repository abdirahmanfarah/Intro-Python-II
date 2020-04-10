# Item class
from room import Room


class Item:
    def __init__(self, name, description):
        self.description = description
        self.name = name

    def __repr__(self):
        return {'Name': self.name, 'Description': self.description}

    def __str__(self):
        return 'Name: '+self.name+', description: '+self.description
