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

    #Labial block
    f.add('round','úóow')
    f.add('labial',f['round'][1] | {'Ppbmfv'}) #w is both labial and dorsal


    #Dorsal block
    f.add('back','úóoiuáNkKghw')
    f.add('high','íiúNkKghw')
    f.add('low','aáo')
    f.add('dorsal',f['back'][1] | f['high'][1] | f['low'][1] | {'é'})

    f.add('ATR','íéiaáúóo')

    #Coronal block
    f.add('distributed','Ttdnszl')
    f.add('anterior','')
    f.add('coronal',f['distributed'][1] | f['anterior'][1] | {''}) #No distinctions yet made between distributed/anterior


    #Laryngeal
    f.add('voice','íéaiuáúóomnNbdgvzwly')
    f.add('aspiration','')
    f.add('glottalized','PTK')


    #Manner (Finally stops v fricatives, yo)
    f.add('continuant','íéaiuáúóofshvzwly')
    f.add('lateral','l')
    f.add('strident','sz')

    #Nasal/Oral
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
    w = 'mínéNapitukáPúTóKobidigifisihiviziwiliy'
    #w = 'piti'
    p_list = []
    for l in w:
        fone = Phone(f)
        fone.featurize(l)
        p_list.append(fone)
        #fone.print_features()

    badabi = Word('nonsense', p_list)
    print(badabi)
    l = Lexicon(None)
    l['pie'] = [badabi,str(badabi)]

