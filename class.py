# class Point:
#     def move(self):
#         print("Moving...")
#     def draw(self):
#         print("Drawing...")
# point1 = Point()
# point1.move()
# point2 = Point()
# point2.draw()
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print(f"Hi! I am {self.name} and I am {self.age} years old")
# john = Person("Jack", 18)
# john.talk()
# bob = Person("Bob", 22)
# bob.talk()
#
# class Mammal:
#     def walk(self):
#         print("walk")
# class Dog(Mammal):
#     pass
# class Cat(Mammal):
#     pass
#
# dog = Dog()
# dog.walk()
# cat = Cat()
# cat.walk()
#
# from dictionary import find_max
# input_list = input("Enter a list of numbers: ")
# num = input_list.split()
# maximum = find_max(num)
# print(f'List is {num}')
# print(f'maximum in list is {maximum}')

# import random
# members = ['john', 'jack', 'ele', 'max']
# print(random.choice(members))


# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
# dice = Dice()
# print(dice.roll())