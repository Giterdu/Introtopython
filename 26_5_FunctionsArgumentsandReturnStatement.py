def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} os due: {due_date}")

display_invoice("Davey_Scatino", 42.69, "01/01" )

# return = statement used to end a function and send a result back to the caller

#def add(x, y):
#    z = x + y
#    return z

#def subtract(x, y):
#    z = x - y
#    return z

#def multiply (x, y):
#    z = x * y
#    return z

#def divide (x, y):
#    z = x / y
#    return z
    
#print(add(1, 2)) # the value of the add function now becomes 3
#print(subtract(1, 2)) # the value of the subtract function now becomes -1
#print(multiply(1, 2)) # the value of the multiply function now becomes 2
#print(divide (1, 2)) # the value of the divide function now becomes 0.5

#def create_name(first, last):
#    first = first.capitalize()
#    last = last.capitalize()
#    return first + " " + last

#full_name = create_name("russell", "pollock")
#print(full_name)