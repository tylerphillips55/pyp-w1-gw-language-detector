# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES
import string
import re


def detect_language(text, languages):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    ls = regex.sub('',text).split()
    word_counts = {}
    freq = {}
    for word in ls:
        word_counts[word] = word_counts.get(word,0) + 1
    for dict in languages:
        count = 0
        for key,value in word_counts.items():
            if key in dict["common_words"]:
                count += value
                freq[dict["name"]] = count
    return max(freq, key=freq.get)
