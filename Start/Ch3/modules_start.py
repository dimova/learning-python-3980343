# LinkedIn Learning Python course by Joe Marini
# Working with modules of code
import math
print(math.sqrt(16))
# import the math module, which contains features for working with mathematics


# import a specific part of the module so you can refer to it more easily
from math import sqrt
print(sqrt(16))


# import a module and give it a different name
import math as m
print(m.sqrt(16))


# the math module contains lots of pre-built functions
print(math.factorial(5))  # Example usage of another math function


# in addition to functions, some modules contain useful constants 
print(math.pi)  # Example usage of a constant from the math module


# Generate a random number between 100 and 200
import random
print(random.randint(100, 200))


# try some of the math functions for yourself here:

# Use the 3rd party tabulate module to print tabulated data:
from tabulate import tabulate
# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
table = tabulate(data, headers="firstrow", tablefmt="grid")
print(table)
