# function = A block of resuable code
#            place () after the function name to invoke it

#print("Happy birthday to you!")
#print("You are old!")
#print("Happy birthday to you!")
#print()

# what if you could just write this code once then reuse it whenever you needed to
# with functions you can starting on line 22

#print("Happy birthday to you!")
#print("You are old!")
#print("Happy birthday to you!")
#print()

#print("Happy birthday to you!")
#print("You are old!")
#print("Happy birthday to you!")
#print()

#def happy_birthday():
#    print("Happy birthday to you!")
#    print("You are old!")
#    print("Happy birthday to you!")
#    print()

#happy_birthday()
#happy_birthday()
#happy_birthday()


# to invoke a function you type the function in and then add a set of parantheses
# you can add arguments to these sets of parantheses to pass in data but you'll need a matching set of parameters and order matters for these parameters and arguments
    #the arguments we are using here are called positional arguments. 4 types of arguments
        #1. positional  2. DEFAULT  3. keyword  4. arbitrary 
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)