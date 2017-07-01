from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    # moves to new file position in bytes (i.e. 0th byte)
    # there is a second optional argument which dictates the mode of
    # offset (the first argument). Default is offset from beginning of file
    # but if second argument is 1: offset is relative to current position,
    # and if second arg is 2: offset is relative to end of file
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(), # extra comma avoids adding a \n

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file,)

current_line += 1
print_a_line(current_line, current_file)
