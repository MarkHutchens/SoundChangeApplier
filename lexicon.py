__author__ = 'mark'

#A dictionary full of words. Includes a csv parser to generate same.
import csv
from SoundChangeApplier.word import *

debug = 1

class Lexicon(dict):
    def __init__(self, parent = None):
        self.parent = parent
        super()

if debug:
    letters = 'ptkbdgaiumnN'
    s = set(letters)

    f = Features('ptkbdgaiumnN') #Will be different by language
    f.add('syllabic','aeiou') #syllable peaks
    #f['sonorant'] = ''
    f.add('consonantal','ptkbdgmnN') #

    f.add('voiced','bdgmnN')
    f.add('labial','pbm')
    f.add('coronal','tdn')
    f.add('dorsal','aeioukgN')
    f.add('nasal','mnN')

    #vowels
    f.add('front','i')
    f.add('back','ua')
    f.add('low','a')


    f.set_valid_places(['labial', 'coronal', 'dorsal'])

if debug:
    w = 'badkubiku'
    p_list = []
    for l in w:
        fone = Phone(f)
        fone.featurize(l)
        p_list.append(fone)

    badabi = Word('nonsense', p_list)
    print(badabi)
    l = Lexicon(None)
    l['pie'] = [badabi,str(badabi)]

