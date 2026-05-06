# A variable is a container that is used to store a value, which can be of various types
# this is a comment

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# DataTypes
x = 1           # int or Integer/whole
# print(x, type(x))

y = 2.5         # float
# print(y, type(y))

name = 'John'   # str
# print(name, type(name))

is_cool = True  # bool
# print(is_cool, type(is_cool))


# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)
# print(x, y, name, is_cool)
name, age, gender = ('john', 23, 'male')
# print(name, age, gender)
# # # Basic math
a = x + y
# print(a)

# # Casting means the conversion or change of value from one datatype to another
x = str(x)
print(x, type(x))
y = int(y)
# print(y, type(y))
# z = float(y)

# print(type(z), z)

age = str(age)
print(age, type(age))