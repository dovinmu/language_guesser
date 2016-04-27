from nltk.corpus import udhr
import time
import math
import random
from pandas import DataFrame
from difflib import SequenceMatcher

df = DataFrame.from_csv('language_speakers', index_col='language')

score = 0
families = set()

unprintables = []
languages = {}
for lang in udhr.fileids():
    lang_name = ' '.join(lang.split('-')[:-1])
    try:
        print(' '.join(udhr.sents(lang)[0])[:50] + '...', lang_name)
        if lang_name in df.index and df.loc[lang_name].get('speakers_native(m)') > 1:
            languages[lang_name] = udhr.sents(lang)
    except:
        print('could not print... ', lang + ':\t')
        unprintables.append(lang)
    time.sleep(.005)
'''
I know: Vietnamese

Close: Swedish (guessed Icelandic), Hungarian (Romanian), Bulgarian (Russian),

I don't know: Tenek_Huasteco, Bosnian_Bosanski, WesternSotho_Tswana Setswana, Lingala, Themne_Temne, Sussu_Soussou Soso Susu, Chamorro, Tojo abal, Hausteco, Rhaeto Romance_Rumantsch, HaitianCreole_Popular, Ido, Qechi_Kekchi, Abkhaz, Baoule, Shipibo Conibo

'''
def guessLanguage():
    global score
    lang = random.choice(list(languages.keys()))
    lang_print = lang.split('_')[0]
    guess = ''
    sent_idx = 0
    print('Guess the language (hit enter to see more, or guess the language family):\n')
    while guess == '':
        print(' '.join(languages[lang][sent_idx])[:300])
        guess = input('')
        sent_idx = (sent_idx + 1) % len(languages[lang])
    if guess in lang:
        print('Correct! {}\n+{} speakers to score!'.format(lang.replace('_',' / '), df.loc[lang].get('speakers_native(m)')))
        score += df.loc[lang].get('speakers_native(m)')
        if type('') == type(df.loc[lang].family):
            families.add(df.loc[lang].family)
        print('current score: {}m'.format(score))
        print('families collected:', ', '.join(sorted(list(families))))
    else:
        close = False
        if guess == df.loc[lang].family:
            close = True
            print('Yup! The specific language is {}.'.format(lang_print))
            if type('') == type(df.loc[lang].family):
                families.add(df.loc[lang].family)
            print('current score: {}m'.format(score))
            print('families collected:', ', '.join(sorted(list(families))))
        else:
            for idx in df.index:
                if guess in idx and df.loc[idx].family == df.loc[lang].family:
                    print('Close! {} and {} are both {} languages.'.format(guess, lang_print, df.loc[lang].family))
                    close = True
                    break
        if not close:
            print('Incorrect. Answer: {}\nnative speakers: \t{}\nfamily: \t\t{}'.format(lang_print, df.loc[lang].get('speakers_native(m)'), df.loc[lang].family))
    input('')
    print('_'*80 + '\n')

print('\n'*5)
while True:
    guessLanguage()
#print('\nCould not print the following:', ', '.join(unprintables))
