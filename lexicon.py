__author__ = 'mark'

#A dictionary full of words. Includes a csv parser to generate same.

class Lexicon(dict):
    def __init__(self, parent = None):
        self.parent = parent