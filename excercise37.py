from sys import exit

def cakes_bought(cakes , customers ,price):
    cakes = int(cakes) - int(customers)
    total = (int(price) * int(customers))
    print("The number of cakes bought %r and the total amount got from it is %r"%(cakes , total))

def profit():

    production_cost = 700 #production cost of one cake.This is a local variable
    total_profit = (int(customers)*int(price)) - (int(customers)*production_cost)
    print("the total profit got was %r" %total_profit)

    #with and as example.The argument must be a string if you are writing to a file
    with open("withexample.txt" , "w") as f:
        f.write(str(total_profit))
        

    with open("withexample.txt") as y:
        data = y.read()
        print(data)



#using global variables
cakes = input("How many cakes have been made?")
customers = input("how many customers have bought the cakes?")
price = input("whats the price of one cake?")
answer = input("do you want to calculate the total amount got or the profit?")

if answer == "total amount":
    cakes_bought(cakes , customers ,price)
elif answer == "profit" :
    profit()
else:
    exit(0)
