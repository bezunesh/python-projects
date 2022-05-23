import unittest
from unittest.mock import patch, Mock
from random import choice
from word_of_the_day import WordOfTheDay

class WordOfTheDayTest(unittest.TestCase):
    
    def setUp(self):
        self.api = WordOfTheDay()
    
    def test_initialization(self):
        self.assertEqual(self.api.fileName, 'amharic-words.dat')
        self.assertIsNotNone(self.api.word_list)
        self.assertIsNotNone(self.api.word)
    
    def test_loadWords(self):
        self.assertIsInstance(self.api.loadWords(), list)

        self.api.fileName = "NonExistingFilename.txt"
        with self.assertRaises(OSError):
            self.api.loadWords()
    
    def test_getWordOfTheDay(self):
        self.assertIsInstance(self.api.getWordOfTheDay(), str)
