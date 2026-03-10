#Password checker

import string

def checkPassword(pas):
    length = len(pas) >= 8
    upper = any(c.isupper() for c in pas)
    lower = any(c.islower() for c in pas)
    digit = any(c.isdigit() for c in pas)
    special = any(c in string.punctuation for c in pas)

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Strong Password 💪"
    elif score >= 3:
        return "Medium Password ⚠️"
    else:
        return "Weak Password ❌"

password = input("Enter your password: ")

result = checkPassword(password)

print("Password Strength:", result)