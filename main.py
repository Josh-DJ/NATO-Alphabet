import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
flag = False
while flag == False:
    usr = input("Enter word: ").upper()
    if usr.isalpha():
        flag = True
    try:
        result = [nato_dict[letter] for letter in usr]
    except KeyError:
        print("Please input a letter.")
    else:
        print(result)
