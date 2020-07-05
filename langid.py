# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import nltk
from nltk.corpus import udhr
import re


# %%
Latin1_langs = [lang for lang in udhr.fileids() if re.search(r"Latin1",lang)]


# %%
def languages_freq(langlist, input_text):
    fdistinput = nltk.FreqDist(input_text)
    result = []
    for language in Latin1_langs:
        Lang_freqdist = nltk.FreqDist(udhr.words(language))
        result.append([language,nltk.spearman_correlation(Lang_freqdist,fdistinput)])
    return result


# %%
def mostprobable(final):
    return sorted(final, key = lambda x : x[1], reverse = True)


# %%
def lang_id(text):
    input_text = nltk.word_tokenize(text)
    final = languages_freq(Latin1_langs,input_text)
    return re.search(r"\w+",str(mostprobable(final)[0][0]))[0]


# %%
if __name__ == '__main__':
    test = "L'idea interna dell'Esperanto è: sulla base di una lingua neutrale si possono abbattere i muri tra le popolazioni e avvicinare le persone, in modo che possano vedere nel proprio prossimo una persona e un fratello."
    print(lang_id(test))

