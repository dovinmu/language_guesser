import json
from nltk.corpus import udhr
from pandas import DataFrame

df = DataFrame.from_csv('language_speakers', index_col='language')

def exportToJSON(langName, passage):
    l = []
    for sentence in passage:
        l.append(sentence)
    with open("passages/" + langName + ".json", 'w') as f:
        f.write(json.dumps(l))


for lang in udhr.fileids():
    langName = ' '.join(lang.split('-')[:-1])
    try:
        print(' '.join(udhr.sents(lang)[0])[:50] + '...', langName)
        if langName in df.index and df.loc[langName].get('speakers_native(m)') > 1:
            exportToJSON(langName, udhr.sents(lang))
    except AssertionError:
        print('could not print... ', lang)
