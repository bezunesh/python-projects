from __future__ import annotations
from rest_framework import viewsets
from rest_framework.response import Response
from .api.resource import WordOfTheDay

class WordOfTheDayView(viewsets.ViewSet):
    """
    Returns a randomly chosen amharic word.
    """
    def list(self, request):
        wordoftheday = WordOfTheDay()
        return Response({ 'word': wordoftheday.getWordOfTheDay()})

    