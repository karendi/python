#working with classes
"""initialize a class"""
class Fruit(object):
    def __init__(self, name , colour , flavour , poisonous):
        self.name = name
        self.colour = colour
        self.flavour = flavour
        self.poisonous = poisonous

    def description(self):
        print("A %s is very %s" %(self.name , self.flavour))

    def edible(self):
        if not self.poisonous:
            print("you can eat this fruit")
        else:
            print("You cannot eat this fruit")

Lemon = Fruit("lemon" , "yellow" , "bitter" , False)

Lemon.description()
Lemon.edible()
