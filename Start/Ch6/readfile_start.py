#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#
sample_file = open("sample.txt", "r")
if sample_file.mode == "r":
    # contents = sample_file.read()
    # print(contents)
    # sample_file.close()
    file_contents = sample_file.readlines()
    for line in file_contents:
        print(line)
    sample_file.close()
    
# Open the file and read the contents

    # use the read() function to read the entire file
