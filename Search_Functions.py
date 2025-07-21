from difflib import SequenceMatcher as Match
from Coffee_Data import Coffee_Spots
import math

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
    dist = {}
    for k,v in Coffee_Spots.items():
        if v[0]['min'] <= 20:
            dist["close"] += k
        else:
            dist["far"] += k
    print(dist)
     
        #### Have a prompt that asks if user wants more information.. Should probably set up a system to hold the information of the recs that do pass and get printed. 
        #### That way not going through the whole dict again.


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