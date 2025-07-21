import os
import time
from Search_Functions import search_name, search_dist, search_score

### Clear Screen function
def clear_screen():
    os.system('cls')

### Time Sleep function
def wait():
    for s in range(0,3):
        print(".")


### Menu options
options = {
    "Search by Name" : search_name, "Search by Distance": search_dist, "Search by Score": search_score
}

### Main Menu ###
def Menu():
    clear_screen()
    selected = 0
    print("Welcome to the Main Menu of Recommendation Pro! Enter 1, 2, or 3 to select an option:\n")
    while selected == 0:
        sub_menus = []
        for k in options.keys():
            print(k) ### Remove when finished
            sub_menus.append(k)
        player_input = int(input("\nPlayer selection: "))
        try:
            player_input = sub_menus[(player_input - 1)]
        except IndexError:
            print("Index is out of range. Please enter a valid option.\n")
            continue
        except:
            print("Something else went wrong")
        try:
            callable(options[player_input])
            print("You have selected  " + player_input)
            wait()
            options[player_input]()
        except KeyError:
            print("Cannot call. The key does not exist.\n")
            continue
        except:
            print("Something else went wrong")






####### TESTING AREA #######

Menu()
