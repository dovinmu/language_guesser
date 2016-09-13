import time
import math
import random
import os
import json
from difflib import SequenceMatcher

class LanguageGuesser:
    def __init__(self):
        self.score = 900
        self.families = set()

        self.unprintables = []
        self.languages = {}

        for fname in os.listdir('passages'):
            with open('passages/' + fname, 'r') as f:
                self.languages[fname[:-5]] = json.loads(f.read())

    def getNextLanguage(self):
        lang = random.choice(list(self.languages.keys()))
        langName = lang.split('_')[0]
        return langName, self.languages[lang]

    def verifyGuess(self, langName, guess):
        return langName == guess

    def guessLanguage(self):
        lang = random.choice(list(self.languages.keys()))
        lang_print = lang.split('_')[0]
        guess = ''
        sent_idx = 0
        print('Guess the language (hit enter to see more, or guess the language family):\n')
        while guess == '':
            print(' '.join(self.languages[lang][sent_idx])[:300])
            guess = input('')
            sent_idx = (sent_idx + 1) % len(self.languages[lang])
        if guess in lang:
            print('Correct! {}\n+{} speakers to score!'.format(lang.replace('_',' / '), self.df.loc[lang].get('speakers_native(m)')))
            self.score += self.df.loc[lang].get('speakers_native(m)')
            if type('') == type(self.df.loc[lang].family):
                families.add(self.df.loc[lang].family)
            if self.score > 1000:
                print('current score: {}b'.format(int(self.score/10)/100))
            else:
                print('current score: {}m'.format(self.score))
            print('families collected:', ', '.join(sorted(list(families))))
        else:
            close = False
            if guess == self.df.loc[lang].family:
                close = True
                print('Yup! The specific language is {}.'.format(lang_print))
                if type('') == type(self.df.loc[lang].family):
                    families.add(self.df.loc[lang].family)
                if score > 1000:
                    print('current score: {}b'.format(int(self.score/10)/100))
                else:
                    print('current score: {}m'.format(self.score))
                print('families collected:', ', '.join(sorted(list(families))))
            else:
                for idx in self.df.index:
                    if guess in idx and self.df.loc[idx].family == self.df.loc[lang].family:
                        print('Close! {} and {} are both {} languages.'.format(guess, lang_print, self.df.loc[lang].family))
                        close = True
                        break
            if not close:
                print('Incorrect. Answer: {}\nnative speakers: \t{}\nfamily: \t\t{}'.format(lang_print, self.df.loc[lang].get('speakers_native(m)'), self.df.loc[lang].family))
        input('')
        print('_'*80 + '\n')

if __name__ == "__main__":
    game = LanguageGuesser()
    print('\n'*5)
    while True:
        langName, passage = game.getNextLanguage()
        print(' '.join(passage[0]), '\n' * 5, "Guess the language:")
        if game.verifyGuess(langName, input('')):
            print("correct!")
        else:
            print("incorrect!")
        print(langName)
        input('')
        #game.guessLanguage()
