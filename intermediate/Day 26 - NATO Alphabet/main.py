"""
List / Dict / Dataframe comprehension
"""

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for index, row in df.iterrows()}

word = input("Type a word : ")
letters_list = [nato_alphabet[letter.upper()] for letter in word]
print(letters_list)