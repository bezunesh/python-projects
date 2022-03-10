"""
***  Amharic Wordle ***

The Rules of the Game
======================
1. Each day the code will randomly select a 5-letter word from the Amharic DataSource
2. You have six tries to guess the word correctly
3. If you guess the exact position of a letter in the word it will turn GREEN
4. If you guess a letter that exists in the word of the day, but it is in the wrong position it turns ORANGE
5. If the letter does not exist, it will stay gray
"""

from random import choice
import pandas as pd

words = ["lucky", "green", "thick"]
class AmharicWordle:

    def __init__(self):
        self.word_of_the_day = []
        self.length_of_word = 5
        self.trials = []
        self.no_of_trials = 6
        self.game_over = False

    def set_word_of_the_day(self):
        """
        Set word of the day
        """ 
        self.word_of_the_day = list(choice(words))
        return self.word_of_the_day

    def get_user_input(self):
        guess = input("Guess a 5 letter word: ")
        self.trials.append(list(guess))
        return guess
    
    def remaining_trials(self):
         return [list("_"*5) for i in range(self.no_of_trials - len(self.trials))]    
    
    def end(self, status):
        self.game_over = status
    
    def set_colors(self, guess):
        greens = []
        oranges = []
        grays = []

        zipped = list(zip(guess, self.word_of_the_day, range(5)))
        greens = [i for x, y, i in zipped if x == y]

        # so that they remeber their position
        guess = list(zip(guess, range(5)))

        # remove the greens
        guess = list(filter(lambda x: x[1] not in greens, guess))
        word_of_the_day = list(filter(lambda x: x[0] not in greens, list(enumerate(self.word_of_the_day))))

        word_of_the_day = [letter for index, letter in word_of_the_day]
        for letter, index in guess:
            if letter in word_of_the_day:
                oranges.append(index)
                # update 
                word_of_the_day.remove(letter)
            else:
                grays.append(index)

        return greens, oranges, grays

    def table(self):
        data = self.trials + self.remaining_trials()
        df = pd.DataFrame(data=data)
        print(df)
    
    def run_main(self):
        print(self.set_word_of_the_day())
        i = 0
        while i < self.no_of_trials:
            guess = self.get_user_input()
            self.table()
            green, orange, gray = self.set_colors(guess)
            if len(green) == self.length_of_word: 
                print("You Won", self.word_of_the_day, " is the word.")
                self.end(True)
                break
            i += 1
            
        if not self.game_over:
            print("You lost", self.word_of_the_day, " is the word.")

if __name__ == '__main__':
    game = AmharicWordle()
    game.run_main()