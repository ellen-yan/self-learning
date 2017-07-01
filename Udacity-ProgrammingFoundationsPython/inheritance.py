class Parent():

    def __init__(self, lastname, eye_color):
        print "Parent constructor called"
        self.last_name = lastname
        self.eye_color = eye_color

    def show_info(self):
        print "Last Name: %s" % self.last_name
        print "Eye Color: %s" % self.eye_color

class Child(Parent): # Child inherits from Parent; methods also inherited

    def __init__(self, last_name, eye_color, number_of_toys):
        print "Child constructor called"
        Parent.__init__(self, last_name, eye_color) # reuse class Parent's init method
        self.number_of_toys = number_of_toys
        # used to make sure next method in method reoslution order called - see inheritance2.py
        #super(Child, self).__init__(last_name, eye_color) # can only be used if parent inherits object


    def show_info(self): # overrides parent method
        print "Last Name: %s" % self.last_name
        print "Eye Color: %s" % self.eye_color
        print "Number of toys: %d" % self.number_of_toys

billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "blue", 5)
miley_cyrus.show_info()
#print miley_cyrus.last_name
#print miley_cyrus.number_of_toys
