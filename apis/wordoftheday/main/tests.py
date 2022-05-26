from os.path import dirname
from django.test import TestCase
from random import choice
from .api.resource import WordOfTheDay

class WordOfTheDayTest(TestCase):
    
    def setUp(self):
        self.api = WordOfTheDay()
    
    def test_initialization(self):
        self.assertIsNotNone(self.api.word_list)
        self.assertIsNotNone(self.api.word)
    
    def test_loadWords(self):         
        self.assertIsInstance(self.api.loadWords(), list)
        self.api.fileName = "NonExistingFilename.txt"
        with self.assertRaises(OSError):       
            self.api.loadWords()
    
    def test_getWordOfTheDay(self):
        self.assertIsInstance(self.api.getWordOfTheDay(), str)

