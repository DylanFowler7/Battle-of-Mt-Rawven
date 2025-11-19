import sys
import random
import string
import time
import copy
from units import *

card_list = []
turn_count = 0
previous_turn_count = 0
player_1_current_mana = 1
player_2_current_mana = 1
bot_current_mana = 6
player_1_units = []
player_2_units = []
p1_first_units = copy.deepcopy(player_1_units)
p2_first_units = copy.deepcopy(player_2_units)
player_1_conquest_points = 0
player_2_conquest_points = 0
player_1_cards = []
player_2_cards = []
deck = []
discarded_cards = []
scout_number = 0
wind_walker_number = 0
tactician_number = 0
drummer_number = 0
paladin_number = 0
investor_number = 0
action_count = 2
YELLOW = "\033[1;33m"
LIGHT_WHITE = "\033[1;37m"
CYAN = "\033[0;36m"
BROWN = "\033[0;33m"
LIGHT_BLUE = "\033[1;34m"
PURPLE = "\033[0;35m"
GREEN = "\033[0;32m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_PURPLE = "\033[1;35m"
RED = "\033[0;31m"
BOLD = "\033[1m"
LIGHT_CYAN = "\033[1;36m"
NEGATIVE = "\033[7m"
is_player_1_turn = True
line_1 = "[]  []  []  []  []  []  []  []  []  []"
line_1_split = line_1.split("  ")
line_2 = "[]  []  []  []  []  []  []  []  []  []"
line_2_split = line_2.split("  ")
line_3 = "[]  []  []  []  []  []  []  []  []  []"
line_3_split = line_3.split("  ")
line_4 = "[]  []  []  []  []  []  []  []  []  []"
line_4_split = line_4.split("  ")
line_5 = "[]  []  []  []  []  []  []  []  []  []"
line_5_split = line_5.split("  ")
line_6 = "[]  []  []  []  []  []  []  []  []  []"
line_6_split = line_6.split("  ")
line_7 = "[]  []  []  []  []  []  []  []  []  []"
line_7_split = line_7.split("  ")
line_8 = "[]  []  []  []  []  []  []  []  []  []"
line_8_split = line_8.split("  ")
line_9 = "[]  []  []  []  []  []  []  []  []  []"
line_9_split = line_9.split("  ")
line_10 = "[]  []  []  []  []  []  []  []  []  []"
line_10_split = line_10.split("  ")
previous_screen = "" 

def game_loop():
    global previous_screen
    global turn_count
    global previous_turn_count
    global is_player_1_turn
    if turn_count == 0:
        create_deck()
        generate_map()
    if turn_count == .5:
        p1_place_starting_units()
    print(f"{LIGHT_WHITE}Map Guide               1   2   3   4   5   6   7   8   9   10")
    print(f"{BROWN}M - Mountain{LIGHT_WHITE}        A   {line_1}")
    print(f"{PURPLE}A - Arcane{LIGHT_WHITE}          B   {line_2}")
    print(f"{GREEN}R - Resupply{LIGHT_WHITE}        C   {line_3}")
    print(f"{NEGATIVE}C - Conquest{GREEN}{LIGHT_WHITE}        D   {line_4}")
    print(f"{LIGHT_BLUE}s - Scout{LIGHT_WHITE}           E   {line_5}")
    print(f"{CYAN}w - Wind Walker{LIGHT_WHITE}     F   {line_6}")
    print(f"{LIGHT_PURPLE}t - Tactician{LIGHT_WHITE}       G   {line_7}")
    print(f"{LIGHT_CYAN}d - Drummer{LIGHT_WHITE}         H   {line_8}")
    print(f"{YELLOW}p - Paladin{LIGHT_WHITE}         I   {line_9}")
    print(f"{LIGHT_GREEN}i - Investor{LIGHT_WHITE}        J   {line_10}")
    if turn_count == 0:
        player_1 = "player_1"
        player_2 = "player_2"
        previous_screen = "game_loop"
        draw_cards(player_1)
        draw_cards(player_1)
        draw_cards(player_1)
        draw_cards(player_2)
        draw_cards(player_2)
        draw_cards(player_2)
        choose_starting_units()
    turn_determiner = turn_count % 2
    print("Commands         (A)ctions    (G)uide    (U)nits    (Q)uit")
    print(f"Actions Remaining: {action_count}")
    if turn_count > 0 and previous_turn_count < turn_count:
        previous_turn_count = turn_count
        resource_gain()
    if turn_determiner != 0 and turn_count > 0:
        second_input = input(f"Player 1: Select a Command: ")
        is_player_1_turn = True
    if turn_determiner == 0 and turn_count > 0:
        second_input = input(f"Player 2: Select a Command: ")
        is_player_1_turn = False
    if second_input == "":
        print("Invalid Command")
        game_loop()
    if second_input.lower() == "action" or second_input.lower() == "a":
        actions()
    if second_input.lower() == "guide" or second_input.lower() == "g":
        previous_screen = "game_loop"
        guide()
    if second_input.lower() == "unit" or second_input.lower() == "u":
        unit_display()
    if second_input.lower() == "quit" or second_input.lower() == "q":
        sys.exit(0)

def generate_map():
    mountain_count = 5
    arcane_count = 5
    conquest_count = 5
    resupply_count = 5
    map_letters = string.ascii_uppercase[1:9]
    while mountain_count > 0:
        placement_number = random.randint(1, 8)
        placement_letter = random.choice(map_letters)
        placement = map_placement(placement_letter)
        placement[placement_number] = f"{BROWN}M {LIGHT_WHITE}"
        mountain_count -= 1
        map_join(placement_letter, placement)
    while arcane_count > 0:
        placement_number = random.randint(1, 8)
        placement_letter = random.choice(map_letters)
        placement = map_placement(placement_letter)
        while placement[placement_number] != "[]":
            placement_number = random.randint(1, 8)
            placement_letter = random.choice(map_letters)
            placement = map_placement(placement_letter)
        placement[placement_number] = f"{PURPLE}A {LIGHT_WHITE}"
        arcane_count -= 1
        map_join(placement_letter, placement)
    while conquest_count > 0:
        placement_number = random.randint(1, 8)
        placement_letter = random.choice(map_letters)
        placement = map_placement(placement_letter)
        while placement[placement_number] != "[]":
            placement_number = random.randint(1, 8)
            placement_letter = random.choice(map_letters)
            placement = map_placement(placement_letter)
        placement[placement_number] = f"{NEGATIVE}C {GREEN}{LIGHT_WHITE}"
        conquest_count -= 1
        map_join(placement_letter, placement)
    while resupply_count > 0:
        placement_number = random.randint(1, 8)
        placement_letter = random.choice(map_letters)
        placement = map_placement(placement_letter)
        while placement[placement_number] != "[]":
            placement_number = random.randint(1, 8)
            placement_letter = random.choice(map_letters)
            placement = map_placement(placement_letter)
        placement[placement_number] = f"{GREEN}R {LIGHT_WHITE}"
        resupply_count -= 1
        map_join(placement_letter, placement)
        
def map_placement(map_letter):
    global line_1_split
    global line_2_split
    global line_3_split
    global line_4_split
    global line_5_split
    global line_6_split
    global line_7_split
    global line_8_split
    global line_9_split
    global line_10_split
    if map_letter == "A":
        map_top = line_1_split
    if map_letter == "B":
        map_top = line_2_split
    if map_letter == "C":
        map_top = line_3_split
    if map_letter == "D":
        map_top = line_4_split
    if map_letter == "E":
        map_top = line_5_split
    if map_letter == "F":
        map_top = line_6_split
    if map_letter == "G":
        map_top = line_7_split
    if map_letter == "H":
        map_top = line_8_split
    if map_letter == "I":
        map_top = line_9_split
    if map_letter == "J":
        map_top = line_10_split
    return map_top

def map_join(placement_letter, placement):
    global line_1
    global line_2
    global line_3
    global line_4
    global line_5
    global line_6
    global line_7
    global line_8
    global line_9
    global line_10
    placement_join = "  ".join(placement)
    if placement_letter == "A":
        line_1 = placement_join
    if placement_letter == "B":
        line_2 = placement_join
    if placement_letter == "C":
        line_3 = placement_join
    if placement_letter == "D":
        line_4 = placement_join
    if placement_letter == "E":
        line_5 = placement_join
    if placement_letter == "F":
        line_6 = placement_join
    if placement_letter == "G":
        line_7 = placement_join
    if placement_letter == "H":
        line_8 = placement_join
    if placement_letter == "I":
        line_9 = placement_join
    if placement_letter == "J":
        line_10 = placement_join
        
def choose_starting_units():
    global player_1_current_mana
    global player_2_current_mana
    global player_1_units
    global player_2_units
    global turn_count
    global previous_screen
    global scout_number
    global wind_walker_number
    global tactician_number
    global drummer_number
    global paladin_number
    global investor_number
    global p1_first_units
    global p2_first_units
    is_player_2_selection = False
    print("Actions     (U)nits")
    print(f"1 Mana: {LIGHT_BLUE}(S)cout{LIGHT_WHITE} or {CYAN}(W)ind Walker{LIGHT_WHITE}")
    print(f"2 Mana: {LIGHT_PURPLE}(T)actician{LIGHT_WHITE} or {LIGHT_CYAN}(D)rummer{LIGHT_WHITE}")
    print(f"3 Mana: {YELLOW}(P)aladin{LIGHT_WHITE} or {LIGHT_GREEN}(I)nvestor{LIGHT_WHITE}")
    while is_player_2_selection == False:
        if player_1_current_mana == 0:
            is_player_2_selection = True
        if is_player_2_selection == False:
            unit_choice = input(f"Player 1: Select unit[Current Mana: {player_1_current_mana}]: ")
            if unit_choice.lower() == "":
                print("Invalid Unit")
                choose_starting_units()
            if unit_choice[0].lower() == "s": 
                player_1_current_mana -= 1
                scout_number += 1
                player_1_units.append(Scout(scout_number))
                print(f"Added {LIGHT_BLUE}Scout{LIGHT_WHITE} {scout_number}")
                choose_starting_units()
            if unit_choice[0].lower() == "w":
                player_1_current_mana -= 1
                wind_walker_number += 1
                player_1_units.append(Wind_walker(wind_walker_number))
                print(f"Added {CYAN}Wind Walker{LIGHT_WHITE} {wind_walker_number}")
                choose_starting_units()
            if unit_choice[0].lower() == "t":
                if player_1_current_mana > 1:
                    player_1_current_mana -= 2
                    tactician_number += 1
                    player_1_units.append(Tactician(tactician_number))
                    print(f"Added {LIGHT_PURPLE}Tactician{LIGHT_WHITE} {tactician_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    choose_starting_units()
            if unit_choice[0].lower() == "d":
                if player_1_current_mana > 1:
                    player_1_current_mana -= 2
                    drummer_number += 1
                    player_1_units.append(Drummer(drummer_number))
                    print(f"Added {LIGHT_CYAN}Drummer{LIGHT_WHITE} {drummer_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    choose_starting_units()
            if unit_choice[0].lower() == "p":
                if player_1_current_mana > 2:
                    player_1_current_mana -= 3
                    paladin_number += 1
                    player_1_units.append(Paladin(paladin_number))
                    print(f"Added {YELLOW}Paladin{LIGHT_WHITE} {paladin_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    choose_starting_units()
            if unit_choice[0].lower() == "i":
                if player_1_current_mana > 2:
                    player_1_current_mana -= 3
                    investor_number += 1
                    player_1_units.append(Investor(investor_number))
                    print(f"Added {LIGHT_GREEN}Investor{LIGHT_WHITE} {investor_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    choose_starting_units()
            if unit_choice.lower() == "u" or unit_choice.lower() == "units":
                previous_screen = "choose_starting_units"
                unit_guide()
            else:
                print("Invalid option. Please enter valid unit.")
                choose_starting_units()
    while is_player_2_selection == True:
        if player_2_current_mana == 0:
            is_player_2_selection = False
            turn_count = .5
            p1_first_units = copy.deepcopy(player_1_units)
            p2_first_units = copy.deepcopy(player_2_units)
            game_loop()
        if is_player_2_selection == True:
            unit_choice = input(f"Player 2: Select unit[Current Mana: {player_2_current_mana}]: ")
            if unit_choice.lower() == "":
                print("Invalid Unit")
            if unit_choice[0].lower() == "s":
                player_2_current_mana -= 1
                scout_number += 1
                player_2_units.append(Scout(scout_number))
                print(f"Added {LIGHT_BLUE}Scout{LIGHT_WHITE} {scout_number}")
                choose_starting_units()
            if unit_choice[0].lower() == "w":
                player_2_current_mana -= 1
                wind_walker_number += 1
                player_2_units.append(Wind_walker(wind_walker_number))
                print(f"Added {CYAN}Wind Walker{LIGHT_WHITE} {wind_walker_number}")
                choose_starting_units()
            if unit_choice[0].lower() == "t":        
                if player_2_current_mana > 1:
                    player_2_current_mana -= 2
                    tactician_number += 1
                    player_2_units.append(Tactician(tactician_number))
                    print(f"Added {LIGHT_PURPLE}Tactician{LIGHT_WHITE} {tactician_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    choose_starting_units()
            if unit_choice[0].lower() == "d":
                if player_2_current_mana > 1:
                    player_2_current_mana -= 2
                    drummer_number += 1
                    player_2_units.append(Drummer(drummer_number))
                    print(f"Added {LIGHT_CYAN}Drummer{LIGHT_WHITE} {drummer_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    choose_starting_units()
            if unit_choice[0].lower() == "p":
                if player_2_current_mana > 2:
                    player_2_current_mana -= 3
                    paladin_number += 1
                    player_2_units.append(Paladin(paladin_number))
                    print(f"Added {YELLOW}Paladin{LIGHT_WHITE} {paladin_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    choose_starting_units()
            if unit_choice[0].lower() == "i":
                if player_2_current_mana > 2:
                    player_2_current_mana -= 3
                    investor_number += 1
                    player_2_units.append(Investor(investor_number))
                    print(f"Added {LIGHT_GREEN}Investor{LIGHT_WHITE} {investor_number}")
                    choose_starting_units()
                else:
                    print("Not enough mana.")
                    unit_choice = input(f"Player 1: Select unit[Current Mana: {player_1_current_mana}]: ")
            if unit_choice.lower() == "u" or unit_choice.lower() == "units":
                previous_screen = "choose_starting_units"
                unit_guide()
            else:
                print("Invalid option. Please enter valid unit.")
                choose_starting_units()
                
def p1_place_starting_units():
    global turn_count
    global previous_screen
    global player_1_units
    global p1_first_units
    if len(p1_first_units) == 0:
        p2_place_starting_units()
    while turn_count == .5:
        letters = ["B", "C", "D", "E", "F", "G", "H", "I"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9]
        not_allowed = []
        for letter in letters:
            for number in numbers:
                space = letter + str(number)
                not_allowed.append(space)
        allowed = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10"]
        print("Actions         (G)uide")
        print(f"{LIGHT_WHITE}Map Guide               1   2   3   4   5   6   7   8   9   10")
        print(f"{BROWN}M - Mountain{LIGHT_WHITE}        A   {line_1}")
        print(f"{PURPLE}A - Arcane{LIGHT_WHITE}          B   {line_2}")
        print(f"{GREEN}R - Resupply{LIGHT_WHITE}        C   {line_3}")
        print(f"{NEGATIVE}C - Conquest{GREEN}{LIGHT_WHITE}        D   {line_4}")
        print(f"{LIGHT_BLUE}s - Scout{LIGHT_WHITE}           E   {line_5}")
        print(f"{CYAN}w - Wind Walker{LIGHT_WHITE}     F   {line_6}")
        print(f"{LIGHT_PURPLE}t - Tactician{LIGHT_WHITE}       G   {line_7}")
        print(f"{LIGHT_CYAN}d - Drummer{LIGHT_WHITE}         H   {line_8}")
        print(f"{YELLOW}p - Paladin{LIGHT_WHITE}         I   {line_9}")
        print(f"{LIGHT_GREEN}i - Investor{LIGHT_WHITE}        J   {line_10}")
        count = 1
        unit_list = []
        split_unit = []
        unit_first = []
        unit_second = []
        for units in p1_first_units:
            print(f"{count}. {units.name} {units.number}")
            unit_list.append(str(count) + ". " + units.name + " " + str(units.number))
            count += 1
        place_unit = input("Choose a unit to place(If using the name be exact): ")
        if place_unit.lower() == "guide" or place_unit.lower() == "g":
            previous_screen = "p1_place_units"
            guide()
        for unit in unit_list:
            split_unit.append(unit.split(". "))
        for unit in split_unit:
            unit_first.append(unit[0])
            unit_second.append(unit[1])
        if place_unit in unit_first or place_unit in unit_second:
            space_selection = input("Select space for unit(May only place on edge spaces, input must be exact, A1 format): ")
            if space_selection in not_allowed:
                print("Space not allowed")
                p1_place_starting_units()
            if space_selection in allowed:
                space_is = []
                for letter in space_selection:
                    space_is.append(letter)
                placement_letter = space_is[0]
                if len(space_is) == 3:
                    two_digit = "".join(space_is[1:])
                else:
                    two_digit = ""
                if len(two_digit) == 2:
                    placement_number = int(two_digit) - 1
                else:
                    placement_number = int(space_is[1]) - 1
                placement = map_placement(placement_letter)
                if placement[placement_number] != "[]":
                    print("Space already occupied")
                    p1_place_starting_units()
                second_split = []
                for part in unit_second:
                    second_split = part.split(" ")
                    if place_unit in unit_second:
                        if second_split[0] == "Scout":
                            placement[int(placement_number)] = f"{LIGHT_BLUE}s{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Wind_Walker":
                            placement[int(placement_number)] = f"{CYAN}w{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Tactician":
                            placement[int(placement_number)] = f"{LIGHT_PURPLE}t{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Drummer":
                            placement[int(placement_number)] = f"{LIGHT_CYAN}d{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Paladin":
                            placement[int(placement_number)] = f"{YELLOW}p{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Investor":
                            placement[int(placement_number)] = f"{LIGHT_GREEN}w{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                resplit_unit = []
                for first in split_unit:
                    if place_unit == first[0]:
                        resplit_unit = first[1].split(" ")
                        if resplit_unit[0] == "Scout":
                            placement[int(placement_number)] = f"{LIGHT_BLUE}s{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Wind_Walker":
                            placement[int(placement_number)] = f"{CYAN}w{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Tactician":
                            placement[int(placement_number)] = f"{LIGHT_PURPLE}t{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Drummer":
                            placement[int(placement_number)] = f"{LIGHT_CYAN}d{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Paladin":
                            placement[int(placement_number)] = f"{YELLOW}p{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Investor":
                            placement[int(placement_number)] = f"{LIGHT_GREEN}w{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                map_join(placement_letter, placement)
                if place_unit in unit_first:
                    p1_first_units.pop(int(place_unit) - 1)
                if place_unit in unit_second:
                    for unit in split_unit:
                        if place_unit == unit[1]:
                            p1_first_units.pop(int(unit[0]) - 1)
            if space_selection not in allowed and space_selection not in not_allowed:
                print("Invalid space selection")
                p1_place_starting_units()
        else:
            print("Invalid unit selection")
            p1_place_starting_units()
        p2_place_starting_units()

def p2_place_starting_units():
    global turn_count
    global previous_screen
    global player_2_units
    global p1_first_units
    global p2_first_units
    if len(p1_first_units) == 0 and len(p2_first_units) == 0:
        turn_count = 1
        game_loop()
    if len(p2_first_units) == 0:
        p1_place_starting_units()
    while turn_count == .5:
        letters = ["B", "C", "D", "E", "F", "G", "H", "I"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9]
        not_allowed = []
        for letter in letters:
            for number in numbers:
                space = letter + str(number)
                not_allowed.append(space)
        allowed = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10"]
        print("Actions         (G)uide")
        print(f"{LIGHT_WHITE}Map Guide               1   2   3   4   5   6   7   8   9   10")
        print(f"{BROWN}M - Mountain{LIGHT_WHITE}        A   {line_1}")
        print(f"{PURPLE}A - Arcane{LIGHT_WHITE}          B   {line_2}")
        print(f"{GREEN}R - Resupply{LIGHT_WHITE}        C   {line_3}")
        print(f"{NEGATIVE}C - Conquest{GREEN}{LIGHT_WHITE}        D   {line_4}")
        print(f"{LIGHT_BLUE}s - Scout{LIGHT_WHITE}           E   {line_5}")
        print(f"{CYAN}w - Wind Walker{LIGHT_WHITE}     F   {line_6}")
        print(f"{LIGHT_PURPLE}t - Tactician{LIGHT_WHITE}       G   {line_7}")
        print(f"{LIGHT_CYAN}d - Drummer{LIGHT_WHITE}         H   {line_8}")
        print(f"{YELLOW}p - Paladin{LIGHT_WHITE}         I   {line_9}")
        print(f"{LIGHT_GREEN}i - Investor{LIGHT_WHITE}        J   {line_10}")
        count = 1
        unit_list = []
        split_unit = []
        unit_first = []
        unit_second = []
        for units in p2_first_units:
            print(f"{count}. {units.name} {units.number}")
            unit_list.append(str(count) + ". " + units.name + " " + str(units.number))
            count += 1
        place_unit = input("Choose a unit to place(If using the name be exact): ")
        if place_unit.lower() == "guide" or place_unit.lower() == "g":
            previous_screen = "p1_place_units"
            guide()
        for unit in unit_list:
            split_unit.append(unit.split(". "))
        for unit in split_unit:
            unit_first.append(unit[0])
            unit_second.append(unit[1])
        if place_unit in unit_first or place_unit in unit_second:
            space_selection = input("Select space for unit(May only place on edge spaces, input must be exact, A1 format): ")
            if space_selection in not_allowed:
                print("Space not allowed")
                p2_place_starting_units()
            if space_selection in allowed:
                space_is = []
                for letter in space_selection:
                    space_is.append(letter)
                placement_letter = space_is[0]
                if len(space_is) == 3:
                    two_digit = "".join(space_is[1:])
                else:
                    two_digit = ""
                if len(two_digit) == 2:
                    placement_number = int(two_digit) - 1
                else:
                    placement_number = int(space_is[1]) - 1
                placement = map_placement(placement_letter)
                if placement[placement_number] != "[]":
                    print("Space already occupied")
                    p2_place_starting_units()
                second_split = []
                for part in unit_second:
                    second_split = part.split(" ")
                    if place_unit in unit_second:
                        if second_split[0] == "Scout":
                            placement[int(placement_number)] = f"{LIGHT_BLUE}s{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Wind_Walker":
                            placement[int(placement_number)] = f"{CYAN}w{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Tactician":
                            placement[int(placement_number)] = f"{LIGHT_PURPLE}t{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Drummer":
                            placement[int(placement_number)] = f"{LIGHT_CYAN}d{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Paladin":
                            placement[int(placement_number)] = f"{YELLOW}p{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if second_split[0] == "Investor":
                            placement[int(placement_number)] = f"{LIGHT_GREEN}w{second_split[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if place_unit == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                resplit_unit = []
                for first in split_unit:
                    if place_unit == first[0]:
                        resplit_unit = first[1].split(" ")
                        if resplit_unit[0] == "Scout":
                            placement[int(placement_number)] = f"{LIGHT_BLUE}s{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Wind_Walker":
                            placement[int(placement_number)] = f"{CYAN}w{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Tactician":
                            placement[int(placement_number)] = f"{LIGHT_PURPLE}t{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Drummer":
                            placement[int(placement_number)] = f"{LIGHT_CYAN}d{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Paladin":
                            placement[int(placement_number)] = f"{YELLOW}p{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                        if resplit_unit[0] == "Investor":
                            placement[int(placement_number)] = f"{LIGHT_GREEN}w{resplit_unit[1]}{LIGHT_WHITE}"
                            for unit in player_1_units:
                                if first[1] == f"{unit.name} {unit.number}":
                                    unit.location = space_selection
                map_join(placement_letter, placement)
                if place_unit in unit_first:
                    p2_first_units.pop(int(place_unit) - 1)
                if place_unit in unit_second:
                    for unit in split_unit:
                        if place_unit == unit[1]:
                            p2_first_units.pop(int(unit[0]) - 1)
            if space_selection not in allowed and space_selection not in not_allowed:
                print("Invalid space selection")
                p2_place_starting_units()
        else:
            print("Invalid unit selection")
            p2_place_starting_units()
        p1_place_starting_units()
                
def unit_display():
    global is_player_1_turn
    if is_player_1_turn == True:
        for units in player_1_units:
            print(units.unit_display())
    else:
        for units in player_2_units:
            print(units.unit_display())
    unit_input = input("Select unit(Input must match unit name and number) or (R)eturn: ")
    if is_player_1_turn:
        for unit_list in player_1_units:
            if unit_input == (f"{unit_list.name} {unit_list.number}"):
                print(f"{unit_list.name}: Health {unit_list.health}, Attack {unit_list.attack}, Has {unit_list.ability} Ability uses left, Has moved this turn: {unit_list.has_moved_this_turn}")
                unit_display()
    if is_player_1_turn == False:
        for unit_list in player_1_units:
            if unit_input == (f"{unit_list.name} {unit_list.number}"):
                print(f"{unit_list.name}: Health {unit_list.health}, Attack {unit_list.attack}, Has {unit_list.ability} Ability uses left, Has moved this turn: {unit_list.has_moved_this_turn}")
                unit_display()
    if unit_input.lower() == "return" or unit_input.lower() == "r":
        game_loop()
    else:
        print("Invalid unit.")
        unit_display()
        

def actions():
    global previous_screen
    global player_1_current_mana
    global player_2_current_mana
    global turn_count
    global player_1_cards
    global player_2_cards
    global is_player_1_turn
    global player_1_conquest_points
    global player_2_conquest_points
    player = ""
    print("Actions      (M)ove    (C)ard    (E)xchange Conquest    (B)uy Unit   (R)eturn")
    if is_player_1_turn == True:
        print(f"Current Mana: {player_1_current_mana}")
        print(f"Current Conquest Points: {player_1_conquest_points}")
        player = "player_1"
    if is_player_1_turn == False:
        print(f"Current Mana: {player_2_current_mana}")
        print(f"Current Conquest Points: {player_1_conquest_points}")
        player = "player_2"
    turn_determiner = turn_count % 2
    if turn_determiner != 0 and turn_count > 0:
        action_selection = input(f"Player 1: Select an action: ")
    if turn_determiner == 0 and turn_count > 0:
        action_selection = input(f"Player 2: Select an action: ")
    if action_selection.lower() == "mover" or action_selection.lower() == "m":
        move(player)
    if action_selection.lower() == "buy" or action_selection.lower() == "unit" or action_selection.lower() == "buy unit" or action_selection.lower() == "b":
        if is_player_1_turn == True and player_1_current_mana == 0:
            print("Not enough mana to buy a unit")
            actions()
        if is_player_1_turn == False and player_2_current_mana == 0:
            print("Not enough mana to buy a unit")
            actions()
        else:
            previous_screen = "actions"
            create_unit()
    if action_selection.lower() == "card" or action_selection.lower() == "c":
        use_card(player)            
    if action_selection.lower() == "exchange" or action_selection.lower() == "conquest" or action_selection.lower() == "exchange conquest" or action_selection.lower() == "e":
        confirm = input("Exchange 1 Conquest Point for 3 Mana? (Y)es or (N)o: ")
        if confirm.lower() == "yes" or confirm.lower() == "y":
            if is_player_1_turn == True:
                if player_1_conquest_points < 1:
                    print("Not enough Coquest Points")
                    actions()
            if is_player_1_turn == False:
                if player_2_conquest_points < 1:
                    print("Not enough Coquest Points")
                    actions()
            exchange_conquest(player)
        if confirm.lower() == "no" or confirm.lower() == "n":
            actions()
    if action_selection.lower() == "return" or action_selection.lower() == "r":
        print("Returning")
        game_loop()
    else:
        print("Invalid input")
        actions()

def guide():
    global previous_screen
    print("{LIGHT_WHITE}Actions     (U)nits  (R)eturn")
    print("Rules")
    print(f"The game will start with a randomly generated 10x10 board with 5 {BROWN}Mountian{LIGHT_WHITE}, 5 {PURPLE}Arcane{LIGHT_WHITE},")
    print(f"5 {NEGATIVE}Conquest{GREEN}{LIGHT_WHITE}, and 5 {GREEN}Resupply{LIGHT_WHITE} tiles placed upon it. These tiles will never be touching")
    print(f"the edge of the board. {BROWN}Mountains{LIGHT_WHITE} are unable to be moved onto. {PURPLE}Arcane{LIGHT_WHITE} tiles earn you mana.")
    print(f"{NEGATIVE}Conquest{GREEN}{LIGHT_WHITE} tiles gives you points. {GREEN}Resupply{LIGHT_WHITE} earns you cards. You earn these resources")
    print("if a unit is upon one of the spaces at the start of your turn.")
    print("Each unit has a different mana value. You start with 6 mana and must purchase units before")
    print("the start of the game. You then take turns placing your units on the edge of the board, starting with player 2.")
    print("You have 2 actions you may take on your turn. These may be any combination of the following:")
    print("Move a unit, Play a card, Expend a point for 3 mana, Spend mana to purchase units.")
    print("A max of 9 of each unit type can be on the map at once.")
    guide_return = input("Select an action: ")
    if guide_return:
        if guide_return[0].lower() == "u":
            previous_screen = "guide"
            unit_guide()
        if guide_return[0].lower() == "r":
            if previous_screen == "main":
                main()
            if previous_screen == "game_loop":
                game_loop()
            if previous_screen == "p1_place_units":
                p1_place_starting_units()
            if previous_screen == "p2_place_units":
                p2_place_starting_units()
            if previous_screen == "create":
                create_unit()
            if previous_screen == "p1_place_new_unit":
                p1_place_unit()
    else:
        print("Invalid input")
        guide()

def unit_guide():
    global previous_screen
    print("Units")
    print(f"{LIGHT_BLUE}Scout: Fast and cheap. The only unit that can travel two spaces in a turn.\nCan only move one space when starting on a resource.")
    print(f"{CYAN}Wind Walker: A specialized Scout. The can only travel one space a turn but\nare the only unit that can skip over mountain spaces.")
    print(f"{LIGHT_PURPLE}Tactician: Be prepared for any situation. Once per turn, you may discard up\nto 3 cards in hand and draw that many from the deck.")
    print(f"{LIGHT_CYAN}Drummer: The greatest sense of Morale. No units next to them can be \ndetroyed. Does not effect other Drummers. This unit can not attack.")
    print(f"{YELLOW}Paladin: The tankiest of units. When a paladin is attacked for the first\ntime, they are protected by a divine shield. The next attack will kill them.")
    print(f"{LIGHT_GREEN}Investor: Profits. When an Investor is on a resoure tile you get two of\nthat resource instead of one.{LIGHT_WHITE}")
    unit_guide_return = input("Press Enter to return")
    if previous_screen == "guide":
        guide()
    if previous_screen == "choose_starting_units":
        choose_starting_units()
        
def create_unit():
    global previous_screen
    global is_player_1_turn
    global player_1_units
    global player_2_units
    global player_1_current_mana
    global player_2_current_mana
    global scout_number
    global wind_walker_number
    global tactician_number
    global drummer_number
    global paladin_number
    global investor_number
    global action_count
    print(f"{LIGHT_WHITE}Actions     (U)nits  (R)eturn")
    print(f"1 Mana: {LIGHT_BLUE}(S)cout{LIGHT_WHITE} or {CYAN}(W)ind Walker{LIGHT_WHITE}")
    print(f"2 Mana: {LIGHT_PURPLE}(T)actician{LIGHT_WHITE} or {LIGHT_CYAN}(D)rummer{LIGHT_WHITE}")
    print(f"3 Mana: {YELLOW}(P)aladin{LIGHT_WHITE} or {LIGHT_GREEN}(I)nvestor{LIGHT_WHITE}")
    unit_creation = input("Select an action: ")
    temp_unit_list = []
    if unit_creation:
        if unit_creation[0].lower() == "u":
            previous_screen = "create"
            unit_guide()
        if unit_creation[0].lower() == "r":
            if previous_screen == "actions":
                game_loop()
        if unit_creation[0].lower() == "s":
            for unit in player_1_units:
                if unit.name == "Scout":
                    temp_unit_list.append(unit.number)
            for unit in player_2_units:
                if unit.name == "Scout":
                    temp_unit_list.append(unit.number)
            sorted_temp_units = sorted(temp_unit_list, key=lambda temp_unit_list: unit.number)
            if len(temp_unit_list) == 9:
                print("Too many of that unit")
                create_unit()
            if is_player_1_turn == True:
                player_1_current_mana -= 1
                scout_number = len(temp_unit_list)
                while scout_number in sorted_temp_units:
                    scout_number += 1
                    if scout_number >= 9:
                        scout_number = 1
                new_unit = Scout(scout_number)
                p1_place_unit(new_unit)
            if is_player_1_turn == False:
                player_2_current_mana -= 1
                scout_number = len(temp_unit_list)
                while scout_number in sorted_temp_units:
                    scout_number += 1
                    if scout_number >= 9:
                        scout_number = 1
                new_unit = Scout(scout_number)
                p2_place_unit(new_unit)
        if unit_creation[0].lower() == "w":
            temp_unit_list = []
            for unit in player_1_units:
                if unit.name == "Wind_Walker":
                    temp_unit_list.append(unit)
            for unit in player_2_units:
                if unit.name == "Wind_Walker":
                    temp_unit_list.append(unit)
            sorted_temp_units = sorted(temp_unit_list, key=lambda temp_unit_list: unit.number)
            if len(temp_unit_list) == 9:
                print("Too many of that unit")
                create_unit()
            if is_player_1_turn == True:
                player_1_current_mana -= 1
                wind_walker_number = len(temp_unit_list)
                while wind_walker_number in sorted_temp_units:
                    wind_walker_number += 1
                    if wind_walker_number >= 9:
                        wind_walker_number = 1
                new_unit = Wind_walker(wind_walker_number)
                p1_place_unit(new_unit)
            if is_player_1_turn == False:
                player_2_current_mana -= 1
                wind_walker_number = len(temp_unit_list)
                while wind_walker_number in sorted_temp_units:
                    wind_walker_number += 1
                    if wind_walker_number >= 9:
                        wind_walker_number = 1
                new_unit = Wind_walker(wind_walker_number)
                p2_place_unit(new_unit)
        if unit_creation[0].lower() == "t":
            temp_unit_list = []
            for unit in player_1_units:
                if unit.name == "Tactician":
                    temp_unit_list.append(unit)
            for unit in player_2_units:
                if unit.name == "Tactician":
                    temp_unit_list.append(unit)
            sorted_temp_units = sorted(temp_unit_list, key=lambda temp_unit_list: unit.number)
            if len(temp_unit_list) == 9:
                print("Too many of that unit")
                create_unit()
            if is_player_1_turn == True:
                if player_1_current_mana < 2:
                    print("Not enough Mana")
                    create_unit()
                player_1_current_mana -= 2
                tactician_number = len(temp_unit_list)
                while tactician_number in sorted_temp_units:
                    tactician_number += 1
                    if tactician_number >= 9:
                        tactician_number = 1
                new_unit = Tactician(tactician_number)
                p1_place_unit(new_unit)
            if is_player_1_turn == False:
                if player_2_current_mana < 2:
                    print("Not enough Mana")
                    create_unit()
                player_2_mana -= 2
                tactician_number = len(temp_unit_list)
                while tactician_number in sorted_temp_units:
                    tactician_number += 1
                    if tactician_number >= 9:
                        tactician_number = 1
                new_unit = Tactician(tactician_number)
                p2_place_unit(new_unit)
        if unit_creation[0].lower() == "d":
            temp_unit_list = []
            for unit in player_1_units:
                if unit.name == "Drummer":
                    temp_unit_list.append(unit)
            for unit in player_2_units:
                if unit.name == "Drummer":
                    temp_unit_list.append(unit)
            sorted_temp_units = sorted(temp_unit_list, key=lambda temp_unit_list: unit.number)
            if len(temp_unit_list) == 9:
                print("Too many of that unit")
                create_unit()
            if is_player_1_turn == True:
                if player_1_current_mana < 2:
                    print("Not enough Mana")
                    create_unit()
                player_1_current_mana -= 2
                drummer_number = len(temp_unit_list)
                while drummer_number in sorted_temp_units:
                    drummer_number += 1
                    if drummer_number >= 9:
                        drummer_number = 1
                new_unit = Drummer(drummer_number)
                p1_place_unit(new_unit)
            if is_player_1_turn == False:
                if player_2_current_mana < 2:
                    print("Not enough Mana")
                    create_unit()
                player_2_mana -= 2
                drummer_number = len(temp_unit_list)
                while drummer_number in sorted_temp_units:
                    drummer_number += 1
                    if drummer_number >= 9:
                        drummer_number = 1
                new_unit = Drummer(drummer_number)
                p2_place_unit(new_unit)
        if unit_creation[0].lower() == "p":
            temp_unit_list = []
            for unit in player_1_units:
                if unit.name == "Paladin":
                    temp_unit_list.append(unit)
            for unit in player_2_units:
                if unit.name == "Paladin":
                    temp_unit_list.append(unit)
            sorted_temp_units = sorted(temp_unit_list, key=lambda temp_unit_list: unit.number)
            if len(temp_unit_list) == 9:
                print("Too many of that unit")
                create_unit()
            if is_player_1_turn == True:
                if player_1_current_mana < 3:
                    print("Not enough Mana")
                    create_unit()
                player_1_current_mana -= 3
                paladin_number = len(temp_unit_list)
                while paladin_number in sorted_temp_units:
                    paladin_number += 1
                    if paladin_number >= 9:
                        paladin_number = 1
                new_unit = Paladin(paladin_number)
                p1_place_unit(new_unit)
            if is_player_1_turn == False:
                if player_2_current_mana < 3:
                    print("Not enough Mana")
                    create_unit()
                player_2_mana -= 3
                paladin_number = len(temp_unit_list)
                while paladin_number in sorted_temp_units:
                    paladin_number += 1
                    if paladin_number >= 9:
                        paladin_number = 1
                new_unit = Paladin(paladin_number)
                p2_place_unit(new_unit)
        if unit_creation[0].lower() == "i":
            temp_unit_list = []
            for unit in player_1_units:
                if unit.name == "Investor":
                    temp_unit_list.append(unit)
            for unit in player_2_units:
                if unit.name == "Investor":
                    temp_unit_list.append(unit)
            sorted_temp_units = sorted(temp_unit_list, key=lambda temp_unit_list: unit.number)
            if len(temp_unit_list) == 9:
                print("Too many of that unit")
                create_unit()
            if is_player_1_turn == True:
                if player_1_current_mana < 3:
                    print("Not enough Mana")
                    create_unit()
                player_1_current_mana -= 3
                investor_number = len(temp_unit_list)
                while investor_number in sorted_temp_units:
                    investor_number += 1
                    if investor_number >= 9:
                        investor_number = 1
                new_unit = Investor(investor_number)
                p1_place_unit(new_unit)
            if is_player_1_turn == False:
                if player_1_current_mana < 3:
                    print("Not enough Mana")
                    create_unit()
                player_2_mana -= 3
                investor_number = len(temp_unit_list)
                while investor_number in sorted_temp_units:
                    investor_number += 1
                    if investor_number >= 9:
                        investor_number = 1
                new_unit = Investor(investor_number)
                p2_place_unit(new_unit)
        else:
            print("Invalid selection")
            create_unit()
    else:
        print("Invalid selection")
        create_unit()
        
def p1_place_unit(new_unit):
    global player_1_units
    global action_count
    global scout_number
    global wind_walker_number
    global tactician_number
    global drummer_number
    global paladin_number
    global investor_number
    global is_player_1_turn
    global player_1_current_mana
    global player_2_current_mana
    letters = ["B", "C", "D", "E", "F", "G", "H", "I"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    not_allowed = []
    for letter in letters:
        for number in numbers:
            space = letter + str(number)
            not_allowed.append(space)
    new_unit_id = f"{new_unit.name} {new_unit.number}"
    allowed = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10"]
    print("Actions         (R)eturn")
    print(f"{LIGHT_WHITE}Map Guide               1   2   3   4   5   6   7   8   9   10")
    print(f"{BROWN}M - Mountain{LIGHT_WHITE}        A   {line_1}")
    print(f"{PURPLE}A - Arcane{LIGHT_WHITE}          B   {line_2}")
    print(f"{GREEN}R - Resupply{LIGHT_WHITE}        C   {line_3}")
    print(f"{NEGATIVE}C - Conquest{GREEN}{LIGHT_WHITE}        D   {line_4}")
    print(f"{LIGHT_BLUE}s - Scout{LIGHT_WHITE}           E   {line_5}")
    print(f"{CYAN}w - Wind Walker{LIGHT_WHITE}     F   {line_6}")
    print(f"{LIGHT_PURPLE}t - Tactician{LIGHT_WHITE}       G   {line_7}")
    print(f"{LIGHT_CYAN}d - Drummer{LIGHT_WHITE}         H   {line_8}")
    print(f"{YELLOW}p - Paladin{LIGHT_WHITE}         I   {line_9}")
    print(f"{LIGHT_GREEN}i - Investor{LIGHT_WHITE}        J   {line_10}")
    place_unit = input("Select space for unit(May only place on edge spaces, input must be exact, A1 format): ")
    if place_unit.lower() == "return" or place_unit.lower() == "r":
        if is_player_1_turn == True:
            if new_unit.name == "Scout":
                scout_number -= 1
                player_1_current_mana += 1
            if new_unit.name == "Wind_Walker":
                wind_walker_number -= 1
                player_1_current_mana += 1
            if new_unit.name == "Tactician":
                tactician_number -= 1
                player_1_current_mana += 2
            if new_unit.name == "Drummer":
                drummer_number -= 1
                player_1_current_mana += 2
            if new_unit.name == "Paladin":
                paladin_number -= 1
                player_1_current_mana += 3
            if new_unit.name == "Investor":
                investor_number -= 1
                player_1_current_mana += 3
        if is_player_1_turn == False:
            if new_unit.name == "Scout":
                scout_number -= 1
                player_2_current_mana += 1
            if new_unit.name == "Wind_Walker":
                wind_walker_number -= 1
                player_2_current_mana += 1
            if new_unit.name == "Tactician":
                tactician_number -= 1
                player_2_current_mana += 2
            if new_unit.name == "Drummer":
                drummer_number -= 1
                player_2_current_mana += 2
            if new_unit.name == "Paladin":
                paladin_number -= 1
                player_2_current_mana += 3
            if new_unit.name == "Investor":
                investor_number -= 1
                player_2_current_mana += 3
        create_unit()
    if place_unit in not_allowed:
        print("Space not allowed")
        p1_place_unit(new_unit)
    if place_unit in allowed:
        space_is = []
        for letter in place_unit:
            space_is.append(letter)
        placement_letter = space_is[0]
        if len(space_is) == 3:
            two_digit = "".join(space_is[1:])
        else:
            two_digit = ""
        if len(two_digit) == 2:
            placement_number = int(two_digit) - 1
        else:
            placement_number = int(space_is[1]) - 1
        placement = map_placement(placement_letter)
        if placement[placement_number] != "[]":
            print("Space already occupied")
            p1_place_unit()
        if new_unit.name == "Scout":
            placement[int(placement_number)] = f"{LIGHT_BLUE}s{new_unit.number}{LIGHT_WHITE}"
            player_1_units.append(new_unit)
            print(f"Added {LIGHT_BLUE}Scout{LIGHT_WHITE} {new_unit.number}")
            for unit in player_1_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Wind_Walker":
            placement[int(placement_number)] = f"{CYAN}w{new_unit.number}{LIGHT_WHITE}"
            player_1_units.append(new_unit)
            print(f"Added {CYAN}Wind Walker{LIGHT_WHITE} {new_unit.number}")
            for unit in player_1_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Tactician":
            placement[int(placement_number)] = f"{LIGHT_PURPLE}t{new_unit.number}{LIGHT_WHITE}"
            player_1_units.append(new_unit)
            print(f"Added {LIGHT_PURPLE}Tactician{LIGHT_WHITE} {new_unit.number}")
            for unit in player_1_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Drummer":
            placement[int(placement_number)] = f"{LIGHT_CYAN}d{new_unit.number}{LIGHT_WHITE}"
            player_1_units.append(new_unit)
            print(f"Added {LIGHT_CYAN}Drummer{LIGHT_WHITE} {new_unit.number}")
            for unit in player_1_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Paladin":
            placement[int(placement_number)] = f"{YELLOW}p{new_unit.number}{LIGHT_WHITE}"
            player_1_units.append(new_unit)
            print(f"Added {YELLOW}Paladin{LIGHT_WHITE} {new_unit.number}")
            for unit in player_1_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Investor":
            placement[int(placement_number)] = f"{LIGHT_GREEN}i{new_unit.number}{LIGHT_WHITE}"
            player_1_units.append(new_unit)
            print(f"Added {LIGHT_GREEN}Investor{LIGHT_WHITE} {new_unit.number}")
            for unit in player_1_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        map_join(placement_letter, placement)
        if place_unit not in allowed and place_unit not in not_allowed:
            print("Invalid space selection")
            p1_place_unit(new_unit)
    else:
        print("Invalid unit selection")
        p1_place_unit(new_unit)
    action_count -= 1
    if action_count == 0:
        turn_count += 1
        action_count = 2
    game_loop()

def p2_place_unit(new_unit):
    global player_2_units
    global action_count
    global scout_number
    global wind_walker_number
    global tactician_number
    global drummer_number
    global paladin_number
    global investor_number
    letters = ["B", "C", "D", "E", "F", "G", "H", "I"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    not_allowed = []
    for letter in letters:
        for number in numbers:
            space = letter + str(number)
            not_allowed.append(space)
    new_unit_id = f"{new_unit.name} {new_unit.number}"
    allowed = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10"]
    print("Actions         (R)eturn")
    print(f"{LIGHT_WHITE}Map Guide               1   2   3   4   5   6   7   8   9   10")
    print(f"{BROWN}M - Mountain{LIGHT_WHITE}        A   {line_1}")
    print(f"{PURPLE}A - Arcane{LIGHT_WHITE}          B   {line_2}")
    print(f"{GREEN}R - Resupply{LIGHT_WHITE}        C   {line_3}")
    print(f"{NEGATIVE}C - Conquest{GREEN}{LIGHT_WHITE}        D   {line_4}")
    print(f"{LIGHT_BLUE}s - Scout{LIGHT_WHITE}           E   {line_5}")
    print(f"{CYAN}w - Wind Walker{LIGHT_WHITE}     F   {line_6}")
    print(f"{LIGHT_PURPLE}t - Tactician{LIGHT_WHITE}       G   {line_7}")
    print(f"{LIGHT_CYAN}d - Drummer{LIGHT_WHITE}         H   {line_8}")
    print(f"{YELLOW}p - Paladin{LIGHT_WHITE}         I   {line_9}")
    print(f"{LIGHT_GREEN}i - Investor{LIGHT_WHITE}        J   {line_10}")
    place_unit = input("Select space for unit(May only place on edge spaces, input must be exact, A1 format): ")
    if place_unit.lower() == "return" or place_unit.lower() == "r":
        if new_unit.name == "Scout":
            scout_number -= 1
            player_2_mana += 1
        if new_unit.name == "Wind_Walker":
            wind_walker_number -= 1
            player_2_mana += 1
        if new_unit.name == "Tactician":
            tactician_number -= 1
            player_2_mana += 2
        if new_unit.name == "Drummer":
            drummer_number -= 1
            player_2_mana += 2
        if new_unit.name == "Paladin":
            paladin_number -= 1
            player_2_mana += 3
        if new_unit.name == "Investor":
            investor_number -= 1
            player_2_mana += 3
        create_unit()
    if place_unit in not_allowed:
        print("Space not allowed")
        p1_place_unit(new_unit)
    if place_unit in allowed:
        space_is = []
        for letter in place_unit:
            space_is.append(letter)
        placement_letter = space_is[0]
        if len(space_is) == 3:
            two_digit = "".join(space_is[1:])
        else:
            two_digit = ""
        if len(two_digit) == 2:
            placement_number = int(two_digit) - 1
        else:
            placement_number = int(space_is[1]) - 1
        placement = map_placement(placement_letter)
        if placement[placement_number] != "[]":
            print("Space already occupied")
            p2_place_starting_units()
        if new_unit.name == "Scout":
            placement[int(placement_number)] = f"{LIGHT_BLUE}s{new_unit.number}{LIGHT_WHITE}"
            player_2_units.append(new_unit)
            print(f"Added {LIGHT_BLUE}Scout{LIGHT_WHITE} {new_unit.number}")
            for unit in player_2_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Wind_Walker":
            placement[int(placement_number)] = f"{CYAN}w{new_unit.number}{LIGHT_WHITE}"
            player_2_units.append(new_unit)
            print(f"Added {CYAN}Wind Walker{LIGHT_WHITE} {new_unit.number}")
            for unit in player_2_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Tactician":
            placement[int(placement_number)] = f"{LIGHT_PURPLE}t{new_unit.number}{LIGHT_WHITE}"
            player_2_units.append(new_unit)
            print(f"Added {LIGHT_PURPLE}Tactician{LIGHT_WHITE} {new_unit.number}")
            for unit in player_2_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Drummer":
            placement[int(placement_number)] = f"{LIGHT_CYAN}d{new_unit.number}{LIGHT_WHITE}"
            player_2_units.append(new_unit)
            print(f"Added {LIGHT_CYAN}Drummer{LIGHT_WHITE} {new_unit.number}")
            for unit in player_2_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Paladin":
            placement[int(placement_number)] = f"{YELLOW}p{new_unit.number}{LIGHT_WHITE}"
            player_2_units.append(new_unit)
            print(f"Added {YELLOW}Paladin{LIGHT_WHITE} {new_unit.number}")
            for unit in player_2_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        if new_unit.name == "Investor":
            placement[int(placement_number)] = f"{LIGHT_GREEN}i{new_unit.number}{LIGHT_WHITE}"
            player_2_units.append(new_unit)
            print(f"Added {LIGHT_GREEN}Investor{LIGHT_WHITE} {new_unit.number}")
            for unit in player_2_units:
                if new_unit_id == f"{unit.name} {unit.number}":
                    unit.location = place_unit
        map_join(placement_letter, placement)
        if place_unit not in allowed and place_unit not in not_allowed:
            print("Invalid space selection")
            p2_place_unit(new_unit)
    else:
        print("Invalid unit selection")
        p2_place_unit(new_unit)
    action_count -= 1
    if action_count == 0:
        turn_count += 1
        action_count = 2
    game_loop()

def create_deck():
    global deck
    global discarded_cards
    global previous_screen
    global is_player_1_turn
    count = 4
    disc_count = 0
    temp_count = 0
    card_types = ["get a 1 mana unit", "get a 2 mana unit", "get a 3 mana unit", "refund one of your units", "get 1 mana", "get 1 conquest point", "destroy one of your opponents units", "move a unit 2 spaces", "opponent loses one conquest point", "get 2 mana"]
    if len(discarded_cards) == 0:
        for card in card_types:
            while temp_count < count:
                deck.append(card)
                temp_count += 1
            if temp_count == 4:
                temp_count = 0
    if len(discarded_cards) != 0:
        for card in card_types:
            if card in discarded_cards:
                disc_count += 1
                new_count = count - disc_count
                while temp_count < new_count:
                    deck.append(card)
                    temp_count += 1
    if previous_screen == "game_loop":
        game_loop()
    if previous_screen == "draw_cards":
        if is_player_1_turn == True:
            player_1 = "player_1"
            draw_cards(player_1)
        if is_player_1_turn == False:
            player_2 = "player_2"
            draw_cards(player_2)
    
def draw_cards(player):
    global deck
    global player_1_cards
    global player_2_cards
    global previous_screen
    if len(deck) == 0:
        previous_screen = "draw_cards"
        create_deck()
    if player == "player_1":
        rand_card = random.choice(deck)
        player_1_cards.append(rand_card)
        deck.remove(rand_card)
    if player == "player_2":
        rand_card = random.choice(deck)
        player_2_cards.append(rand_card)
        deck.remove(rand_card)
        
def use_card(player):
    global player_1_cards
    global player_2_cards
    global player_1_current_mana
    global player_2_current_mana
    global action_count
    count = 0
    print(player)
    print("Actions         (R)eturn")
    if player == "player_1":
        for card in player_1_cards:
            count += 1
            print(f"{count}. {card}")
    if player == "player_2":
        for card in player_2_cards:
            count += 1
            print(f"{count}. {card}")
    card_use = input("Choose a card number to use: ")
    if card_use.isdigit() == False:
        print("Invalid selection")
        use_card(player)
    if player == "player_1":
        if player_1_cards[int(card_use) - 1] == "get 1 mana":
            player_1_current_mana += 1
            player_1_cards.pop(int(card_use))
        if player_1_cards[int(card_use) - 1] == "get 2 mana":
            player_1_current_mana += 2
            player_1_cards.pop(int(card_use))
    if player == "player_2":
        if player_2_cards[int(card_use) - 1] == "get 1 mana":
            player_2_current_mana += 1
            player_2_cards.pop(int(card_use))
        if player_2_cards[int(card_use) - 1] == "get 2 mana":
            player_2_current_mana += 2
            player_2_cards.pop(int(card_use))
    action_count -= 1
    if action_count == 0:
        turn_count += 1
        action_count = 2
    game_loop()
        

def exchange_conquest(player):
    global player_1_conquest_points
    global player_2_conquest_points
    global player_1_current_mana
    global player_2_current_mana
    global action_count
    if player == "player_1":
        player_1_current_mana += 3
        player_1_conquest_points -= 1
    if player == "player_2":    
        player_2_current_mana += 3
        player_2_conquest_points -= 1
    action_count -= 1
    if action_count == 0:
        turn_count += 1
        action_count = 2
    game_loop()

def move(player):
    global player_1_units
    global player_2_units
    if player == "player_1":
        for units in player_1_units:
            print(units.unit_display())
    if player == "player_2":
        for units in player_2_units:
            print(units.unit_display())
    moving_unit = input("Choose Unit to move: ")
    if player == "player_1":
        for unit in player_1_units:
            if moving_unit == f"{unit.name} {unit.number}":
                chosen_space = input("Choose space for unit to move to: ")
            else:
                print("Invalid unit")
                move(player)
    if player == "player_2":
        for unit in player_2_units:
            if moving_unit == f"{unit.name} {unit.number}":
                chosen_space = input("Choose space for unit to move to: ")
            else:
                print("Invalid unit")
                move(player)
    allowed_spaces(moving_unit, chosen_space)
        

def allowed_spaces(moving_unit, chosen_space):
    global is_player_1_turn
    if is_player_1_turn == True:
        player = "player_1"
        for unit in player_1_units:
            if moving_unit == f"{unit.name} {unit.number}":
                unit_to_move = unit
                unit_type = unit.name
    if is_player_1_turn == False:
        player = "player_2"
        for unit in player_2_units:
            if moving_unit == f"{unit.name} {unit.number}":
                unit_to_move = unit
                unit_type = unit.name
    caps = list(string.ascii_uppercase)
    final_spaces = []
    split_starting_space = []
    starting_space = unit_to_move.location
    split_starting_space = list(starting_space)
    placement_letter = split_starting_space[0]
    if len(split_starting_space) == 3:
        two_digit = "".join(split_starting_space[1:])
    else:
        two_digit = ""
    if len(two_digit) == 2:
        placement_number = int(two_digit) - 1
    else:
        placement_number = int(split_starting_space[1]) - 1
    placement = map_placement(placement_letter)
    for cap in caps:
        if split_starting_space[0] == cap:
            current_letter = caps.index(cap)
    final_spaces.append(split_starting_space[0] + str(int(split_starting_space[1])))
    final_spaces.append(split_starting_space[0] + str((int(split_starting_space[1]) - 2)))
    if int(split_starting_space[1]) > 9:
        final_spaces.remove(split_starting_space[0] + str(int(split_starting_space[1])))
    if int(split_starting_space[1]) - 2 < 0:
        final_spaces.remove(split_starting_space[0] + str((int(split_starting_space[1]) - 2)))
    final_spaces.append((caps[current_letter - 1]) + str((int(starting_space[1]) - 1)))
    final_spaces.append((caps[current_letter + 1]) + str((int(starting_space[1]) - 1)))
    if current_letter - 1 < 0:
        final_spaces.remove((caps[current_letter - 1]) + str((int(starting_space[1]) - 1)))
    if current_letter + 1 > 9:
        final_spaces.remove((caps[current_letter + 1]) + str((int(starting_space[1]) - 1)))
    if player == "player_1":
        if unit_type == "Wind_Walker":
            for space in final_spaces:
                space_is = []
                for letter in space:
                    space_is.append(letter)
                print(space_is)
                placement_letter = space_is[0]
                if len(space_is) == 3:
                    two_digit = int("".join(space_is[1:]))
                    two_digit += 1
                else:
                    two_digit = ""
                print(two_digit)
                if len(two_digit) == 2:
                    placement_number = int(two_digit) - 1
                else:
                    placement_number = int(space_is[1])
                placement = map_placement(placement_letter)
                for cap in caps:
                    if placement_letter == cap:
                        mountain_space = caps.index(cap)
                print(placement[placement_number])
            if placement[placement_number] == "M":
                final_spaces.append(space_is[0] + str(placement_number))
                print(final_spaces)
                final_spaces.append(space_is[0] + str((int(placement_number) - 2)))
            if int(placement_number) > 9:
                final_spaces.remove(space_is[0] + str(placement_number))
            print(final_spaces)
            if int(placement_number) - 2 < 0:
                final_spaces.remove(space_is[0] + str((int(placement_number) - 2)))
            final_spaces.append((caps[int(space_is[0]) - 1]) + str((int(placement_number) - 1)))
            final_spaces.append((caps[int(space_is[0]) + 1]) + str((int(placement_number) - 1)))
            if space_is[0] - 1 < 0:
                final_spaces.remove((caps[int(space_is[0]) - 1]) + str((int(placement_number) - 1)))
            if space_is[0] + 1 > 9:
                final_spaces.remove((caps[int(space_is[0]) + 1]) + str((int(placement_number) - 1)))
            if chosen_space in final_spaces:
                final_spaces.remove(split_starting_space[0] + str(starting_space[1] - 1))
    print(final_spaces)
    space_is = []
    for letter in chosen_space:
        space_is.append(letter)
    placement_letter = space_is[0]
    if len(space_is) == 3:
        two_digit = "".join(space_is[1:])
    else:
        two_digit = ""
    if len(two_digit) == 2:
        placement_number = int(two_digit) - 1
    else:
        placement_number = int(space_is[1]) - 1
    placement = map_placement(placement_letter)
    if placement[placement_number] != "[]":
        if placement[placement_number] == "M" and unit.name != "Wind_Walker":
            print("Cannot move onto mountian")
            move(player)
        if (placement[placement_number]) == "M" and unit.name == "Wind_walker":
            print("Choose a space adjacent to mountain")
            move(player)
        

def resource_gain():
    pass