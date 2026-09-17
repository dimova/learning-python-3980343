# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, 2, 3, 4, 5]
mylist2=[0,1,"two",3.2,False]
print(len(mylist2))

# to access a member of a sequence type, use []
print(mylist2[2])  # access the third element of the list


# add a list to another list
mylist.extend(mylist2)
print(mylist)
mylist=mylist+mylist2
mystr = "This is a string"
print(mystr[0])  # access the first character of the string
print(mystr[5:7])  # access a slice of the string
print(mystr[:4])   # access the first four characters of the string
print(mystr[8:])   # access the characters from index 8 to the end

# use slices to get parts of a sequence
print(mylist[2:5])  # get elements from index 2 to 4
print(mylist[:3])   # get the first three elements
print(mylist[3:])   # get elements from index 3 to the end
print(mylist[:])  # get a copy of the entire list
print(mylist[1:4:2])  # get every second element from index 1 to 3

# you can use slices to reverse a sequence
print(mylist[::-1])  # reverse the list


# Tuples are like lists, but they are immutable
mytuple = (1, 2, 3, 4, 5)
print(mytuple)
print(mytuple[2])  # access the third element of the tuple


# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 4, 5}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(3 in myset)  # True
print(6 in myset)  # False
print(3 not in myset)  # False
print(6 not in myset)  # True
print(3 in mytuple)
print(5 in mylist)
