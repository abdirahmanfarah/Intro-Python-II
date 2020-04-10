from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['torch']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# room['foyer'].item = ['torch']

torch = Item('Torch', "A torch")
candle = Item('Candle', "A candle")
bag = Item('Bag', 'A bag')
brush = Item('Brush', 'A brush')
boots = Item('Boots', 'Boots')

print(torch)

room['outside'].add_item(torch)
room['foyer'].add_item(candle)
room['foyer'].add_item(bag)
room['narrow'].add_item(boots)
room['treasure'].add_item(brush)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Ted", room['outside'])
print('Welcome player, ready for adventure? ')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#


i = 1
while i:
    print(player_1.current_room.name)
    print(player_1.current_room.description)
    print(player_1.current_room.get_items())
    value = input(
        "[n] for North, [s] for South, [w] for West, [e] for East, [q] to Quit \n ")

    # If the user enters "q", quit the game.
    if value.lower() == 'q':
        break

     # If the user enters a cardinal direction, attempt to move to the room there.
    elif player_1.current_room == room['outside']:
        if value.lower() == 'n':
            player_1.room(room['foyer'])
        elif value != 'n':
            print("Sorry, wrong key pressed")

    elif player_1.current_room == room['foyer']:
        if value.lower() == 's':
            player_1.room(room['outside'])
        elif value.lower() == 'n':
            player_1.room(room['overlook'])
        elif value.lower() == 'e':
            player_1.room(room['narrow'])
        else:
            print('Sorry, wrong key pressed')

    elif player_1.current_room == room['overlook']:
        if value.lower() == 's':
            player_1.room(room['foyer'])
        elif value.lower != 's':
            print('Sorry, wrong key pressed')

    elif player_1.current_room == room['narrow']:
        if value.lower() == 'w':
            player_1.room(room['foyer'])
        elif value.lower() == 'n':
            player_1.room(room['treasure'])
        else:
            print('Sorry, wrong key pressed')

    elif player_1.current_room == room['treasure']:
        if value.lower() == 's':
            player_1.room(['narrow'])
        elif value.lower() != 's':
            # Print an error message if the movement isn't allowed.
            print('Sorry, wrong key pressed')
