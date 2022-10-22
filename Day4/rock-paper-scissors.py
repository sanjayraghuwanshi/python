"""
Make a rock, paper, scissors game.
Start the game by asking the player:"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
Rock wins against scissors | Scissors win against paper | Paper wins against rock.
"""
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

user = int(input('"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."\n'))
list = [rock, paper, scissors]
if user >=3:
    print("Please provide a valid value")
else:
    print(list[user])

    random_integer = random.randint(0, 2)

    print(f"computer chose:\n" + list[random_integer])

    if user == random_integer:
        print("Its a tie, play again")
    elif (user == 0 and random_integer == 1) or (user == 0 and random_integer == 2):
        print("You won")
    elif user == 1 and random_integer == 0:
        print("You won")
    elif (user == 1 and random_integer == 2):
        print("You lose")
    elif user == 2 and random_integer == 0:
        print("You lose")
    elif user == 2 and random_integer == 1:
        print("You Won")