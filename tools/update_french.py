# -*- coding: utf-8 -*-

from word import Word
import os

path = 'content/patois/'
words = []
errors = []
for directory in os.listdir(path):
    for file in os.listdir(f"{path}/{directory}"):
        w = Word.from_file( f"{path}/{directory}/{file}" )
        results, error = w.to_french()
        words +=  results 
        errors += error
for w in words:
    w.set_path()
    w.save_or_update()

