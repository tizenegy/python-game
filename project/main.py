# Some stuff from CS50

# Strings: Ordered: Yes, Mutable: No
name = "Harry"
print(name[0])
print(name[1])

# Lists: Ordered: Yes, Mutable: Yes
# A Python list allows you to store any variable types.
# We create a list using square brackets and commas, as shown below.
# Similarly to strings,
# we can print an entire list, or some individual elements.
# We can also add elements to a list using append, and sort a list using sort
names = ["Harry", "Ron", "Hermione"]
# Print the entire list: \
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Sort the list:
names.sort()
# Print the new list:
print(names)

# Tuples: Ordered: Yes, Mutable: No
# Tuples are generally used when you need to store just two or three values together,
# such as the x and y values for a point.
# In Python code, we use parentheses:
point = (12.5, 10.6)

# Sets: Ordered: No, Mutable: N/A
# Sets are different from lists and tuples in that they are unordered.
# They are also different because while you can have two or more of the same elements
# within a list/tuple,
# a set will only store each value once.
# We can define an empty set using the set function.
# We can then use add and remove to add and remove elements from that set,
# and the len function to find the set’s size.
# Note that the len function works on all sequences in python.
# Also note that despite adding 4 and 3 to the set twice, each item can only appear once in a set.
# Create an empty set:
s = set()
# Add some elements: s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)
# Remove 2 from the set
s.remove(2)
# Print the set:
print(s)
# Find the size of the set:
print(f"The set has {len(s)} elements.")

# Dictionaries: Ordered: No, Mutable: Yes
# Python Dictionaries or dicts, will be especially useful in this course.
# A dictionary is a set of key-value pairs, where each key has a corresponding value,
# just like in a dictionary, each word (the key) has a corresponding definition (the value).
# In Python, we use curly brackets to contain a dictionary,
# and colons to indicate keys and values. For example:
# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "Gryffindor"
# Print out Hermione's House:
print(houses["Hermione"])


# Functions
def square(x):
    return x * x
# call function:
for i in range(10):
    print(f"The square of {i} is {square(i)}")

# Modules
# As our projects get larger and larger,
# it will become useful to be able to write functions in one file and run them in another.
# In the case above, we could create create one file called
# functions.py
# And call a function in it after importing:
from functions import square_value
for i in range(10):
    print(f"The square of {i} is {square_value(i)}")
