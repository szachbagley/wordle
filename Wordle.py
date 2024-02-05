import random
import pyperclip
import tkinter as tk
from tkinter import messagebox

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR


# Global variable to store statistics for the current session
guess_statistics = {}

def wordle():
    def enter_action(s):
        
        s = s.lower()
        if s not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            print(s)
            print(word)
        else:
                # Get the current row
            row = gw.get_current_row()
                

            # Check each letter in the guess
            for col in range(N_COLS):
                guess_letter = gw.get_square_letter(row, col).lower()
                if guess_letter == word[col]:
                    # The guessed letter is correct
                    gw.set_square_color(row, col, CORRECT_COLOR)
                elif guess_letter in word:
                    # The guessed letter is present but in the wrong position
                    gw.set_square_color(row, col, PRESENT_COLOR)
                else:
                    # The guessed letter is missing
                    gw.set_square_color(row, col, MISSING_COLOR)

            

            # Update guess statistics
            num_guesses = gw.get_current_row() + 1
            #if num_guesses not in guess_statistics:
            #    guess_statistics[num_guesses] = 1
            #else:
             #   guess_statistics[num_guesses] += 1

            # Check if the user has correctly guessed all five letters
            if s == word:
                gw.show_message(f"Congrats! You've guessed the word! \n Guesses: {num_guesses}/6  -  results copied to clipboard")
                print("Congrats! You've guessed the word!")
                pyperclip.copy(f"Wordle Guesses: {num_guesses}/6")

            elif s != word and row < N_ROWS -1:
                # Move on to the next row for the next guess
                gw.set_current_row(row + 1)
                gw.show_message("Congrats! Your word is valid.")
                print("Your word is valid")
            else:
                # The game is over
                gw.show_message(f"Game Over!")
                pyperclip.copy(f"I didn't guess the word :(")


   # def display_game_over():
        # Display statistics at the end of each game
    #    gw.show_message("Game Over! Guess Statistics:")
     #   for guesses, count in guess_statistics.items():
      #      gw.show_message(f"{guesses} guesses: {count} times")

    colorblind = False
        
    result = messagebox.askquestion("Mode Selection", "Do you want to play in colorblind mode?")
        
    if result == "yes":
        colorblind = True
    else: 
        colorblind = False
        
    if colorblind == False:
        CORRECT_COLOR = "#66BB66"       # Light green for correct letters
        PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
    else: 
        CORRECT_COLOR = "#0000FF"
        PRESENT_COLOR = "#FF0000"
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Pick a random word from the list
    word = random.choice(FIVE_LETTER_WORDS).lower()
    print(word)
    


# Startup code
if __name__ == "__main__":
    wordle()