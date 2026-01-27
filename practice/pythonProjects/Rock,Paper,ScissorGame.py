import random

choices = ['r','p','s']
user_choice = input("Enter your choice:(r/p/s)").lower()
if user_choice not in choices:
    print("\nInvalid choice. Please try again.")

pc_choice = random.choice(choices)
print("\nThe computer chose is " + pc_choice)
for attempt in range (1, 11):
    if user_choice == pc_choice:
        print("\nYou won!")
        break
    else:
        print("\nYou lost!")