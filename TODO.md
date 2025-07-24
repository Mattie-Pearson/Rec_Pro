#### To Do List
Ordered by file (for now)

### coffee_data.py
None

### script.py
None

### search_functions.py
To Dos:
- search_name() 
    - General cleanup. Logic basically wortks find but need to add and fix functionality. 
    - Cleanup specifically after <elif match_val in range...> 

- search_dist() 
    - As data expands. everything on the while loop will need to be refactored to account for the possibility of more than 2 options
    - range(len(dist[moreinfo_key]))
    - input("Which would you like more information on? {0}".format(str(n)) + ", " for n in range(len(dist[moreinfo_key]))) ? Untried/untested. Just a point to bounce from.
    - fix up the way things are printed so they're easier to read/prettier (aft line 69)

- search_score()
    - have it check to see what scores are in the list, that way if a user selects a score to view that is not contained in the list, it returns that there are no recommendations with a score of x without having to iterate through the entire list. cache the information so retrieval is easy.



Ideas:
- DONE Idea_1: On refactor add suggestor
- TO DO Idea_2: Clean up suggestor. Maybe make it its own function?
