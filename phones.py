__author__ = 'mark'

import re

debug = 0

class Features(dict):
    #Has a dictionary. Dictionary holds sets.
    def __init__(self, letters):
        self.letters = set(letters)
        self.__valid_places = None
        self.s_replace = [] #For converting phones to digraphs


    def get_letters(self):
        return self.letters.copy()

    def set_letters(self, l):
        self.letters = {l}

    def get_valid_places(self):
        return self.__valid_places

    def set_valid_places(self, places: list):
        self.__valid_places = places

    def set_digraph(self,s,replace):
        self.s_replace.append([s,replace])
        
    def add(self,feature,lets):
        #add two sets at once. One that does contain, one that doesn't.
        self[feature] = [self.letters.difference(lets), set(lets)]


#Words exist as a series of phonemes. Phonemes have a set of phonological features.
class Phone(dict):
    def __init__(self, features: Features):
        self._features = features  #subclasses (for different langs) would have different relevant features
        #self._place = None
        #Consonant place and vowel place w has both, for instance. Neato.
        self._vplace = None #Vowel place
        self._cplace = None #[None,self._vplace] #default to none.

        self._laryngeeal = {'voice': None,'aspiration': None,'glottalized': None} #[voice, aspiration, glottalization]


    def featurize(self, letter):
        syl = 'syllabic' in self
        for i in self._features.keys():
            self[i] = letter in self._features[i][1] #Boolean t/f

            if i in self._features.get_valid_places() and self[i]:
                self._cplace = [i,self._vplace]
                if syl:
                    if self['syllabic']:
                        #If a vowel/semivowel, also get a vplace.
                        self._vplace = i

            if i in self._laryngeeal.keys():
                self._laryngeeal[i] = self[i]


    def update(self):
        #Make sure nodes of place and laryng match true/false tags
        for i in self._laryngeeal.keys():
            self[i] = self._laryngeeal[i]
        if i in self._features.get_valid_places():
            self[i] = i in self._cplace




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
            print("Conflict: two phones have same description")
            print(letter)
            self.print_features()
            pass

        return(next(iter(letter)))  #How to get the item from a set


    def set_place(self, cplace, vplace = None):
        for i in self._features.get_valid_places():
            self[i] = False
        self._vplace = vplace
        self._cplace = [cplace,self._vplace]
        self[self._cplace] = True
        if self._vplace:
            self[self._vplace] = True

    def get_place(self):
        return self._cplace

    def set_att(self, at, boo):
        self[at] = boo

    def assimilate(self, other, feature):
        if type(other) == str:
            new_phone = Phone(self._features)
            new_phone.featurize(other)
            other = new_phone
            print(other.get_place())
        if feature == 'cplace':
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

        for rep in self._features.s_replace:
            to_return = to_return.replace(rep[0],rep[1])
        return(to_return)

    def print_features(self):
        #print(self)
        for i in self._features:
            print('  ' + i + ':' + str(self[i]))