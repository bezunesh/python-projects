import unittest
import pandas as pd
from unittest.mock import patch, Mock
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

    @patch('wordle.display')
    @patch('wordle.pd.DataFrame')
    @patch('wordle.input')
    def test_run_main(self, mock_input, mock_pd_dataframe, mock_display):
        self.game.set_word_of_the_day = Mock(return_value='lucky')
        mock_input.return_value = 'lobby'
        self.game.chances = 1
        row = 0
        # the userinput's the 1st and last characters are correct(green), while the rest not (grays)
        greens, oranges, grays = [0,4],[],[1,2,3]
        self.game.set_colors = Mock(return_value=(greens, oranges, grays))
        remaining_attempts = ['','','','','']
        self.game.remaining_attempts = Mock(return_value=[remaining_attempts])
        df_data = [['l','o','b','b','y'],remaining_attempts]
        df = pd.DataFrame('', columns=[0,1,2,3,4], indexs=[0,1,2,3,4,5])
        mock_pd_dataframe.return_value = df
        df.style.apply = Mock(return_value='')
    
        self.game.run_main()
        
        mock_input.assert_called_with("Guess a 5 letter word: ")
        self.assertEqual(self.game.attempts, [['l','o','b','b','y']])
        self.game.set_colors.assert_called_with('lobby')
        mock_pd_dataframe.assert_called_with(data=df_data)
        df.style.apply.assert_called_with(
            self.game.highight,
            axis=None,
            greens = greens,
            oranges=oranges,
            grays=grays,
            row=row
        )
        mock_display.assert_called_with('')
    

if __name__ == '__main__':
   unittest.main()