print "How old are you?", # there's a space between the print and input
age = raw_input()
print "How tall are you?",
height = raw_input()
weight = raw_input("How much do you weigh? ")

print "So you're %r old, %r tall and %r heavy." % (
    age, height, weight)
