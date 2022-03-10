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
    word_of_the_day = []
    game_over = False

    def set_word_of_the_day(self):
        """
        Set word of the day
        """ 
        self.word_of_the_day = list(choice(words))
        return self.word_of_the_day

    def get_user_input(self):
        guess = input("Guess a 5 letter word: ")
        return guess
    
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


if __name__ == '__main__':
    game = AmharicWordle()
    print(game.set_word_of_the_day())

    i = 0
    while not game.game_over and i < 6:
        guess = game.get_user_input()
        game.set_colors(guess)
        i += 1
    
    if not game.game_over:
        print("You lost", game.word_of_the_day, " is the word.")