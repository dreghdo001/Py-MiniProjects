import random
from art import logo
import os
EASY_LIFES = 10
HARD_LIFES = 5

def compare(guessed, random):
    """Comparre the guessed number with the random one, and if they match, the fuction return 0"""
    if guessed > random:
        print("⬆️  Too high ⬆️\n")
        return 1
    elif guessed < random:
        print("⬇️  Too low ⬇️\n")
        return 1
    else:
        print(f"You got it. The answer was {guessed} 🎉🎊🎉🎊🎊🎉 \n")
        return 0

def choose_difficulty():
    """Set the number of lifes that user has considering the difficulty level that we chosed"""
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard: ")
    if difficulty == 'hard':
        lifes = HARD_LIFES
    elif difficulty == 'easy':
        lifes = EASY_LIFES
    else:
        print("Wrong difficulty level entered !!!")
        return 0
    return lifes

def play_game():
    """Engine of the tgame that execute everyhing."""
    print(logo)
    print("I'm thinking of a numbet between 1 and 100")
    lifes = choose_difficulty()

    random_number = random.randint(1,100)
    #print(f"psst, the number is {random_number}")
    is_ending = False   
    while not is_ending:
        print(f"You have {lifes} attempts to guess the number.")
        if lifes == 0:
            print(f"You lost !, the answer was {random_number}")
            break 
        guessed_number = int(input("Make a guess : "))
        result = compare(guessed=guessed_number, random=random_number)
        if result == 0:
            is_ending = True
        else:
            lifes -= 1
            
play = input("Do you want to play Guessing game ? Yes/No :").lower()
while play == 'yes' or play == "y":
    play_game()
    play = input("Do you want to play another game ? Yes/No ? ").lower()
    os.system('cls')

