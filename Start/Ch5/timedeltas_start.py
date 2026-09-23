#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today's date is:", now)

# print today's date one year from now
print("One year from now will be:", now + timedelta(days=365))


# create a timedelta that uses more than one argument
delta = timedelta(days=2, hours=3, minutes=30)
print("A timedelta of 2 days, 3 hours, and 30 minutes:", delta)


# calculate the date 1 week ago, formatted as a string
one_week_ago = now - timedelta(weeks=1)
print("One week ago it was:", one_week_ago)


### How many days until April Fools' Day?
today = date.today()
april_fools = date(today.year, 4, 1)
if april_fools < today:
    april_fools = date(today.year + 1, 4, 1)
days_until_april_fools = (april_fools - today).days
print("Days until April Fools' Day:", days_until_april_fools)
