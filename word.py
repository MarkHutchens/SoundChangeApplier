__author__ = 'mark'

#Important.
from phones import*

debug = 1

if debug:
    f = Features('ptkbdgaiumnN') #Will be different by language
    f['syllabic'] = 'aeiou'
    f['consonant'] = 'ptkbdgmnN'
    f['voiced'] = 'bdgmnN'
    f['labial'] = 'pbm'
    f['coronal'] = 'tdn'
    f['dorsal'] = 'aeioukgN'
    f['nasal'] = 'mnN'

    #vowels
    f['front'] = 'i'
    f['back'] = 'ua'
    f['low'] = 'a'


    f.set_valid_places(['labial', 'coronal', 'dorsal'])

class Syl():
    def __init__(self):
        #lists of phonemes
        self.onset = []
        self.morae = []

    def is_long(self):
        #Will vary by language how this is determined
        return (len(self.morae) > 1)

    def add_onset(self, on):

        if len(self.onset) == 0:    #No complex onsets
            self.onset.append(on)
            return 1
        else:
            return 0

    def add_mora(self, vow):
        if len(self.morae) == 0:    #No complex nuclei/codas, only single vowels allowed.
            self.morae.append(vow)
            return 1
        else:
            return 0

    def __str__(self):
        to_return = ''
        for o in self.onset:
            to_return += str(o)
        for m in self.morae:
            to_return += str(m)
        return to_return


class Word():
    #A list of phones that will have all sorts of fun goodies attached to it.
    def __init__(self, gloss, phones):
        self.gloss = gloss
        self.phones = phones    #list of phone types.
        self.syllables = self.syllabilize()

    def set_phones(self, syls):
        self.syllables = syls
        self.syllabilize()

    def syllabilize(self):
        #Make syllables from a list of phones. Will vary by language.
        last_vow = None
        syl_list = []
        cur_syl = Syl()
        for p in self.phones[::-1]:
            if p['syllabic']:
                if(cur_syl.add_mora(p)):
                    last_vow = p
                    pass
                else:
                    syl_list.append(cur_syl)
                    cur_syl = Syl()
                    cur_syl.add_mora(p)
                    last_vow = p
                    pass
            else:
                if(cur_syl.add_onset(p)):
                    pass
                else:
                    syl_list.append(cur_syl)
                    cur_syl = Syl()
                    #Make a placeholder vowel, assimilating the next vowel's attributes.
                    cur_syl.add_mora(last_vow)
                    cur_syl.add_onset(p)
                    pass
        syl_list.append(cur_syl)
        return syl_list


    def __str__(self):
        to_return = ''
        for s in self.syllables[::-1]:
            to_return += str(s) + '.'
        return(to_return)




if debug:
    w = 'badkubiku'
    p_list = []
    for l in w:
        fone = Phone(f)
        fone.featurize(l)
        p_list.append(fone)

    badabi = Word('nonsense', p_list)
    print(badabi)