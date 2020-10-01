# Functional Programming

# In addition to supporting Object-Oriented Programming,
# Python also supports the Functional Programming Paradigm,
# in which functions are treated as values just like any other variable.

# Decorators
# One thing made possible by functional programming is the idea of a decorator,
# which is a higher-order function that can modify another function.
# For example, let’s write a decorator that announces when a function is about to begin,
# and when it ends. We can then apply this decorator using an @ symbol.

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()

# Lambda Functions

# Lambda functions provide another way to create functions in python.
# For example, if we want to define the same square function we did earlier, we can write:
square = lambda x: x * x
# Where the input is to the left of the : and the output is on the right.
# This can be useful when we don’t want to write a whole separate function
# for a single, small use. For example, if we want to sort some objects
# where it’s not clear at first how to sort them.
# Imagine we have a list of people,
# but with names and houses instead of just names that we wish to sort:
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
# people.sort()
# print(people)
# This, however, leaves us with the error:
# Type Error
# Which occurs because Python doesn’t know how to compare two Dictionaries to check
# if one is less than the other.
# We can solve this problem by including a key argument to the sort function,
# which specifies which part of the dictionary we wish to use to sort:
def f(person):
    return person["name"]
people.sort(key=f)
print(people)

# While this does work, we’ve had to write an entire function
# that we’re only using once, we can make our code more readable
# by using a lambda function:
people.sort(key=lambda person: person["name"])
print(people)