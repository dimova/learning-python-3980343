# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
# keys are immutable values
# values might be collections
mydict = {"key1": "value1", "key2": "value2",
           3: "three", 4.5: [1,2,3,4,5,6]}
# print(mydict)
# dictionaries are accessed via keys
print(mydict["key1"])  # access the value associated with "key1"

# you can also set dictionary data by creating a new key
mydict["key3"] = "value3"
print(mydict)


# Trying to access a nonexistent key will produce an error
# print(mydict["key4"])  # this will cause an error


# To avoid this, you can use the "in" operator to see if a key exists
print("key1" in mydict)  # True
print("key4" in mydict)  # False


# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())
print(mydict.values())


# You can also iterate over all the items in a dictionary
for key, value in mydict.items():
    print(key, value)
