people = 30
cars = 40
buses = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide")

if buses > cars:
    print("That's too many cars")
elif buses < cars :
    print("maybe we could take the buses")
else:
    print("We still cant decide")

if people > buses:
    print("Alright lest then just take the buses")
else:
    print("Fine lets stay home then")
