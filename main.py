import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
usr = input("Enter word: ").upper()

try:
    result = [nato_dict.get(letter) for letter in usr]
except KeyError:
    print("Please input a letter.")
else:
    print(result)
