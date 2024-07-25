#Step 1
import random
from hangman_words import word_list
from logo import stages,logo
import os

chosen_word = random.choice(word_list)
#chosen_word = "baboon"
right = 0
print(f"{logo} \n")

word_length = len(chosen_word)
# Create the empty word
display = []
fails = len(stages) - 1
for _ in range(word_length):
    display.append("_")

print(f"\n {stages[len(stages) - 1]} \n ")

print(" ".join(display))

while "".join(display) != chosen_word:
    guess  = input("\nLetter : ").lower()
    os.system('cls')
    attempt = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            attempt = True
            display[position] = letter
    if not attempt:
        fails -=1
        print(f"\n {stages[fails]}\n")
    if fails == 0:
        print(f"\nYou lose :(\n The word was {chosen_word}")
        break

    print(" ".join(display))

if "".join(display) == chosen_word:
    print("\nCongrats...you won !\n")

print()