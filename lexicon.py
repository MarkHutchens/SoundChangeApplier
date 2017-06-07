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
    letters = 'íéaiuáúóomnNptkPTKbdgfshvzwly'
    #s = set(letters)

    f = Features(letters) #Will be different by language
    f.add('syllabic','íéaiuáúóo') #syllable peaks
    #f['sonorant'] = ''
    f.add('consonantal','mnNptkPTKbdgfshvz') #w/l/y are neither.

    #Dorsal block
    f.add('back','úóoiuáNkKghw')
    f.add('front','íéay')
    f.add('high','íiúNkKghw')
    f.add('low','aáo')


    f.add('voice','íéaiuáúóomnNbdgvzwly')
    f.add('labial','pbmúóow') #w is both labial and dorsal
    f.add('coronal','tdn')
    f.add('dorsal',f['back'][1] | f['front'][1])
    f.add('nasal','mnN')

    #vowels
    #f.add('front','i')
    #f.add('back','ua')
    #f.add('low','a')


    f.set_valid_places(['labial', 'coronal', 'dorsal', 'pharyngeal', 'placeless'])

    f.set_digraph("K","k'")
    f.set_digraph("P","p'")
    f.set_digraph("T","t'")
    f.set_digraph("N","ng'")

if debug:
    w = 'badkubéku'
    p_list = []
    for l in w:
        fone = Phone(f)
        fone.featurize(l)
        p_list.append(fone)

    badabi = Word('nonsense', p_list)
    print(badabi)
    l = Lexicon(None)
    l['pie'] = [badabi,str(badabi)]

