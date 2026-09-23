#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import shutil
import os
from os import path
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("sample.txt.old"):
    # get the path to the file in the current directory
    src = path.realpath("sample.txt.old")
    # # get the path to the file in the current directory
    #dst = src + ".bak"

    # shutil.copy(src, dst)
    # # let's make a backup copy by appending "bak" to the name

    # # now use the shell to make a copy of the file


    # # rename the original file
    ##os.rename("sample.txt", "sample.txt.old")

    #os.remove(dst)
    # now put things into a ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("sample", "zip", root_dir, tail)


    # more fine-grained control over ZIP files
with ZipFile("test.zip", "w") as zip:
    zip.write("sample.txt.old")
    zip.write("sample.txt.bak")