# Display user entered name with some statement
name = input("Enter your name: ")

print(f"Good afternoon {name} sir") 

# Print the letter template with given input
import datetime

def getdate():
 date1 = input(datetime.date)
 return date1

date = getdate()

name = input("Enter your name: ")
letter = '''Dear <|name|>,
You are selected!
<|date|> '''
print(letter.replace("<|name|>","name").replace("<|date|>",date))

# Double space in detecter
string = input("Enter a string: ")

f = string.find("  ")

if (f>0):
    print("In the string double space is exist")
else:
    print("In the string double space is not exist")

print(string)

# Replace the double space with single space

string = input("Enter a string: ")

print(string.replace("  "," "))

print(string)

# Add escape sequence characters in a string

letter = "Hello! Chinmaya \n\tWell-come to Python Program \n \t Have a nice Day."

print(letter)