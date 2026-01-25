import random

print("Welcome to the Dice Game!")
count = 0

while True:
    choice = input("Roll dice? (y/n): ")

    if choice == 'y':
        n = int(input("How many dice? "))
        count += 1

        if n < 1:
            print("Please enter a positive number.")
            continue

        for i in range(n):
            print(random.randint(1, 6), end=" ")

        print("\nTotal rolls:", count)

    elif choice == 'n':
        print("Thanks for playing!")
        print(f"You rolled the dice {count} times")
        break

    else:
        print("Invalid choice")
