# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                 inner loop:

#for x in range(1, 10):
    #print(x, end=" ") #counts the numbers 1 thru 9 on the same line with spaces
                        #if you wanted to do this 3 times
                            #you could make 3 different loops OR...

# nested loop all printed on the same line

#for x in range(3):
    #for counter in range(1, 10):
        #print(counter, end="") #no spaces between numbers here

# each of the 3 nested loops printed on its own line

#for x in range(3): #you want to iterate the nested loop thrice
    #for counter in range(1, 10):
        #print(counter, end = " ") #spaces between numbers here
    #print() #so within the outer loop but not within the inner loop create a blank print statement to
             #print on next line

# printing a rectangle using any character a user can set (customizable)

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
character = input("Enter a character to use: ")

#for x in range(rows): #how many times to iterate nested loop
    #for y in range(columns): 
        #print(character, end = " ") #spaces between numbers here
    #print()