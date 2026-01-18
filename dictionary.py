# customer = {
#     "name": "John Wick",
#     "age": 42,
#     "city": "New York",
#     "kill_count": 162
# }
# customer["name"] = "BabaYaga"
# print(customer.get("city"))
# print(customer)

# phone = input("Phone_No: ")
# digits = { "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
#            "6": "six", "7": "seven", "8": "eight", "9": "nine","0": "zero"}
# for char in phone:
#     if char in digits:
#         print(digits[char],end=" ")
#     else:
#         print(" ? ",end=" ")

# mes = input("Enter your message: ")
# words = mes.split(" ")
# emojis = {
#     ":)": "😊",
#     ":(": "😔",
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# def find_max(num):
#     max_n = num[0]
#     for i in num:
#         if i > max_n:
#             max_n = i
#     return max_n
# num = [8, 9, 6, 12, 10]
# maximum = find_max(num)
# print(maximum)