# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
# sample_file= open("sample.txt", "w+")
# sample_file.write("This is a sample line of text.\n")
# sample_file.close()

# Open the file for appending text to the end
sample_file= open("sample.txt", "a+")

# write some lines of data to the file
sample_file.write("This is another line of text.\n")
sample_file.close()

# close the file when done
