foods = [] #using list rather than other collection type because tuples are unchanageable and can't append and sets are unordered
prices = [] 
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART ------")

for food in foods:
    print(food, end = " ")

for price in prices:
    total += price

print() #adds a line just to make it look nicer
print(f"Your total is: ${total:.2f}") #used a format specifier to round the total to 2 digits as there was a bug where it would post a ton of digits if you don't round here