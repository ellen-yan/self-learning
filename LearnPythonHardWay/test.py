from sys import argv

script, filename = argv

target = open(filename)
print "Reading file:"
print target.read()

print "Opening file with 'w'"

target = open(filename, 'w')
target.close()
target = open(filename)
contents = target.read()
print "Here's the file"
print contents
