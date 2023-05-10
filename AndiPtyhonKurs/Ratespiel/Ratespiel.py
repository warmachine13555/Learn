import random

print("Hello this is a guessing game you need to guess a number between 1 and 100 if it matches you win if not you loose.")

guess = input("Please enter your Guess")

if guess >= "100":
    print("Your number is not in between 1 and 100")
else:
    print(f"You entered {guess}")
