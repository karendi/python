print("the back spaces sharon'\s python practise test you'\d need a couple of minutes there'\s \\ creating a \n new line and a \t tab")
print("\t i need a dollar \t a dollar is all i need \t so the tab just moves everything \t moves like four spaces")
poem = """
Can we get to the store
as quickly as possible
can we please get there \ni need to be there in like five
\n\t\tLets see what this does""" #\n creates
print("-*10")
print(poem)
print("-*10")
def secretformular(p):
    jelly_beans = p * 3
    beans = p -100
    crates = p/100
    return jelly_beans , beans , crates

start_point = 1000
jelly_beans , beans , crates = secretformular(start_point)

print("With a starting point of %r " %(start_point))
print("Now we have these many things %r, %r , %r" %(jelly_beans, beans , crates))

start_point = start_point / 100
print("we can also do this %d , %d , %d"%(secretformular(start_point)))
