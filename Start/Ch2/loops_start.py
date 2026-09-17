# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
while x < 10:
    print(x)
    x += 1

# define a for loop
for i in range(10):
    print(i)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# use a for loop over a collection
for day in days:
    print(day)


# use the break and continue statements
for day in days:
    print(day)
    if day == "Wednesday":
        break
    if day == "Tuesday":
        continue
    print("This will not print for Tuesday")
# using the enumerate() function to get an index and an item
for index, day in enumerate(days):
    print(index,day)
