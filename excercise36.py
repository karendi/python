from sys import exit

def red_ball() :
    print("you have chosen a red ball")
    pick_bat()

def blue_ball() :
    print("you have chosen a blue ball")
    pick_bat()

def green_ball() :
    print("you have chosen a green ball")
    pick_bat()

def pick_bat():
    bat = input("Please choose either a green blue or red bat?")


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
