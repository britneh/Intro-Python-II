from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item("torch", "firey object")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("torch", "firey object")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("torch", "firey object")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("torch", "firey object")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("torch", "firey object")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
while True:
# * Prints the current room name
    print(player.location)
    print(player.location.print_items())
# * Prints the current description (the textwrap module might be useful here).done in room
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    command = input("> ").split(',')
    if command[0] == 'bp':
        breakpoint()

    if command[0] == 'q':
        break
    elif command[0] == 'n':
        if hasattr(player.location, 'n_to') == False:
            print('Cannot move north. Try again. \n')
        else:
            player.location = player.location.n_to
    elif command[0] == 's':       
        if hasattr(player.location, 's_to') == False:
            print('Cannot move south. Try again. \n')
        else:
            player.location = player.location.s_to
    elif command[0] == 'e':       
        if hasattr(player.location, 'e_to') == False:
            print('Cannot move east. Try again. \n')
        else:
            player.location = player.location.s_to
    elif command[0] == 'w':       
        if hasattr(player.location, 'w_to') == False:
            print('Cannot move south. Try again. \n')
        else:
            player.location = player.location.w_to
        
