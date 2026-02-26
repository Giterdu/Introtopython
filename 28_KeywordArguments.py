#keyword argument = an argument preceded by an identifier
#helps with readability. order of arguments doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

#hello("Hello", "Mr.", "Spongebob", "Squarepants") #example of positional arguments where order matters

hello("Hello", title = "Mr.", last = "Squarepants", first = "Spongebob",) #order doesnt matter in keyword arguments
     #"Hello", above is still a positional argument and if placed after a keyword argument it will give you an error like in the example of the syntax error below
#hello(title="Mr.", last="Squarepants", first="Spongebob", "Hello")


#we have used keyword arguments for formatting in past lessons as well. An example of this is shown below with the usage of the end keyword argument to add a space between the numbers being printed on the same line
for x in range(1,11):
    print(x, end= " ")

print("1", "2", "3", "4", "5", sep = "-")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country = 1, area = 123, first = 456, last = 7890)

print(phone_num)