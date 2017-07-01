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

UserA()
