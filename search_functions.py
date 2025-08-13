from difflib import SequenceMatcher as Match
from coffee_data import coffee_spots
import math



### Time Sleep function
def wait():
    for s in range(0,3):
        print(".")


### Search by Name ###
def search_name():
    loop = 1
    confirmed = 1

    while loop == 1:
        print("Please enter the name of the shop you would like to search for. If you would like to return to the main menu, enter 'Return'.")
        search = input("Shop name:")
        search_length = len(search)

        if search.lower() == "return":
            loop = 0
            return loop

        for e in coffee_spots.keys():
            match_val = math.floor(Match(None, e, search).ratio()*100)
            print(match_val)
            print(confirmed)

            if match_val >= 60:
                return print("{0} is {1} minutes away and has a score of {2}\n".format(e, coffee_spots[e][0]['min'], coffee_spots[e][1]))
            elif match_val in range(25, 59) and confirmed == 1:
                answer = input("Did you mean " + e + "? Y or N.\nInput: ")

                if answer.lower() == "y":
                    print("Awesome! {0} is {1} minutes away and has a score of {2}\n".format(e, coffee_spots[e][0]['min'], coffee_spots[e][1]))
                    confirmed = 0
                    continue
                elif answer.lower() == "n":
                    #### Maybe add logic here later? Or just print all of the names and recurse
                    print("check")
                    continue
            elif match_val in range(0,24) and confirmed == 1:
                print("I'm sorry, we weren't able to find a match.. Returning you to the beginning...\n")
                


### Search by Distance ###
def search_dist():

    dist = { 
        "close": [],
        "far": []
    }

    for k,v in coffee_spots.items():
        #Check if close
        if v[0]['min'] <= 20:
            dist["close"].append(k)
        #Else add to far
        else:
            dist["far"].append(k)
     
    print("Please enter how far you're okay with going for recommendations. 'Close' for any place within 20 minutes and 'Far' for any place over 20 minutes.")
    player_input = input("Close or Far? ")
    moreinfo_key = player_input.lower()
    player_input = input("Would you like more information on one of these? Y or N.\nInput: ")

    if player_input.lower() == 'y':
        on = 1
        while on == 1:
            if player_input == "y":
                player_input = input("Which would you like more information on? 1 or 2.\nInput: ")
                
            if player_input == "1":
                print(player_input)
                try:
                    print(f"You've chosen to have more information on {dist[moreinfo_key][0]}")
                    print(coffee_spots[dist[moreinfo_key][0]])
                    player_input = input("\nTo return to the main menu, type 'Return'. To see the other option, type 'Other'.\nInput: ")
                    if player_input.lower() == 'return':
                        return
                    elif player_input.lower() == 'other':
                        player_input = "2"
                        continue 
                except:
                    print("Failed to find 1")
            
            elif player_input == "2":
                try:
                    print("You've chosen to have more information on {0}".format(dist[moreinfo_key][1]))
                    print(coffee_spots[dist[moreinfo_key][1]])
                    player_input = input("\nTo return to the main menu, type 'Return'. To see the other option, type 'Other'.\nInput: ")
                    if player_input.lower() == 'return':
                        return
                    elif player_input.lower() == 'other':
                        player_input = "1"
                        continue 
                except: 
                    print("Failed to find 2")
            elif player_input != ("1" or "2"):
                print("Please enter a valid answer")
                continue

    elif player_input.lower() == "n":
        player_input = input("Would you like to return to the Main Menu? Y or N.\nInput: ")
        
        if player_input.lower() == "y":
            print("Returning")
            wait()
        elif player_input.lower() == "n":
            search_dist()
            


### Search by Score ###
def search_score():
    player_input = input("To search by score, enter one, all, or none of the following options: " + str(list(range(1,6))) +".\nExample: entering 1 and 2 will only return options with scores of 1 or 2.\nPressing Enter without typing anything will return all shops in order of worst to best score.\n\nSearch: ")


    if player_input == "":
        print("Needs to print all stores in order worst to best.")
        store_scores = [(s,score[1]) for s,score in coffee_spots.items()]
        order = []
        for e in store_scores:
            order.append(e[1])
        print(order)
            
    

    player_input = [e for e in player_input if e.isdigit()]
    shops_list = []
    x = list(range(1,6))
    print(x)

    if player_input:
        print("contains")
        for e in player_input:
            for s,score in coffee_spots.items():
                print(s, score[1])

                if int(e) == math.floor(float(score[1])):    
                    print(math.floor(float(score[1])))
                else:
                    print("No shops with a score of {e} are available".format(e=e))
    elif player_input == []:
        print("empty")
    else:
        player_input = input("Please input a valid answer. If you would like to exit, enter return. Otherwise press enter.\nInput: ")
        
        if player_input.lower() == "return":
            wait()
            return
        elif player_input == "":
            wait()
            search_score()