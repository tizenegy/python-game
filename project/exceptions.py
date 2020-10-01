# Exceptions
# During this lecture, we’ve run into a few different exceptions,
# so now we’ll look into some new ways of dealing with them.
# In the following chunk of code, we’ll take two integers from the user,
# and attempt to divide them:
x = int(input("x: "))
y = int(input("y: "))
result = x / y
print(f"{x} / {y} = {result}")

# In many cases, this program works well.
# However, we’ll run into problems when we attempt to divide by 0.
# We can deal with this messy error using Exception Handling.
# In the following block of code, we will try to divide the two numbers,
# except when we get a ZeroDivisionError:
import sys
x = int(input("x: "))
y = int(input("y: "))
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)
print(f"{x} / {y} = {result}")

# However, we still run into an error when the user enters non-numbers for x and y.
# We can solve this problem in a similar manner!
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program     sys.exit(1)
print(f"{x} / {y} = {result}")
