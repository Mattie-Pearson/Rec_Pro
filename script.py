import os
from search_functions import search_name, search_dist, search_score, wait

### Clear Screen function
def clear_screen():
    os.system('cls')

### Menu options
options = {
    "Search by Name" : search_name, "Search by Distance": search_dist, "Search by Score": search_score
}

### Main Menu ###
def Menu():
    #clear_screen()
    selected = 0
    while selected == 0:
        print("\nWelcome to the Main Menu of Recommendation Pro! Enter 1, 2, or 3 to select an option:\n")
        sub_menus = []
        for k in options.keys():
            print(k) ### Remove when finished
            sub_menus.append(k)
        player_selection = int(input("\nPlayer selection: "))
        try:
            player_selection = sub_menus[(player_selection - 1)]
        except IndexError:
            print("Index is out of range. Please enter a valid option.\n")
            continue
        except:
            print("Something else went wrong")
        try:
            callable(options[player_selection])
            print("You have selected  " + player_selection)
            wait()
            options[player_selection]()
        except KeyError:
            print("Cannot call. The key does not exist.\nPotentially booted out of the function back to menu.")
            print(player_selection)
            continue
        except:
            print("Something else went wrong")






####### TESTING AREA #######

Menu()
