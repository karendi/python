the_count = [1 , 2 , 3, 4]
fruits = ["apples" , "grapes" , "pineapples" , "bananas"]
change = [1 , "pennies" , 2 , "dimes" , 3 , "quarters" ]

#this for loop goes through a list

for number in the_count:
    print ("This is count %d" %number)

#same as above
for fruit in fruits:
    print("A fruit of type:%s" %fruit)

#going through mixed lists use %r to get the raw output coz we dont know whats there
for i in change:
    print("print I got %r" %i)

#building lists:start with an empty lists
elements = []

#using the range function to do 0 to 5 counts
for i in range(0 , 6):
    print("Adding %d to the list." %i)
    elements.append(i)

#printing the appended list
for i in elements:
    print("Element was %d" %i)

#additional list
newelements = []

for i in range(0, 9):
    print("Adding %d to new elements" %i)
