from Coffee_Data import Coffee_Spots
#from pynput import keyboard
import os
import time
from difflib import SequenceMatcher as Match
import math

### Clear Screen function
def clear_screen():
    os.system('cls')

### Time Sleep function
def wait():
    for s in range(0,3):
        print(".")

### Search by Name ###
def search_name():
    print("Please enter the name of the shop you would like to search for.\n")
    search = input("Shop name:")
    shop_names = [k for k in Coffee_Spots.keys()]
    print(search)
    print(shop_names)
    
    ##### Idea: on refactor, add in a suggestor. If user enters most of a name right, when program searching for name and doesn't
    ##### find exact match but close matches, will ask "where you looking for..." <provide close matches>
    ##### User will then have the option to select one of the provided suggestions if it matches what they were looking for

    #----------#

    #find common characters/ basic logic for suggestor
    ##### TO DO: Clean up. Logic basically works fine, but need to add/fix up the functionality.
    search_length = len(search)
    for e in Coffee_Spots.keys():
        match_val = math.floor(Match(None, e, search).ratio()*100)
        print(match_val)
        if match_val >= 60:
            return print(e)
##### Everything below here needs to be looked at again. Probably could be cleaned up a bit on a single pass
        elif match_val in range(25, 59):
            print("Did you mean " + e + "? Y or N")
            answer = input()
            if answer.lower() == "y":
                return print(e)
            elif answer.lower() == "n":
                continue
    
    print("I'm sorry, there are no shops that match.")
    #### I'm wanting to compare strings to see just how


### Search by Distance ###
def search_dist():
    print("Please enter how far you're okay with going for recommendations. 'Close' for any place within 20 minutes and 'Far' for any place over 20 minutes.")
    player_input = input("Close or Far? ")
    if player_input.lower() == 'close':
        for k,v in Coffee_Spots.items():
            ##### Will need to adjust the way the data is stored so that I can compare it with how close or far user will go
            pass


### Search by Score ###
def search_score():
    scores = list(range(1,6))
    player_input = input("To search by score, enter one, all, or none of the following options: " + str(scores) +".\nExample: entering 1 and 2 will only return options with scores of 1 or 2.\nPressing Enter without typing anything will return all shops in order of worst to best score.\n\nSearch: ")
    player_input = [e for e in player_input if e.isdigit()]
    print(player_input)
    shops_list = []
##### Push goal - have it check to see what scores are in the list, that way if a user selects a score to view that is not contained in the list, it returns that there are no recommendations with a score of x
##### 
    for e in player_input:
        for s,score in Coffee_Spots.items():
            print(s, score[1])
            if int(e) == math.floor(float(score[1])):    
                print(math.floor(float(score[1])))




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
            player_input = None







####### TESTING AREA #######

Menu()
