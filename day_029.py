# Docstrings in Python
# Python docstrings are the string literals that appears right after the definition of a function, method, class, or module

def square(n):
    ''' Takes in a number n, returns the square of n'''
    print(n**2)
square(6)  # print square of 6

# we can print docstring (string just after function) by this way:

print(square.__doc__) #print docstrings

# Difference between comment and docstrings:
# comments: comments are descriptions that help programmers better understanding the intent and functionality of the program. They are completely ignored by the Python interpreter
# docstrings: Python docstrings are strings used right after the definition of a function, method, class, or module. they are used to document our code.
