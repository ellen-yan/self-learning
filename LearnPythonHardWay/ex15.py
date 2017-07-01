from sys import argv # sys is a package; gets argv module from the package

script, filename = argv

txt = open(filename) # creates new file object

print "Here's your file %r:" % filename
print txt.read() # txt is now a file that has a function read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# important to close files when done
txt.close()
txt_again.close()
