# Rec_Pro
Recommendation Program



### Running the program
Open a new terminal and type: python script.py

 -Note: The program doesn't take any arrow keys and won't open a new application window or anything fancy. You'll be using it directly within the terminal and need to make sure you're focused on it... There have been a few times where I've accidentally typed a num or letter just in my .py file cause I wasn't focused on the terminal.

### What you can do in the program
Look up a small library of coffee shops by name, distance, or score.

## Quit the program
You can end the program at any time using Ctrl + C
----------------
### Overview of files

coffee_data - 
- Dictionary where shop name is Key and the rest of the information is held in a list. Format can be seen in file.

script.py -
- Where the main aspect of the program runs. Only really calls functions of the sub-menus and doesn't really hold a function outside of the program base.

search_functions.py -
- File where the bulk of the functions that do the work are held. There are only three search functions currently (Name, Distance, and Score).
    - Search Name: very simple. Takes the chars entered by user and determines which shop name to provide based on which shop had the highest match in characters. This is done to allow for mis-spells or different interpretations. If the input match is below a certain amount the program will prompt the user asking if that is the name they were searching for. Anything below a 25 pct match fails and is not offered as an option.