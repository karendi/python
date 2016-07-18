from sys import exit
from sys import argv

script, username = argv

def red_ball() :
    print("you have chosen a red ball")
    pick_bat()
    hit_ball()

def blue_ball() :
    print("you have chosen a blue ball")
    pick_bat()
    hit_ball()

def green_ball() :
    print("you have chosen a green ball")
    pick_bat()
    hit_ball()

def pick_bat():
    bat = input("Please choose either a green blue or red bat?")
    if bat == "green":
        print("You can only use it to hit either the blue or red ball")


    elif bat == "blue" :
        print("You can use it to hit either the blue or green ball")


    elif bat == "red" :
        print("You can use it to hit either the blue or green ball")


    else:
        exit(0)

def hit_ball():
    message = print("Congragulations you have hit the ball")


player = input("whats your name?")
print("okay %s welcome.." %player)
print("please pick a ball")
ball = input("please choose the ball you want")

if ball == "red":
    red_ball()

elif ball == "blue":
    blue_ball()

elif ball == "green":
    green_ball()

else:
    exit(0)
