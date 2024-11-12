# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']
print(b)


# Mixed data types
c = [1, 'hello', 3.14,'quava','chinmaya', 7878, 5354, True]

# string type
d = 'chinmaya'
# d[7] = 'e'  (TypeError: 'str' object does not support item assignment) character of a string never change in list

b[0] = 'quava'
e = b # objects of a list can be change
print(a)
print(c)
print(c[0:4])
print(d)
print(d[7])
print(e)