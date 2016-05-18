# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES
import string
import re


def detect_language(text, languages):
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub('',text)     #remove punctuation in string
    text = text.lower()
    ls = text.split()                                                           #returns list of words in text
    word_counts = {}                                                            #dict will hold {word:frequency in text}
    total = {}                                                                  #dict will hold {language:total common words that appear}
    for word in ls:                                                             #iterate over words from text
        word_counts[word] = word_counts.get(word,0) + 1                         #return current count of word if exists or 0 if it has not beed added yet, then increment by 1
    for d in languages:                                                         #iterate over dictionaries 
        count = 0                                                               #count tallies total number of common word occurences for langauge
        for key,value in word_counts.items():                                   #iterate over word:frequency pairs in dict of words in text
            if key in d["common_words"]:                                        #if word is a common word, 
                count += value                                                  #   increment count by word frequency in text and
                total[d["name"]] = count                                        #   add or update {language:total commmon words}
    return max(total, key=total.get)                                            #return language with greatest common word total
