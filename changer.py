__author__ = 'mark'

#class that takes in a dictionary of items, then applies a series of sound changes to them.
#RegEx is super duper important.
import re

class Changer(object):

    def __init__(self, d = {}, rules = [], classes = {}):
        #classes is a list of categories on which we might apply changes.
        #d is a dictionary of terms. Changes are applied to it. Keys are English, values are in lang.
        self.d = d
        self.rules = rules
        self.classes = classes
        pass

    def change(self):
        for i in self.rules:
            for k in self.d.keys():
                self.d[k] = self.d[k].replace(i[0],i[1])

    def set_rules(self, rules):
        self.rules = rules
        pass

    def __str__(self):
        to_return = ''
        for i in self.d.keys():
            to_return += ("'%s' : '%s'\n" % (i, self.d[i]))
        return to_return


'''
Words are spelled with letters. Classes are spelled with some special character preceding.
How to handle digraphs? That is, fricatives and nonsense.

letters exist as a series of attributes.
'''

cls = {}

cls['V'] = ['[aeiou]']

c = Changer()
c.set_rules([['H','W']])
c.d['hello'] = 'hello'
print(c)

c.change()

print(c)