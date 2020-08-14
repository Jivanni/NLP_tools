# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'


# %%
'''
The Automated Readability Index (ARI) is a readability test designed to assess the understandability of a text. Like other popular readability formulas, the ARI formula outputs a number which approximates the grade level needed to comprehend the text. For example, if the ARI outputs the number 10, this equates to a high school student, ages 15-16 years old; a number 3 means students in 3rd grade (ages 8-9 yrs. old) should be able to comprehend the text.
More info: https://readabilityformulas.com/automated-readability-index.php
Use ARI_text_from_corpus if you want to calcluate the ARI from a Nltk corpus object, use ARI_rawtext if the text has not been tokenized.

'''

# %%
import nltk
import re
import nltk.data
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


# %%
def vowelfreq(text):
    fd = nltk.FreqDist(vs for word in text for vs in re.findall(r'[aáeéiíoöóőuűüú]{2,}', word))
    return fd.tabulate()


# %%
def μw_fun(words):
    values = [len(w) for w in words]
    return sum(values)/len(values)


# %%
def μs_fun(sents):
    values = [len(sent) for sent in sents]
    return sum(values)/len(values)


# %%
def ARI_text_from_corpus(corp,text):
    μw = μw_fun(corp.words(text))
    μs = μs_fun(corp.sents(text))
    return 4.71 * μw + 0.5 * μs - 21.43


# %%
def ARI_rawtext(text):
    sents = sent_detector.tokenize(text.strip())
    words = re.findall(r"[\w']+",text)
    μw = μw_fun(words)
    μs = μs_fun(sents)
    return  4.71 * μw + 0.5 * μs - 21.43


# %%
sample = '''
It's The rule of rhythm in prose is not so intricate. Here, too, we write in groups, or phrases, as I prefer to call them, for the prose phrase is greatly longer and is much more nonchalantly uttered than the group in verse. so that not only is there a greater interval of continuous sound between the pauses, but, for that very reason, word is linked more readily to word by a more summary enunciation. Still, the phrase is the strict analogue of the group, and successive phrases, like successive groups, must differ openly in length and rhythm. The rule of scansion in verse is to suggest no measure but the one in hand; in prose, to suggest no measure at all. Prose must be rhythmical, and it may be as much so as you will; but it must not be metrical. It may be anything, but it must not be verse.
'''
ARI_rawtext(sample)