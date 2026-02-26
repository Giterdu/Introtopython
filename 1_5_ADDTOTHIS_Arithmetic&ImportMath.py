import math

x = 9.9

#print (math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x) #rounds up to the next integer
result = math.floor(x) #rounds down 

print(result)

##  ## next we will do some geometric calculations

import math

#radius = float(input("Enter the radius of a circle: "))

#circumference = 2 * math.pi * radius

#print(f"The circumference of the circle is: {round(circumference, 2)}cm")

#radius = float(input("Enter the radius of a circle: "))

#area = math.pi * pow(radius, 2)

#print(f"The area of the circle is: {round(area, 2)}cm\u00B2")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2)) #calculates the Hypotenuse of a right triangle

print(f"Side C = {c}")

#try doing this with a while loop so if you enter an invalid input it makes you enter a proper input