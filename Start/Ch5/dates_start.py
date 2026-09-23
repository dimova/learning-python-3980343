#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
print("Today's date is:", today)


# print out the date's individual components
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("Weekday (0=Monday, 6=Sunday):", today.weekday())

## DATETIME OBJECTS
# Get today's date from the datetime class
now = datetime.now()
print("Current date and time:", now)


# Get the current time
t = now.time()
print("Current time:", t)