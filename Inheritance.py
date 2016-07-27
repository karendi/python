#learning about classes
class Animal(object):
    is_alive = True

    def __init__(self, name, number_legs ,fur,food_eaten ):
        self.name = name
        self.legs = number_legs
        self.fur = fur
        self.food_eaten = food_eaten

    def description(self , name , legs):
        print("This %r has these many legs: %r" %(self.name , self.legs))

class Dog(Animal):
    def description(self):
        print("This %r has these many legs %r" %(self.name , self.legs))




Barry = Dog("Barry" , "4" , "has fur" , "meat")
Barry.description()

if not Barry.is_alive:
    print("sorry Barry is not around")
else:
    print("barry is alive")
