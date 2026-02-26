principal = 0
rate = 0
time = 0

#while principal <= 0:
    #principal = float(input("Enter the principal amount: "))
    #if principal <= 0:
        #print("Principal can't be less than or equal to zero.")

#while rate <= 0:
    #rate = float(input("Enter the interest rate: "))
    #if rate <= 0:
        #print ("Interest rate can't be less than or equal to zero.")

#while time <= 0:
    #time = float(input("Enter the time: "))
    #if time <= 0:
        #print ("Time can't be less than or equal to zero.")

# below is a compound interest calculator on python that can accept 0 as input

#while True:
    #principal = float(input("Enter the principal amount: "))
    #if principal < 0:
        #print("Principal can't be less than zero.")
    #else:
        #break

#while True:
    #rate = float(input("Enter the interest rate: "))
    #if rate < 0:
        #print ("Interest rate can't be less than zero.")
    #else:
        #break

#while True:
    #time = float(input("Enter the time: "))
    #if time < 0:
        #print ("Time can't be less than zero.")
    #else:
        #break

#try to make a compound interest calculator with a while not loop instead of while loop next

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")