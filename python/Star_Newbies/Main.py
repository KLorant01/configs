import os
import Main_game
import Main_menu
import Main_settings
import Utility

try:
    with open('Data/settings.js', 'r') as fuck:
        if os.stat("Data/settings.js").st_size == 0:
            Utility.write_settings_def()
except:
    Utility.write_settings_def()
Utility.write_sys_inf()

state = 1

while 1:  # Main loop

    match state:
        case 0:
            Utility.clear_window()          # Exit the game
            break
        case 1:
            state = Main_menu.run()         # The user in the main menu
        case 2:
            state = Main_game.run()         # Launch the game!
        case 3:
            pass                            # Load game menu TODO make this once
        case 4:
            state = Main_settings.run()     # Settings menu
        case 5:
            pass                            # Achivements menu
