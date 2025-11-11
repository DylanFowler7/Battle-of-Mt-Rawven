import sys
import random
from game_loop import game_loop
from game_loop import guide

previous_screen = "main"
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
LIGHT_CYAN = "\033[1;36m"
NEGATIVE = "\033[7m"

def main():
    global previous_screen
    while True:
        print(f"{LIGHT_WHITE}Welcome to Battle of Mt. Rawven: the tactical, unit based board game for two.")
        print("Select one of the following: \n1. Play against (h)uman\n2. Play against (b)ot\n3. (G)uide\n4. (Q)uit")
        print("------------------------------")
        first_input = input()
        print("------------------------------")
        if first_input == "":
            print("Invalid Input")
            main()
        if first_input[0].lower() == "1" or first_input[0].lower() == "h":
            print("Beginning game")
            print("------------------------------")
            game_loop()
        if first_input[0].lower() == "2" or first_input[0].lower() == "b":
            player_first = False
            flip = random.choice([0, 1])
            if flip == 1:
                player_first = True
            print("Beginning game")
            print("------------------------------")
            game_loop()
        if first_input[0].lower() == "3" or first_input[0].lower() == "g":
            previous_screen = "main"
            guide()
        if first_input[0].lower() == "4" or first_input[0].lower() == "q":
            sys.exit(0)

if __name__ == "__main__":
    main()





