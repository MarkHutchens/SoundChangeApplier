__author__ = 'mark'

import re

debug = 0

class Features(dict):
    #Has a dictionary. Dictionary holds sets.
    def __init__(self, letters):
        self.letters = set(letters)
        self.__valid_places = None

    def get_letters(self):
        return self.letters.copy()

    def set_letters(self, l):
        self.letters = {l}

    def get_valid_places(self):
        return self.__valid_places

    def set_valid_places(self, places: list):
        self.__valid_places = places
        
    def add(self,feature,lets):
        #add two sets at once. One that does contain, one that doesn't.
        self[feature] = [self.letters.difference(lets), set(lets)]


#Words exist as a series of phonemes. Phonemes have a set of phonological features.
class Phone(dict):
    def __init__(self, features: Features):
        self._features = features  #subclasses (for different langs) would have different relevant features
        self._place = None

    def featurize(self, letter):
        for i in self._features.keys():
            self[i] = letter in self._features[i][1] #Boolean t/f
            if i in self._features.get_valid_places() and self[i]:
                self._place = i


    def letterize(self):
        letter = self._features.get_letters() #start as a list of all possible letters
        #Rewritten for sets instead of strings.

        for i in self._features.keys():
            if self[i]:
                letter = letter.difference(self._features[i][0])
            else:
                letter = letter.difference(self._features[i][1])

            #print(letter)

        if len(letter) > 1:
            pass

        return(next(iter(letter)))  #How to get the item from a set

        '''
        for i in self._features.keys():
            before = letter
            if(self[i]):
                add = '+'
                pattern = '[^' + self._features[i][1] + ']'
            else:
                add = '-'
                pattern = '[' + self._features[i][1] + ']'
            letter = re.sub('%s' % pattern, '', letter)
            #print(i, before, add, self._features[i][1], '=', letter )
'''


    def set_place(self, place):
        for i in self._features.get_valid_places():
            self[i] = False
        self._place = place
        self[self._place] = True

    def get_place(self):
        return self._place

    def set_att(self, at, boo):
        self[at] = boo

    def assimilate(self, other, feature):
        if type(other) == str:
            new_phone = Phone(self._features)
            new_phone.featurize(other)
            other = new_phone
            print(other.get_place())
        if feature == 'place':
            #Place is the only one that acts in a mutually exclusive way, so this is okay.
            self.set_place(other.get_place())
        else:
            self[feature] = other[feature]

    def __str__(self):
        to_return = ''
        for i in sorted(self.items()):
            if i[1] and debug:
                to_return += '%s, ' % (i[0])
        to_return += self.letterize()
        return(to_return)