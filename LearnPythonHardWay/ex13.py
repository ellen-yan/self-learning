from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# since we're unpacking three variables, we need to give the script variables
# when we run it in the terminal --> python ex13.py var1 var2 var3
