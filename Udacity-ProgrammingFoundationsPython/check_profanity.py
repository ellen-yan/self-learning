import urllib

def read_text(filename):
    file_object = open(filename, "r")
    contents = file_object.read()
    print contents
    file_object.close()
    check_profanity(contents)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    print output
    connection.close()

read_text("final.txt")
