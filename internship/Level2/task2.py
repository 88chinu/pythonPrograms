#Number Guessing game random number

import random

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

number = random.randint(start, end)

print("\n🎯 Welcome to the Number Guessing Game!")
print(f"Guess the number between {start} and {end}\n")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(f"🎉 Correct! You guessed the number {number}.")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")