# A 2D Collection is a Collection Made Up of Collections
# if you ever need a grid or matrix of data. 2D collections work

#fruits =     ["apple", "orange", "banana", "coconut"]
#vegetables = ["celery", "carrots", "potatoes"]
#meats =      ["chicken", "fish", "turkey"]

#groceries = [fruits, vegetables, meats]

#print(groceries[1]) #this returns an entire row in the 2D collection. Specifically the second row, a list of vegetables
#print(groceries[0][3]) #this prints coconut. The 4th element in the 1st list

#fuck making seperate lists tho amirite?
#below is a better way you could format your 2D collection
#can utilize for loops and nested loops by formatting this way
#groceries = [["apple", "orange", "banana", "coconut"], 
             #["celery", "carrots", "potatoes"],
             #["chicken", "fish", "turkey"]]

#print(groceries[0])
#for collection in groceries:
    #for food in collection:
        #print(food, end = " ")
    #print()  #use this to print a grid structure of your 2d collection

#below is an example of a tuple made up of sets that is valid too
#use whatever 2D collection that is best for your programs
#groceries = ({"apple", "orange", "banana", "coconut"}, 
             #{"celery", "carrots", "potatoes"},
             #{"chicken", "fish", "turkey"})

#print(groceries[2])

#below is an example of how you can use a 2D collection to create a 2 dimensional keypad you would typically find on your phone for dialing calls
#tuples are fastest and we cam use them here so we will use them

#num_pad = ((1, 2, 3),
           #(4, 5, 6),
           #(7, 8, 9),
           #("*", 0, "#"))

#for row in num_pad:
    #for num in row:
        #print(num, end = " ")
    #print()