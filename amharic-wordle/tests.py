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
        
    def test_remaining_attempts(self):
        self.game.attempts = ["monks", "books"]
        # 4 chances remain
        remaining_list = [list("_"*5) for i in range(4)]
        self.assertEqual(self.game.remaining_attempts(), remaining_list)

    def test_end_game(self):
        self.game.end_game(True)
        self.assertTrue(self.game.game_over)
        self.game.end_game(False)
        self.assertFalse(self.game.game_over)

    def test_set_colors(self):
        self.game.word_of_the_day = "apple"
        self.assertEqual(self.game.set_colors("kiwis"), ([],[],[0,1,2,3,4]))
        self.assertEqual(self.game.set_colors("apple"), ([0,1,2,3,4],[],[]))
        self.assertEqual(self.game.set_colors("about"), ([0],[],[1,2,3,4]))
        self.assertEqual(self.game.set_colors("appen"), ([0,1,2],[3],[4]))
        self.assertEqual(self.game.set_colors("lobby"), ([],[0],[1,2,3,4]))
        self.assertEqual(self.game.set_colors("pelle"), ([3,4],[0],[1,2]))

    def test_highlight_applies_css_colors(self):
        row, greens, oranges, grays = 0, [0, 2], [3], [1, 4]
        row_0 = ['background-color: green',
                'background-color: gray',
                'background-color: green',
                'background-color: orange',
                'background-color: gray']
        data = [['','','','',''] for i in range(5)]
        data.insert(0, row_0)
        df = pd.DataFrame(data)
        resulting_style_df = self.game.highight([], row=row, greens=greens, oranges=oranges, grays=grays)
        self.assertTrue(df.equals(resulting_style_df))
    
    def test_highlight_turns_all_cells_green(self):
        row, greens, oranges, grays = 1, [0,1,2,3,4], [], []
        row_1 = [
            'background-color: green',
            'background-color: green',
            'background-color: green',
            'background-color: green',
            'background-color: green']
        data = [['','','','',''] for i in range(5)]
        data.insert(1, row_1)
        df = pd.DataFrame(data)
        resulting_style_df = self.game.highight([], row=row, greens=greens, oranges=oranges, grays=grays)
        self.assertTrue(df.equals(resulting_style_df))


if __name__ == '__main__':
   unittest.main()