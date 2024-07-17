from game_data import data
from art import logo,vs
import random
import os

def play_game():
    print(logo)
    is_ending = False
    score = 0
    random2 = random.choice(data)
    while not is_ending:
        
        random1 = random2
        random2 = random.choice(data)
        while random1 == random2:
            random2 = random.choice(data)
            
        print(f"Compare A: {random1['name']}, a {random1['description']}, from {random1['country']}\n")
        print(f"{vs}\n")
        print(f"Compare B: {random2['name']}, a {random2['description']}, from {random2['country']}\n")
        guess = input("Who has more followers ? A or B ? ").lower()
        if random1['follower_count'] >= random2['follower_count'] and guess == "a":
            os.system('cls')
            score += 1
            print(f"You're right! Current score {score}")
        elif random1['follower_count'] <= random2['follower_count'] and guess == "b":
            os.system('cls')
            score += 1
            print(f"You're right! Current score {score}")            
        else:
            os.system('cls')
            print(f"Sorry, that's wrong. Final score: {score}")
            is_ending = True
            score = 0

again = 'y'
while again == 'y':
    play_game()
    again = input("\nDo you want to play again ? y/n : ")
    os.system('cls')