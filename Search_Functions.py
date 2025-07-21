from difflib import SequenceMatcher as Match
from Coffee_Data import Coffee_Spots
import math



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
##### TO DO: Everything below here needs to be looked at again. Probably could be cleaned up a bit on a single pass
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

    dist = { 
        "close": [],
        "far": []
    }

    for k,v in Coffee_Spots.items():
        #Check if close
        if v[0]['min'] <= 20:
            dist["close"].append(k)
        #Else add to far
        else:
            dist["far"].append(k)
     
    print("Please enter how far you're okay with going for recommendations. 'Close' for any place within 20 minutes and 'Far' for any place over 20 minutes.")
    player_input = input("Close or Far? ")
    moreinfo_key = player_input
    print(dist[player_input.lower()])
    player_input = input("Would you like more information on one of these? Y or N")

    if player_input.lower() == 'y':
        on = 1
        while on == 1:

### TO DO   #### As data expands, this will have to be refactored to account for the fact that there could be more than 2 options.
            #### range(len(dist[moreinfo_key]))
            #### input("Which would you like more information on? {0}".format((str(n) + ", " for n in range(len(dist[moreinfor_key]))))) ? 

            player_input = input("Which would you like more information on? 1 or 2. ")
            if player_input == "1":
                print("You've chosen to have more information on {0}".format(dist[moreinfo_key][0]))
### TO DO       #### fix up the way these are printed out so they're prettier
                print(Coffee_Spots[dist[moreinfo_key][0]])
            elif player_input == "2":
                print("You've chosen to have more information on {0}".format(dist[moreinfo_key][1]))
                print(Coffee_Spots[dist[moreinfo_key][1]])
            else:
                print("Please enter a valid answer")
                continue
            player_input = input("Would you like to see the information for another? Y or N")
            if player_input.lower() == "y":
                continue
            elif player_input.lower() == "n":
                on = 0
                print("Returning to Main Menu")
                wait()
    elif player_input.lower() == "n":
        return
            


### Search by Score ###
def search_score():
    player_input = input("To search by score, enter one, all, or none of the following options: " + str(list(range(1,6))) +".\nExample: entering 1 and 2 will only return options with scores of 1 or 2.\nPressing Enter without typing anything will return all shops in order of worst to best score.\n\nSearch: ")
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