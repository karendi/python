ten_things = "Apples Lightning Oranges Crows Telephone Light Sugar"

print("there are not ten things in the list.lets fix that")

stuff = ten_things.split(" ")
more_stuff = ["day" , "night" , "girl" , "boy", "banana" , "crow" ,"frisbee" , "aeroplane"]

while len(stuff) != 10:
     next_one = more_stuff.pop()
     print("we are addding this %r" %next_one)
     stuff.append(next_one)
     print("there are now this many stuff %d" %(len(stuff)))

print("here we go %r" %stuff)
print("lets do something with the stuff")
print("I have changed something")

print(stuff[0])
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print('#'.join(stuff[3:5]))
