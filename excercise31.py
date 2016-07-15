print("you enter a dark room with two doors.Do you go through door 1 or 2")

door = input(">")

if door == "1":
    print("theres a huge bear eating a cheese.What do you do?")
    print("1.Take the cheese")
    print("2.Scream at the bear")

    bear = input(">")

    if bear == "1" :
      print("the bear eats your face off")
    elif bear == "2" :
      print("The bear eats your legs off")
    else :
      print("Well doing %s is better" %bear)


elif door == "2":
    print("you stare into something's retina")
    print("1.blueberries")
    print("2.Yellow Jacket")
    print("3.Understanding melodies")

    insanity = input("?")

    if insanity == "1" or insanity == "2":
        print("goodjob")
    else:
        print("Something else")
else:
    print("something else")
