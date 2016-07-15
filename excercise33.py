i = 0
mynumbers = []

while i < 6:
    print("the number at the top is %d:" %i)
    mynumbers.append(i)

    i += 1
    print(mynumbers)
    print("at the bottom i is %d" %i)

print("The numbers are:")

for num in mynumbers:
    print(num)
