class Other(object):
    def override(self):
        print("other override")

    def implicit(self):
        print("Other implicit()")

    def altered(self):
        print("Other altered()")

class child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print(2*9)
        self.other.altered()
        print(3 ** 2)

son = child()

son.implicit()
son.override()
son.altered()
