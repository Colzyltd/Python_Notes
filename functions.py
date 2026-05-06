# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

# In programming, a parameter is a variable in a function's definition (a placeholder), while an argument is the actual value that is passed to the function when it is called.

# Create/Declare a function
def sayHello(name='Tobi'):
    print(f'Hello {name}')


# Function calling/invoking
sayHello('Remi')
sayHello('Joshua')
sayHello('Bolanle')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(10, 5))
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2  

print(getSum(10, 3))
