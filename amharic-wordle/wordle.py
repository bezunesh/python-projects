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
        return guess
    
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


    def board(self, word="", r=0):
        # prints 5X6 board
        self.trials.append(list(word))
        for trial in self.trials:
            print("\n")
            for letter in trial:
                print(letter, "\t", end="") 
            
        # fill the remaining rows blank
        for row in range(self.no_of_trials-len(self.trials)):  
                print("\n", "__\t"*self.length_of_word)
            

if __name__ == '__main__':
    game = AmharicWordle()
    print(game.set_word_of_the_day())
  
    i = 0
    while i < game.no_of_trials:
        guess = game.get_user_input()
        game.board(guess, i)
        green, orange, gray = game.set_colors(guess)
        if len(green) == game.length_of_word: 
            print("You Won", game.word_of_the_day, " is the word.")
            game.end(True)
            break
        i += 1
    
    if not game.game_over:
        print("You lost", game.word_of_the_day, " is the word.")