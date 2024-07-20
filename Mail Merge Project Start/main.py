
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.readlines()

# Interesting line for remove the space at the end of every line
# names = [x.replace('\n', '') for x in names]

for name in names:
    name = name.strip()
    letter_template = [x.replace('[name]', name) for x in letter_template]
    message = ''.join(letter_template)
    with open(f"Output/ReadyToSend/letter_{name}.txt", mode="w") as letter:
        letter.write(message)
