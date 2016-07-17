from sys import exit

def gold_room():
    print("the room is full of gold how much do you take?")

    next = input("?")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Type a number")
    if how_much < 50:
        print("nice")
        exit(0)
    else:
        dead("naaah")

def bear_room():
    print("theres a bear")
    print("the bear has honey")
    print("Bear is infront of a door")
    print("How will you move the bear")
    bear_moved = False

    while True:
        next = input("?")

        if next == "take honey":
            dead("the bear loks at you")
        elif next == "taunt bear" and not bear_moved:
            print("The bear moves and you can go through the door")
            bear_moved = True
        elif next == "Taunt bear" and bear_moved:
            print("The bear gets angry")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea")

def evil():
    print("You see something evil")
    print("Stares at you and you go insane")
    print("do you flee or eat your head")

    next = input(">")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("tasty")
    else:
        evil()

def dead(why):
    print(why, "good job")
    exit(0)

def start():
    print("you are in a dark room")
    print("Thers a door to your left and right")
    print("Which one do you take")

    next = input("?")

    if next == "left":
        bear_room()
    elif next == "right" :
        evil()
    else:
        dead("You stumble and die")


start()
