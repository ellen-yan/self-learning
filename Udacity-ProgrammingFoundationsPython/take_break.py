# Programming Foundations with Python
# Udacity
# Lesson 2, Exercise 1
# Opening a web browser after some time interval

import time
import webbrowser

reply = "y"
url = "https://www.youtube.com/watch?v=9sSK4S2q5Pk"
print "The current time is", time.ctime()
print """
How long would you like the time interval between
breaks to be, in minutes?"""

how_long = float(raw_input("> "))

how_long = int(how_long * 60)

while reply == "y":
    # suspends execution for a given number of seconds
    time.sleep(how_long)
    webbrowser.open(url)

    print """Do you have a different URL you would like to open
    for the next break? Enter y if you would like to input a URL..."""
    url_reply = raw_input("> ")
    if url_reply == "y":
        print "Enter the new URL"
        url = raw_input("> ")

    print "Ready to go back to work? Enter y to continue..."
    reply = raw_input("> ")
