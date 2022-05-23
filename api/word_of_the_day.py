"""
A REST API that provides a randomly choosen word of the day in amharic

 - Endpoints:
    1. GET domain.com/api/wordoftheday
    2. GET domain.com/api/wordoftheday?size=6
 - Response: Json format 
    {
     'word' : 'ሃይ'
    }

    # size=4
    {
        'word': 'መጽሐፍ'
    }
- No authentication, no token or key required, public API
"""
from __future__ import annotations
from random import choice
import json

class WordOfTheDay:
    '''
    WordOfTheDay
    '''
    def __init__(self):
        self.fileName = 'amharic-words.dat'
        self.word_list = self.loadWords()
        self.word = choice(self.word_list)
    
    def loadWords(self):
        '''
        Reads amharic words from a file source and loads them into a list.
        '''
        try:
            with open(self.fileName) as file:
                content = file.read()
                ## when do we need to decode
                #content_str = content_byte.decode("utf-8")
                return content.split()
        except OSError as e:
            raise e

    def getWordOfTheDay(self, size: int = None) -> str:
        # don't escape unicode characters
        response = json.dumps(self.word, ensure_ascii=False)
        return response

    # How do you make a REST API
    # has reachable endpoint - url
    # able to accept http request
    # parse request
    # return a response
if __name__ == '__main__':
    api = WordOfTheDay()
    print(api.getWordOfTheDay())
