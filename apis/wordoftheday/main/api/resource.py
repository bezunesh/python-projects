"""
A REST API that provides a randomly choosen word of the day in amharic
"""
from __future__ import annotations
from random import choice
from os.path import dirname
import json

class WordOfTheDay:
    '''
    WordOfTheDay
    '''
    def __init__(self):
        self.fileName = dirname(__file__) + '/amharic-words.dat'
        self.word_list = self.loadWords()
        self.word = choice(self.word_list)
    
    def loadWords(self):
        '''
        Reads amharic words from a file source and loads them into a list.
        '''
        try:
            with open(self.fileName, encoding="utf-8") as file:
                content = file.read()
                return content.split()
        except OSError as e:
            raise e

    def getWordOfTheDay(self, size: int = None) -> str:
        return self.word

#api = WordOfTheDay()
#print(api.getWordOfTheDay())
