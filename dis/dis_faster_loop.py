#!/usr/bin/env python3
# encoding: utf-8

import string


class Dictionary:

    def __init__(self, words):
        self.by_letter = {
            letter: []
            for letter in string.ascii_letters
        }
        self.load_data(words)

    def load_data(self, words):
        for word in words:
            self.by_letter[word[0]].append(word)
