import random

# list of the variants
variants = ['scissors', 'paper', 'rock']

# get random from the list of the variants
randomChoice = random.choice(variants)

# user variant in the lower case
userChoice = str.lower(input('Pls, Choose and print: scissors, paper or rock: \n'))

# if user input was correct
if userChoice in variants:

    # if draw = enough, next variants
    if userChoice == randomChoice:
        print("Draw! Pls, start again for next try ")

    if userChoice == "scissors" and randomChoice == "rock":
        print("You loose, start and try again")

    if userChoice == "scissors" and randomChoice == "paper":
        print("You Win!")

    if userChoice == "paper" and randomChoice == "rock":
        print("You win")

    if userChoice == "paper" and randomChoice == "scissors":
        print("You loose, start and try again")

    if userChoice == "rock" and randomChoice == "paper":
        print("You loose, start and try again")

    if userChoice == "rock" and randomChoice == "scissors":
        print("You win")

else:
    # if user input is bad statement
    print("Pls, print correct variant next time")

# print random variant
print(f"The choice of the game was : {randomChoice}")


