# -*- coding: utf-8 -*-

from word import Word
import os

if __name__ == '__main__':
    path = 'content/patois/'
    words = []
    errors = []
    for directory in os.listdir(path):
        for file in os.listdir(f"{path}/{directory}"):
            print( f"Reading {path}/{directory}/{file}" )
            w = Word.from_file( f"{path}/{directory}/{file}" )
            results, error = w.to_french()
            words +=  results 
            errors += error
    for w in words:
        w.set_path()
        w.save_or_update()

