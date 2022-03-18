import unittest
import pandas as pd
from unittest.mock import patch
from random import choice
from wordle import AmharicWordle

class WordleTest(unittest.TestCase):
    
    def setUp(self):
        self.game = AmharicWordle()
        
    def test_initialization(self):
        game = self.game
        self.assertEqual(game.word_of_the_day, [])
        self.assertEqual(game.length_of_word, 5)
        self.assertEqual(game.attempts, [])
        self.assertEqual(game.chances, 6)
        self.assertFalse(game.game_over)
        self.assertIsInstance(AmharicWordle.style_df, pd.DataFrame)
        df = AmharicWordle.style_df
        self.assertEqual(list(df.index), [0,1,2,3,4,5])
        self.assertEqual(list(df.columns), [0,1,2,3,4])

    def test_set_word_of_the_day(self):
        words = ["lucky", "green", "thick"]
        word_of_the_day = self.game.set_word_of_the_day()
        self.assertIn(''.join(word_of_the_day), words)
    
    @patch('builtins.input', return_value='lucky')
    def test_get_user_input(self,input):
        self.assertEqual(self.game.get_user_input(), 'lucky')

    def test_remaining_attempts(self):
        self.game.attempts = ["monks", "books"]
        # 4 chances remain
        remaining_list = [list("_"*5) for i in range(4)]
        self.assertEqual(self.game.remaining_attempts(), remaining_list)

    def test_end_gmae(self):
        self.game.end_game(True)
        self.assertTrue(self.game.game_over)
        self.game.end_game(False)
        self.assertFalse(self.game.game_over)

if __name__ == '__main__':
   unittest.main()