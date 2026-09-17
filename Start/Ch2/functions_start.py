# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def say_hello():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

say_hello()
# function that takes parameters
def greet(name):
  print("Hello,", name)

greet("Alice")


# function that returns a value
def add(a, b):
  return a + b

result = add(5, 3)
print(result)


# function with default value for an parameter
def greet_with_default(name="Guest"):
  print("Hello,", name)

greet_with_default()
greet_with_default("Bob")


# function with variable number of parameters
def greet_multiple(*names):
  for name in names:
    print("Hello,", name)

greet_multiple("Alice", "Bob", "Charlie")

# function with keyword-only arguments
def greet_with_keywords(*, greeting="Hello", name="Guest"):
  print(greeting, name)

greet_with_keywords()
greet_with_keywords(greeting="Hi", name="Alice")


# function that counts even or odd numbers in a list
def count_numbers(which, numbers):
  if which == "even":
    return sum(1 for n in numbers if n % 2 == 0)
  elif which == "odd":
    return sum(1 for n in numbers if n % 2 != 0)
  return -1

print(count_numbers("even", [1, 2, 3, 4, 5, 6]))
print(count_numbers("odd", [1, 2, 3, 4, 5, 6]))
