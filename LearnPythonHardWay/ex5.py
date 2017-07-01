my_name = 'Ellen X. Yan'
my_age = 23 # not a lie
my_height = 65 # inches
my_weight = 135 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)

print "I just want to print %%"
print "This prints no matter what: %r, %r" % (my_name, my_age)

# '%s', '%d', and '%r' are "formatters". They tell Python to take the variable
# on the right and put it in to replace the %s with its value

# List of Python formatters:
# %c: character
# %s: string conversion via str() prior to formatting
# %i: signed decimal integer
# %d: signed decimal integer
# %u: unsigned decimal integer
# %o: octal integer
# %x: hexadecimal integer (lowercase letters)
# %X: hexadecimal integer (UPPERcase letters)
# %e: exponential notation (with lowercase 'e')
# %E: exponential notation (with UPPERcase 'E')
# %f: floating point real number
# %g: the shorter of %f and %e
# %G: the shorter of %f and %E
# %r: print the raw data (i.e. everything); useful for debugging
