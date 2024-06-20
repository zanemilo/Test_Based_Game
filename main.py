import sys

# Zane Deso

# Dictionary of rooms
rooms = {
        'Start Room': {'South': 'Chamber of Echoing Whispers'},
        'Chamber of Echoing Whispers': {'North': 'Start Room', 'South': 'Sanctum of Forgotten Ancestors', 'East': 'Crypt of Eternal Shadows'},
        'Sanctum of Forgotten Ancestors': {'North': 'Chamber of Echoing Whispers'},
        'Crypt of Eternal Shadows': {'West': 'Chamber of Echoing Whispers', 'East' : 'Hall of Resounding Silence'},
        'Hall of Resounding Silence': {'West': 'Crypt of Eternal Shadows', 'South': 'Chamber of Timeless Enigmas' },
        'Chamber of Timeless Enigmas': {'North': 'Hall of Resounding Silence', 'South' : 'Oracles Veiled Sanctuary'},
        'Oracles Veiled Sanctuary': {'North': 'Chamber of Timeless Enigmas', 'South' : 'Vault of Reverberating Echoes'},
        'Vault of Reverberating Echoes': {'North': 'Oracles Veiled Sanctuary'},
    }

# Dictionary of items and corresponding rooms
items_in_room = {
            'Chamber of Echoing Whispers' : 'Sword',
            'Sanctum of Forgotten Ancestors' : 'Scroll',
            'Crypt of Eternal Shadows' : 'Chalice',
            'Hall of Resounding Silence' : 'Amulet',
            'Chamber of Timeless Enigmas' : 'Golden Egg',
            'Oracles Veiled Sanctuary' : 'Crown',
            'Vault of Reverberating Echoes' : 'Wraith',
}

# Dictionary of descriptions for each room
room_description = {
    "Chamber of Echoing Whispers": "In this chamber, whispers from beyond the veil intertwine, carrying secrets both sacred and sinister.",
    "Sanctum of Forgotten Ancestors": "Amidst the flickering candlelight, ancient portraits of ancestors watch with unblinking eyes, their stories etched in the dusty air.",
    "Crypt of Eternal Shadows": "The air grows thick as you descend into the crypt, where spectral figures seem to stir, imprisoned by their own lingering regrets.",
    "Hall of Resounding Silence": "Footsteps echo in eerie solitude along the vast hall, where the silence is almost suffocating in its weight.",
    "Chamber of Timeless Enigmas": "Curious arcane symbols line the walls, each holding a puzzle that defies the bounds of time and reason.",
    "Oracles Veiled Sanctuary": "Behind the heavy curtains lies the oracle's chamber, where a mist-shrouded statue peers into the future with eyes that have seen too much.",
    "Vault of Reverberating Echoes": "Within the vault, your whispers become a chorus of echoes that seem to awaken dormant spirits, yearning to break free."
}

inventory = []

# stores one of the nested dictionary from rooms as the current room info
current_room_info = {'Start Room': {'South': 'Chamber of Echoing Whispers'} }

# initialize current room manually once
for room in current_room_info:
    current_room = current_room_info




def update_current_room():
    """This function is called to update the current room according to key of current_room_info"""

    global current_room
    last_room = current_room
    for room in current_room_info:
        current_room = current_room_info
    #print(f'update_current_room from {last_room} to {current_room} \nusing key of current_room_info : {current_room_info} .\n' )


def move_room(room_choice):
    """Function for changing value of current_room_info to new room choice"""

    global current_room_info
    last_room_info = current_room_info
    for room in rooms:
        if room == room_choice: # make a new dictionary where room is {'Room' : {'Direction' : 'Next Room'} }
            new_room_info = {str(room_choice) : rooms[room] }
            current_room_info = new_room_info 
    #print(f'move_room from current_room_info : {last_room_info} \nusing room_choice: {room_choice} to {current_room_info}.\n' )
    # Call update room function
    update_current_room()


def corresponding_room_choice_with_direction(direction_choice):
    """Takes direction choice and finds the corresponding room and then returns it"""

    corresponding_room = None
    for room in current_room_info:
        corresponding_room_info = current_room_info[room] # copy dicitonary value of room from current room info
        print(corresponding_room_info)
        for key in corresponding_room_info: # finds each key and checks if it is equal to direction choice
            if key == direction_choice:
                corresponding_room = corresponding_room_info[key] # set corresponding room to the value of the next room dependent on direction choice = to current room infos available pathways
            else:
                print(direction_choice, 'not in', key)
    #print('corresponding_room_choice_with_direction returns:', corresponding_room, '\n')
    return corresponding_room  


def print_available_directions():
    """Prints each direction in current_room dictionary"""

    counter = 1
    for room, direction in current_room.items():
        print(f'Current Room: {room}')
        for direction in current_room[room]:
            print(f'Pathway {counter}: {direction}')
            counter += 1
    print()


def validate_direction(direction_choice):
    """Checks if direction choice is in the current_room choices and returns either True or False"""

    for room in current_room:
        if direction_choice in current_room[room]:
            # print('Valid direction chosen\n')
            return True
        elif direction_choice == 'Exit': # ensures if exit is entered that the invalid choice notification will not display
            break
        else:
            print('Invalid direction chosen\nPlease enter a valid direction such as ("North, East, South or West") from the list of available directions\n')
            input(f'The invalid choice was: {direction_choice}\nPress enter to continue')
            return False 


def add_item_to_inventory(room):
    """Handles adding item into player inventory and removing item from the items_in_roomd dict so it cannot be picked up multiple times"""
    
    item = return_item_in_room()
    inventory.append(item) # add item to inventory
    del items_in_room[room] # delete room and item from items_in_room dict


def display_inventory():
    """Displays contents of inventory if any"""

    if inventory != []:
        count = 1
        for item in inventory:
            print(f'{count}. {item}')
            count += 1
        input('Press enter to continue\n')
    else:
        input('As you open your stachel you find that it is empty, ready to fill with artifacts if you find any.\nPress enter to continue\n')


def return_room_name():
    for room_name in current_room: # name = list version of keys in current_room but only the first one effectively just assigning current_room_name with ONLY the name of the room
        current_room_name = list(current_room.keys())[0]
        return current_room_name


def return_item_in_room():
    """Returns Item in current room or None if there is none"""

    current_room_name = return_room_name()

    for room in current_room: # find room in item_in_room dict and return the corresponding item to room name
        if current_room_name in items_in_room:
            return items_in_room[current_room_name]
        else:
            return None


def return_room_description():
    """Returns current_room_name description from the room_description dict"""

    current_room_name = return_room_name()

    for room in room_description: # find current_room_name in room_description dict and returns description
        if room == current_room_name:
            return str(room_description[current_room_name])
        else:
            pass


def search_room():
    """Returns room description followed by adding the rooms item to the players inventory"""

    clear_display()
    current_room_name = return_room_name()
    # print(f'return_room_name : {current_room_name}')
    item = return_item_in_room()
    # print(f'return_item_in_room : {item}')
    desc = return_room_description()
    # print(f'return_room_description : {desc}')

    if item is not None:
        input(f'{desc}\nPress enter to continue')
        add_item_to_inventory(current_room_name)
        input(f'You recover an artifact! Added {item} to your inventory!\nPress enter to continue')
    elif item is None:
        input(f'{desc}\nPress enter to continue')
        input(f'As you scrutinize your surrondings you are unable to find any artifacts in the {current_room_name}\nPress enter to continue')


def start_move_room():
    """Starts process of moving rooms"""

    clear_display()
    # set current room name
    current_room_name = return_room_name()

    # Print each direction in current_room dictionary
    print_available_directions()
    
    # get user input to select direction to proceed towards
    direction_choice = input('Please choose a direction \n').title()

    if validate_direction(direction_choice): # if this function returns true

        # set correspond. function to room_choice for readability
        room_choice = corresponding_room_choice_with_direction(direction_choice)
        print(f'Room Choice: ', room_choice)

        # Call move room function with room_choice as arguement
        move_room(room_choice)


def action_menu():
    """Main action menu to choose whether to search the room(to get the item) or move to another room"""

    # set current room name
    current_room_name = return_room_name()

    print(f'Current Room: {current_room_name}\n')

    if current_room != {'Start Room': {'South': 'Chamber of Echoing Whispers'} }:
        print(f'1. Leave Room\n2. Search Room\n3. Inventory')
        choice = input('What would you like to do?').title()
        if choice in ('1' , 'Leave' , 'Leave Room'):
            start_move_room()
        elif choice in ('2', 'Search', 'Search Room'):
            search_room()
        elif choice in ('3', 'Inventory', 'I'):
            display_inventory()
        else:
            input(f'Invalid input: {choice}\nPlease enter a valid input and try again.\nPress enter to continue')
    else:
        start_move_room()


def check_win():
    """Checks if win or game over conditions are met"""

    if current_room == wraith_room: # Game over condition
        sys.exit("In the depths of the ancient temple, a wraith emerges from the shadows, its form a chilling symphony of ethereal mist and malevolent hunger.\nIts hollow eyes fixate on the intruder, a silent promise of torment before the inevitable plunge into icy oblivion.\nGAME OVER.")
    elif len(inventory) == 6: # Win condition
           sys.exit("With the artifacts reunited, the temple's shadows retreat, revealing a truth older than time itself.\nAs the final piece falls into place, a shiver of understanding crawls up your spine — victory, hard-earned and\nhaunting, now rests in your trembling hands.")
    else:
        pass


def clear_display(num=50):
    """Prints nothing 50 times by default to clear the display"""

    while num > 0:
        print()
        num -= 1


wraith_room = {'Vault of Reverberating Echoes': {'North': 'Oracles Veiled Sanctuary'}}

game_active = True

while game_active:

    clear_display()
    check_win()
    action_menu()
