import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through data frame
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def nato_convertor():
    word = input("Enter a word: ").upper()
    try:
        phonetic_word_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet allowed !")
        nato_convertor()
    else:
        print(phonetic_word_list)


nato_convertor()
