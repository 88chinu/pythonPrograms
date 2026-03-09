#Palindrome Check

def isPalindrome(text):
    text = text.lower()
    reverse = text[::-1]

    if text == reverse:
        return True
    else:
        return False

word = input("Enter a word: ")

if isPalindrome(word):
    print(f"{word} - is a palindrome")
else:
    print(f"{word} - is not a palindrome")