operator: str = input("Enter an operator (+-*/): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print("not valid")

#now do this with a while loop that forces the user to input an operator and two numbers
#use the while loop lesson 11 as a reference guide for this while loop calculcator.
    #didn't need to do all that while loop stuff I just added an else statement on line 17 (1/14/26)
    #ok still add to this with a while loop if you want user to enter correct input for each