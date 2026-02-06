import random

name = input("Type your name: ")
print(f"\nWelcome {name} to this adventure game!")

def play_game():

    health = 100
    print("\nYou are on a dirt road. Go LEFT or RIGHT.")
    answer = input("Choose direction: ").lower()

    if answer in ["left", "l"]:
        choice = input("River ahead. Walk or swim? ").lower()

        if choice in ["swim","s"]:
            print("An alligator attacks you!\n")
            print("You lose!")
        elif choice in ["walk", "w"]:
            print("You safely reach a village. You WIN!")
        else:
            print("Invalid option.")

    elif answer in ["right","r"]:
        choice = input("You see a bridge. Cross or go back (c/b)? ").lower()

        if choice in ["cross","c"]:
            print("You meet a stranger and find treasure. You WIN!")
        else:
            print("You returned home. Game over.")

    else:
        print("Invalid direction.")

# -------- MAIN LOOP --------
while True:
    play_game()

    again = input("\nPlay again? (y/n): ").strip().lower()

    if again in ["y", "yes"]:
        continue
    else:
        print(f'Thanks for playing {name}!')
        break

