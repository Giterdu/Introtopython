weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit.lower() == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {weight:.2f} {unit}")
 #try to figure out how to fix case sensitive bullshit below   
elif unit.lower() == "l": #fixed on 8/4/25 utilizing lower method and lowercasing "K" and "L" 
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {weight:.2f} {unit}")
else:
    print(f"{unit} not valid")