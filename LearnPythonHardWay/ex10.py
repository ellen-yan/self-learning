tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat." # escape backslash in string

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# List of all the escape sequences Python supports
# \\ - Backslash (\)
# \' or \" - single-quote or double-quote
# \a - ASCII bell (BEL)
# \b - ASCII backspace (BS)
# \f - ASCII formfeed (FF)
# \n - ASCII linefeed (LF)
# \N{name} - character named name in the Unicode database (Unicode only)
# \r - carriage return (CR)
# \t - horizontal tab (TAB)
# \uxxxx - character with 16-bit hex value xxxx (u" string only)
# \Uxxxxxxxx - character with 32-bit hex value xxxxxxxx (u" string only)
# \v - ASCII vertical tab (VT)
# \ooo - character with octal value ooo
# \xhh - character with hex value hh

# Note that if you use \U or \u, you need the unicode string in quotes with a
# u in front: e.g. u'\U0001F47E'

print "%rthis uses r to format" % "\t" # prints out raw data i.e. '\t'
print "%sthis uses s to format" % "\t" # formats tab character properly
# %r is for debugging, %s is for displaying
