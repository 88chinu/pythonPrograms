# #Display user entered name with some statement
# name = input("Enter your name: ")

# print(f"Good afternoon {name} sir") 

# #Print the letter template with given input
# import datetime

# def getdate():
#    date1 = input(datetime.date)
#    return date1

# date = getdate()

# name = input("Enter your name: ")
# letter = '''Dear <|name|>,
# You are selected!
# <|date|> '''
# print(letter.replace("<|name|>","name").replace("<|date|>",date))

#Double space in detecter
string = input("Enter a string: ")

f = string.find("  ")
print(f)
if (f>0):
    print("In the string double space is exist")
else:
    print("In the string double space is not exist")