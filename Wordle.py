# File: Wordle.py

"""
Zach Bagley, Patrick Petty, Mark Thuet, Mark Barlocker
"""

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        s = s.lower()
        if s not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            gw.show_message("Congrats! Your word is valid.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Pick a random word from the list
    word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Display the word in the first row of boxes
    for i in range(len(word)):
        gw.set_square_letter(0, i, word[i])

# Startup code

if __name__ == "__main__":
    wordle()
