"""
***  Amharic Wordle ***

The Rules of the Game
======================
1. You have six tries to guess the word correctly
2. If you guess the exact position of a letter in the word it will turn GREEN
3. If you guess a letter that exists in the word of the day, but it is in the wrong position it turns ORANGE
4. If the letter does not exist, it will stay gray
"""

from random import choice
import pandas as pd
from IPython.display import display

class AmharicWordle:
    style_df = None
    
    def __init__(self):
        self.word_of_the_day = []
        self.length_of_word = 5
        self.attempts = []
        self.chances = 6
        self.game_over = False
        AmharicWordle.style_df = pd.DataFrame('', index=[0,1,2,3,4,5], 
            columns=[0,1,2,3,4])

    def set_word_of_the_day(self):
        #TODO: load a data file and get a random word form it
        words = ["lucky", "green", "thick"]
        self.word_of_the_day = list(choice(words))
        return self.word_of_the_day
    
    def remaining_attempts(self):
        remaining = self.chances - len(self.attempts)
        return [list("_"*5) for i in range(remaining)]    
    
    def end_game(self, status):
        self.game_over = status
    
    def set_colors(self, guess):
        greens = []
        oranges = []
        grays = []

        zipped = list(zip(guess, self.word_of_the_day, range(5)))
        greens = [i for x, y, i in zipped if x == y]
        guess = list(zip(guess, range(5)))
        # remove the greens
        guess = list(filter(lambda x: x[1] not in greens, guess))
        word_of_the_day = list(filter(lambda x: x[0] not in greens, list(enumerate(self.word_of_the_day))))
        word_of_the_day = [letter for index, letter in word_of_the_day]
        for letter, index in guess:
            if letter in word_of_the_day:
                oranges.append(index)
                word_of_the_day.remove(letter)
            else:
                grays.append(index)
        return greens, oranges, grays

  
    def highight(self, df, **kwargs):
        c0 = 'background-color: green'
        c1 = 'background-color: orange'
        c2 = 'background-color: gray'
        c_row = kwargs['row']

        for pos in kwargs['greens']:
            AmharicWordle.style_df.loc[[c_row],pos] = c0
        
        for pos in kwargs['oranges']:
            AmharicWordle.style_df.loc[[c_row],pos] = c1
        
        for pos in kwargs['grays']:
            AmharicWordle.style_df.loc[[c_row],pos] = c2

        return AmharicWordle.style_df

    def run_main(self):
        self.set_word_of_the_day()
        i = 0
        
        while i < self.chances:
            guess = input("Guess a 5 letter word: ")
            self.attempts.append(list(guess))

            greens, oranges, grays = self.set_colors(guess)
            data = self.attempts + self.remaining_attempts()
            df = pd.DataFrame(data=data)

            s = df.style.apply(self.highight, axis=None,
                greens=greens, oranges=oranges, grays=grays, row=i)  
            display(s)

            if len(greens) == self.length_of_word: 
                print("You Won", self.word_of_the_day, " is the word.")
                self.end_game(True)
                break
            i += 1
        if not self.game_over:
            print("You lost", self.word_of_the_day, " is the word.")


if __name__ == '__main__':
    game = AmharicWordle()
    game.run_main()