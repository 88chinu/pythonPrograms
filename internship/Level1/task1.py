#String Reversal

def reverse(string):
    result = ""
    for char in string:
        result = char + result
    return result

s = input("Enter a string: ")
print("Reversed String is: " + reverse(s))