# print('Chinmaya')
# print('*'*10)
from turtledemo.penrose import start

# name = input("enter name: ")
# print("Hii " + name)

# yob = input("dob: ")
# age = 2026 - int(yob)
# print(age)
# print(type(age))

# pounds = input("Enter weight in pounds: ")
# kg = float(pounds) * 0.45
# print(pounds + "p in kg is "+ str(kg)+"kg")

# first = 'John'
# sec = 'Wick'
# msg = first + ' { ' + sec + ' } is a shooter'
# formated_string = f'{first} [{sec}] is a shooter'
# print(formated_string)
# print(msg)

# is_hot  = False
# is_cold = True
# if is_hot:
#     print("It's a hot day.")
#     print("Enjoy your day")
# elif is_cold:
#     print("It's not a cold day.")
#     print("Enjoy your day.")
# else:
#     print("It's a lovely day.")
# print("Drink plenty Water.")

# house = 1000000
# user_input = input("Do you have good credit ? (y/n):").strip().lower()
# good_credit = user_input == "y"
# if good_credit:
#     payment = house * 0.1
# else:
#     payment = house * 0.02
# print(f"Down payment is: ${payment}")

# w = int(input('Weights: '))
# u = input('(L)bs or (k)g: ')
# if u.upper() == 'L':
#     converted = w * 0.45
#     print(f"Your weight is {converted:.2f} kilograms")
# else:
#     converted = w / 0.45
#     print(f"Your weight is {converted:.2f} pounds")

# i = 1
# while i <= 6:
#     print('*' * i)
#     i = i + 1

# from random import randint
# secret_num = randint(10, 50)
# guess_count = 0
# guess_limit = 8
# while guess_count < guess_limit:
#     guess = int(input("Guess a number between 10 and 50: "))
#     guess_count += 1
#     if guess == secret_num:
#         print("Congratulations! You guessed it!")
#         break
# else:
#     print("Sorry, you didn't guess correctly.")

# print("Enter command for engine:")
# started = False
# while True:
#     for_car = input("> ").lower()
#
#     if for_car == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("The engine is starting...")
#     elif for_car == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("The engine is stopping...")
#     elif for_car == "help":
#         print("""
# start - The engine is starting...
# stop - The engine is stopping...
# quit  - Shut down the engine...""")
#     elif for_car == "quit":
#         print("The engine is in Rest mode...")
#         break
#     else:
#         print("Unknown command")
