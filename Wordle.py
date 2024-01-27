import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

# Global variable to store statistics for the current session
guess_statistics = {}

def wordle():
    def enter_action(s):
        s = s.lower()
        if s not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            gw.show_message("Congrats! Your word is valid.")

            # Update guess statistics
            num_guesses = gw.get_current_row() + 1
            if num_guesses not in guess_statistics:
                guess_statistics[num_guesses] = 1
            else:
                guess_statistics[num_guesses] += 1

            # Check if the game is over
            if gw.get_current_row() == N_ROWS - 1:
                display_game_over()

    def display_game_over():
        # Display statistics at the end of each game
        gw.show_message("Game Over! Guess Statistics:")
        for guesses, count in guess_statistics.items():
            gw.show_message(f"{guesses} guesses: {count} times")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()
