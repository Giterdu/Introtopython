# dictionary = an object that contains a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "St. Petersburg",
            "Japan": "Tokyo"}

#print(dir(capitals)) #to display all the attributes and methods of a dictionary
#print(help(capitals)) #to display an in depth description of all these dictionary attributes and methods

#print(capitals.get("India")) #prints the capital of India

#if capitals.get("Japan"):
    #print("That capital exists")
#else:
    #print("That capital doesn't exist") #checks to see if a particular country (key) exists in the dictionary

#capitals.update({"Germany": "Berlin"}) #can use update method to insert a new {key:value} pair or update an existing {key:value} pair.
#capitals.update({"Russia": "Moscow"})
#capitals.pop("China") #to remove a {key value} pair
#capitals.popitem() #removes last {key:value} pair in dictionary
#capitals.clear() #clears the dictionary

#keys = capitals.keys()
#print(keys) #use the keys method to list all the keys in the dictionary but not the values
#for key in capitals.keys(): #can also use for loops while utilizing keys method to list each key on a different line
    #print(key)

#values = capitals.values()
#print(values) #use the values method to list all the values in the dictionary but not the keys
#for value in capitals.values(): #can also use for loops while utilizing values method to list each value on a different line
    #print(value)

#items = capitals.items()
#print(items) #items returns a dictionary object which resembles a 2D list of tuples [(),(),()]
#for key, value in capitals.items(): #can also use for loops while utilizing items method to list each {key:value} pair from the list of tuples on a different line
    #print(f"{key}: {value}")


print(capitals)