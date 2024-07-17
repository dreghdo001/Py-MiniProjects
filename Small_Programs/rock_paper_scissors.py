import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def numToChoise(num):
    your_choise = "Wrong choise !"
    match num:
        case "0":
            your_choise = rock
        case "1":
            your_choise = paper
        case "2": 
            your_choise = scissors
    return your_choise

#Write your code below this line 👇
your_choise = (input("Make your choise wisely ! \n"))
computer_choise = str(random.randint(0,2))

print(f"Your choise : \n {numToChoise(your_choise)} \n Computer chose \n {numToChoise(computer_choise)}")

if numToChoise(your_choise) == rock and numToChoise(computer_choise) == paper:
    print ("You lose !")
elif numToChoise(your_choise) == rock and numToChoise(computer_choise) == rock:
    print ("Tie !")
elif numToChoise(your_choise) == rock and numToChoise(computer_choise) == scissors:
    print ("You win !")
    
elif numToChoise(your_choise) == paper and numToChoise(computer_choise) == paper:
    print ("Tie!")
elif numToChoise(your_choise) == paper and numToChoise(computer_choise) == rock:
    print ("You win !")
elif numToChoise(your_choise) == paper and numToChoise(computer_choise) == scissors:
    print ("You lose !")

elif numToChoise(your_choise) == scissors and numToChoise(computer_choise) == paper:
    print ("You win !")
elif numToChoise(your_choise) == scissors and numToChoise(computer_choise) == rock:
    print ("You lose !")
elif numToChoise(your_choise) == scissors and numToChoise(computer_choise) == scissors:
    print ("Tie !")









