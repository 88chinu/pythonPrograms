import random

def play_game():
    name = input("\nType your name: ")
    print(f"\nWelcome {name} to this adventure!")

    health = 100
    print("\nYou are on a dirt road. Go LEFT or RIGHT.")
    answer = input("Choose direction: ").lower()

    if answer == "left" or "l":
        choice = input("River ahead. Walk or swim? ").lower()

        if choice == "swim" or "s":
            print("An alligator attacks you!")
            print("You lose!")
        elif choice == "walk" or "w":
            print("You safely reach a village. You WIN!")
        else:
            print("Invalid option.")

    elif answer == "right" or "r":
        choice = input("You see a bridge. Cross or go back (c/b)? ").lower()

        if choice == "c" or "c":
            print("You meet a stranger and find treasure. You WIN!")
        else:
            print("You returned home. Game over.")

    else:
        print("Invalid direction.")

# -------- MAIN LOOP --------
while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again == "no" or "n":
        print("Thanks for playing!")
        break
