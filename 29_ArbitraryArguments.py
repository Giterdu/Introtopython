#arbitrary arguments = a varying amount of arguments.
#to accept a varying amount of arguments developers use the parameters of *args and **kwargs
#                                                                 */** = unpacking operators
# 4 types of arguments in total: 1. positional 2. default 3. keyword 4. ARBITRARY



# *args = allows you to pass multiple non-key arguments

#def add (a, b):
    #return a + b

#print (add(1, 2))
#print (add(1, 2, 3)) #leads to an error because it takes only 2 positional arguments

#def add(*args): #args class collection type is a tuple in this example
    #total = 0
    #for arg in args:
        #total += arg
    #return total

#print(add(1, 2, 3, 4, 5))

#def display_name(*args): #with the unpacking operators and a unique parameter name you can pack various arguments into a tuple
    #for arg in args:
        #print(arg, end = " ")

#display_name("Professor", "Spongebob", "Edward", "Squarepants", "3")



# **kwargs = allows you to pass multiple keyword-arguments

#def print_address(**kwargs):
    #for key, value in kwargs.items():
        #print(f"{key}")

#print_address(street = "2444 West Estes",
              #apt = "3",
              #city = "Chicago", 
              #state = "IL", 
              #zip = "60645")



#you can also use *args and **kwargs together like in the following example

def shipping_label(*args, **kwargs): #*args must be in front of **kwargs or it will lead to a syntax error because your keyword arguments must follow your positional arguments
    for arg in args:
        print(arg, end = " ")
    print()
    #for value in kwargs.values():
        #print(value, end = " ")
    
    print(f"{kwargs.get('Street')}")
    print(f"{kwargs.get('City')} {kwargs.get('State')} {kwargs.get('Zip')}") #city State and Zip all case sensitive



shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               Street = "123 Fake St",
               City = "Detroit",
               State = "MI",
               Zip = "54321")