#Leaning Python
print ('Hello', 'world')

#Print using variable
w = 10
x = 5
Y = "John"
z = 8.765
print(x+w)
print(type(x+w))
print(type(x))
print(type(Y))
print(type(z))

#use of if statement
if (x<z):
  print("z is greater than x") 


#Object statement
fruits = ["apple", "banana", "orange"] 
f = ("apple", "banana", "orange")
a, b, c = fruits
print(a)
print(b)
print(c)
print(type(fruits))
print(type(f))

#Global variable
q = "awesome"  
def myfunc():
    global p
    p = "fantastic"
myfunc()

print("Python is " + p)
print("Python is " + q + " and " + p)

#Complex datatype
real = 3
imaginary = 5


z = complex(real, imaginary)
print("The complex number is ", z)