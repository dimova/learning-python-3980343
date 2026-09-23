#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#



# Print the name of the OS
import os
from os import path
import time
from datetime import datetime
print(os.name)

# Check for item existence and type
print("Checking for item existence and type")
print("Does sample.txt exist? ", path.exists("sample.txt"))
print("Is sample.txt a file? ", path.isfile("sample.txt"))
print("Is sample.txt a directory? ", path.isdir("sample.txt"))

# Work with file paths
print("File name of sample.txt: ", path.basename("sample.txt"))
print("Directory name of sample.txt: ", path.dirname("sample.txt"))
print("Absolute path of sample.txt: ", path.abspath("sample.txt"))
print("Item's path of sample.txt: ", path.realpath("sample.txt"))
print("Item's path and name:", path.split(path.realpath("sample.txt")))


# Get the modification time
mod_time = path.getmtime("sample.txt")
print("Modification time of sample.txt: ", datetime.fromtimestamp(mod_time))


# Calculate how long ago the item was modified
time_since_mod = time.time() - mod_time
print("sample.txt was modified", time_since_mod, "seconds ago")
print("sample.txt was modified", time_since_mod / 60, "minutes ago")
print("sample.txt was modified", time_since_mod / 3600, "hours ago")
print("sample.txt was modified", time_since_mod / 86400, "days ago")
td = datetime.now() - datetime.fromtimestamp(mod_time)
print("sample.txt was modified", td, "ago")
