import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through data frame
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

phonetic_word_dict = {letter: phonetic_dict[letter] for letter in word}
phonetic_word_list = [phonetic_dict[letter] for letter in word]
print(phonetic_word_dict)
print(phonetic_word_list)

