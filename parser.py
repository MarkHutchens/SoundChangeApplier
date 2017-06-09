__author__ = 'mark'

#Reads csv files of phones, like phonelist.csv
import csv
from SoundChangeApplier.phones import Features


class Parser():
    def __init__(self):
        self.letters = None
        pass

    def sublist(self, l):
        toreturn = ''
        for i in range(len(self.letters)):
            if l[i+1] == '1':
                toreturn += self.letters[i]

        return toreturn

    def parse(self, filename):
        f = open(filename, 'r', encoding= 'utf-16')
        file = csv.reader(f)

        c = 0
        for l in file:
            if c == 0:
                self.letters = l[0] #top left corner holds the list of letters
                feats = Features(self.letters)
                c = 1
            else:
                feats.add(l[0],self.sublist(l))

        return feats