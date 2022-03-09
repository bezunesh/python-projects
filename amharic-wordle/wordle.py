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
    word_of_the_day = ""
    game_over = False

    def set_word_of_the_day(self):
        """
        Set word of the day
        """ 
        self.word_of_the_day = choice(words)
        return self.word_of_the_day

    def get_user_input(self):
        guess = input("Guess a 5 letter word: ")
        return guess
    
    def check(self, word):
        if self.word_of_the_day == word:
            self.game_over = True
            print("You got it.", self.word_of_the_day, " is the word.")
        else:
            zipped = zip(word, self.word_of_the_day)
            for x, y in zipped:
                if x == y:
                    print("Green ", x, y)
                elif x in self.word_of_the_day:
                    print("Orange ", x)
            

if __name__ == '__main__':
    game = AmharicWordle()
    print(game.set_word_of_the_day())

    i = 0
    while not game.game_over and i < 6:
        guess = game.get_user_input()
        game.check(guess)
        i += 1
    
    if not game.game_over:
        print("You lost", game.word_of_the_day, " is the word.")