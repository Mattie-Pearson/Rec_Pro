from Coffee_Data import Coffee_Spots
from pynput import keyboard
import os

#for key, value in Coffee_Spots.items():
#    pass

power = 1

### Menu options
options = [
    "Search by Name", "Search by Distance", "Search by Score"
]

### Clear Screen function
def clear_screen():
    os.system('cls')

def on_press(key):
    try:
        # Printing the key that was pressed
        clear_screen()
        print(f'Key {key.char} pressed')
    except AttributeError:
        # Handling special keys
        print(f'Special key {key.name} pressed')

def on_release(key):
    # Exiting the program when the 'esc' key is pressed
    if key == keyboard.Key.esc:
        print('Exiting program')
        return False
    
### Main Menu ###
def Menu():
    clear_screen()
    selection = 0
    selected = 0
    print("Welcome to the Main Menu of Recommendation Pro! Use the arrow keys to move and Enter to select an option:\n")
    while selected == 0:
        for k in range(len(options)):
            if on_press(k) == selection:
                print("--->" + options[k])
            else:
                print('    ' + options[k])
        player_input = input()
        if player_input == keyboard.Key.down:
            selection += 1
            clear_screen()
            continue
        elif input() == keyboard.Key.enter:
            pass

### Keyboard Listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        # Running the listener in the background
        listener.join(Menu())