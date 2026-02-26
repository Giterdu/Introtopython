# Validate user input exercise
    #1 username is no more than 12 characters
    #2 username must not contain spaces
    #3 username must not contain digits

username = input("Enter a username: ") 

# below is step 1
if len(username) > 12:
    print("Your username can't be more than 12 characters")
# below is step 2
elif not username.find(" ") == -1:  #if no spaces are found the find method will return -1
    print("Your username can't contain spaces")
# below is step 3
elif not username.isalpha(): #this would technically check for spaces for step 2 too
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")