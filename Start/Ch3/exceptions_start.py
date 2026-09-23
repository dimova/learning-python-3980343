# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This block always executes, regardless of whether an exception occurred.")
# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("A value error occurred.")
finally:
    print("This block always executes, regardless of whether an exception occurred.")
# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together


# You can also catch specific exceptions

