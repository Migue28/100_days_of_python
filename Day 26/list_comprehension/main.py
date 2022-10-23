# # List comprehension
# numbers = [1, 2, 3, 4]
# new_numbers = [n+1 for n in numbers]
# odd_numbers = [n for n in numbers if n%2 != 0]
# name = "Eddy"
# new_name_list = [s for s in name]
# range_double = [i for i in range(1,5)]
# range_double = [i*2 for i in range(1,5)]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# name_list = [name.upper() for name in names if len(names) >= 5]
# name_list = [name.upper() for name in names if len(name) >= 5]
# long_name_list = [name.upper() if len(name) > 5 else name for name in names if len(name) >= 5]
# long_name_list = [name.upper() if len(name) > 5 else name for name in names if len(name) < 5]
# long_name_list = [name.upper() if len(name) >= 5 else name for name in names]
#
# # Dictionary Comprehension
# from random import randint
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# names_with_scores = {name: randint for name in names}
# names_with_scores = {name: randint() for name in names}
# passed_students = {key: value for (key, value) in names_with_scores.items() if value > 60}

# Iterate  dataframes
# import pandas as pd

# students_scores = {'Alex': 29, 'Beth': 21, 'Caroline': 19, 'Dave': 69, 'Eleanor': 85, 'Freddie': 71}
# students_names = [name for (name, score) in students_scores.items()]
# students_scores = [score for (name, score) in students_scores.items()]
# students_score = {"student": students_names,
#                   "score": students_scores}
# students_df = pd.DataFrame(students_score)
#
# for (index, row) in students_df.iterrows():
#     print(f"{row.student}: {row.score}")

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
data = {row.letter: row.code for (index, row) in df.iterrows()}

user_word = input("Enter a word: ").upper()
word_list = [data[letter] for letter in user_word]
print(word_list)
