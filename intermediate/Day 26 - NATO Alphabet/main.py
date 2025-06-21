"""
List / Dict / Dataframe comprehension
"""

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for index, row in df.iterrows()}

def generate_phonetic():
    word = input("Type a word : ")
    try:
        letters_list = [nato_alphabet[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(letters_list)

generate_phonetic()