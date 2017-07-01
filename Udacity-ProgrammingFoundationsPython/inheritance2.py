# The point of writing super() is to ensure that the next method in line
# in the method resolution order (MRO) is called, which becomes important
# in multiple inheritance
# Note: super() can only be called if an ancestor inherits object eventually

class Base(object):
    def __init__(self):
        print("Base init'ed")

class ChildA(Base):
    def __init__(self):
        print("ChildA init'ed")
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        print("ChildB init'ed")
        super(ChildB, self).__init__()

class UserDependency(Base):
    def __init__(self):
        print("UserDependency init'ed")
        super(UserDependency, self).__init__()

class UserA(ChildA, UserDependency):
    def __init__(self):
        print("UserA init'ed")
        super(UserA, self).__init__()

class UserB(ChildB, UserDependency):
    def __init__(self):
        print("UserB init'ed")
        super(UserB, self).__init__()

UserA() # UserDependency never gets called because ChildA does not use super()
UserB() # UserDependency gets called before Base
