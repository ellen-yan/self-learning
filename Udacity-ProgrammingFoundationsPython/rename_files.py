# Programming Foundations with Python
# Udacity
# Lesson 2, Exercise 2
# Renaming files (i.e. removing numbers)

import os

path = ("/Users/ellenyan/Documents/SelfLearning/Udacity-ProgrammingFoundationsPython/prank")
def rename_files():
    # get file names from a folder
    file_list = os.listdir(path)
    os.chdir(path) # change working directory to the right folder

    # for each file, rename file name
    for filename in file_list:
        # second argument: characters to remove
        new_filename = filename.translate(None, "0123456789")
        os.rename(filename, new_filename)
        print "Changed %s to %s" % (filename, new_filename)

rename_files()
