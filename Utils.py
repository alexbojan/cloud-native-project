
import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    # Clears the screen
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux and Mac
