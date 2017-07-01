x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x # %r prints the raw data inside the variable, and therefore variable x is displayed with quotations
print "I also said: '%s'." % y # We added quotes here but %s formats the string so we don't see the quotations around it

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # variable hilarious got inserted into other string with a formatter
print joke_evaluation # formatter is printed as a string literal when nothing is inserted

w = "This is the left side of..."
e = "a string with a right side."

print w + e
