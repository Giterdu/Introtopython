# collection = single "variable" used to store multiple values
#   List = [] ordered and changable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangable, Duplicates OK. FASTER 
    # list, set, and tuple are all be commands too for converting one collection type to another.
#   Dictionaries--> We will cover them in another lesson. Each collection has unique benefits



# LISTS
fruits = ["apple", "orange", "banana", "coconut", "coconut"]
tupleafruits = ("dragonfruit", "cherry", "grapes", "grapefruit")

#the 4 lines below are some examples of index operators you can use for collections
#print(fruits[1]) #prints orange
#print(fruits[::2]) #prints every 2nd element beginning with index[0]
#print(fruits[::-2]) #prints every 2nd element backwards beginning with last element
#print(fruits[::-1]) #prints every element backwards

#for fruit in fruits: #proper naming convention for iterating collections
    #print(fruit)

#print("apple" in fruits)
#print("pineapple" in fruits) 
#fruits[1] = "pineapple" #replaces orange with pineapple

#fruits.append("pineapple") #adds pineapple to end of collection
#fruits.extend(tupleafruits) #adds all the elements of any iterable to the end of the current list
#fruits.remove("apple")
#fruits.pop() #removes whatever element shows up last for lists and randomly removes an element in sets
#fruits.insert(2, "pear") #insert method can add a value to a specific index
#fruits.sort() #sorts the collection in alphabetical order
#fruits.reverse() #sorts not in not necessarily reverse alphabetical order, but in reverse to the way in which list is currently sorted
#to sort in reverse alphabetical order first sort then reverse.
#fruits.clear() #clears all the elements in a collection
#print(fruits) #prints new collection with edited elements

#print(fruits.index("orange")) #prints the index of a particular element in a collection
#print(fruits.count("pineapple")) #prints the amount of times an element appears in a collection. Lists and Tuples can have duplicates. Sets cannot have duplicates in their collection
#print(len(fruits)) #prints the number of elements in a collection
#print(fruits)

#print(dir(fruits)) #to list the different methods that are available to a list
#print(help(fruits)) #to print a description of all the methods and attributes available to a list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2] #unpacking/titty operator (*) provides an efficient way of combining multiple lists at once but I prefer the extend method

print(merged_list)


# SETS #work well when you're working with constants ex: seeing if a particular COLOR is in a set

fruits = {"apple", "orange", "banana", "coconut", "coconut"} #will only print one coconut as it doesn't accept duplicates

#print(fruits) #will print in a random order because it is a set and sets are unordered
#print(fruits[0]) #will return a type error because you are unable to utilize indexing on a set because sets are unordered

#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop() #removes a random element in the set unlike the pop method function in other collections
#print(fruits)

#print(dir(fruits)) #to list the different methods that are available to a set
#print(help(fruits)) #to print a description of all the methods and attributes available to a set

numbers_with_duplicates = (1, 2, 2, 3, 4, 3, 5)
unique_numbers = set(numbers_with_duplicates)
print(unique_numbers)

# TUPLES #faster than lists. If you're working with a collection and it's ok if the collection is ordered and ununchangable you mine as well use a tuple because it's faster than the other collections.

fruits = ("apple", "orange", "banana", "coconut", "coconut")

#print(fruits.index("coconut")) #will print the index of the first time a particular element appears in a tuple or list
#print(fruits.count("coconut")) #prints the amount of times an element appears in a collection. Lists and Tuples can have duplicates

#for fruit in fruits: #lists and tuples are iterable unlike sets
    #print(fruit)

#print(dir(fruits)) #to list the different methods that are available to a tuple (tuples only have 2 methods available .index and .count)
#print(help(fruits)) #to print a description of all the methods and attributes available to a set

numbers_without_duplicates = {1, 2, 3, 4, 5}
numbers_can_duplicate = list(unique_numbers)
twoplicates = [1,5]
numbers_can_duplicate.extend(twoplicates)
print(numbers_can_duplicate)