# Guess the Number Game
import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

number_to_guess = random.randint(1, 10)
attempts = 0
guessed = False

while not guessed:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"🎉 You got it! The number was {number_to_guess}.")
            print(f"It took you {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")
