# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # one way to print multiple lines

print "Here are the days: ", days
print "Here are the months: ", months

# another way to print multiple lines (even the 'enter' key is converted to newlines)
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# newline characters are printed out with quotes around, i.e. raw data
print "Just curious: %r" % months
