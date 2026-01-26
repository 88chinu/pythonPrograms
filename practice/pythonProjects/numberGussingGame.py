import random

chances = 10
number = random.randint(1, 100)

print("\n🎯 Welcome to the Number Guessing Game!")
print(f"You have {chances} chances to guess the number.\n")

for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == number:
        print(f"🎉 Correct! You guessed the number {number} in {attempt} attempts.")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")

else:
    print(f"\n😢 Out of chances! The correct number was {number}.")
