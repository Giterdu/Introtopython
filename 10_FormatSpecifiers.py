# format specifiers = {value:flags} format 

price1 = 3.14159
price2 = -987.65
price3 = 12.34

#print(f"Price 1 is ${price1:.3f}") #rounded to the third decimal
#print(f"Price 2 is ${price2:>10}") #right justified with 10 total characters. (<10 would be left justified with 10 total characters)
#print(f"Price 3 is ${price3:010}") #zero padded with 10 total characters


price4 = 3000.14159
price5 = -9870.65
price6 = 1200.34

# below prints all 3 prices center-aligned
#print(f"Price 1 is ${price1:^10}") 
#print(f"Price 2 is ${price2:^10}")
#print(f"Price 3 is ${price4:^10}")

# below displays a plus sign to any positive values 
#print(f"Price 4 is ${price4:+}")
#print(f"Price 5 is ${price5:+}")
#print(f"Price 6 is ${price6:+}")

# below displays a space character in front of any positive values 
#print(f"Price 4 is ${price4: }")
#print(f"Price 5 is ${price5: }")
#print(f"Price 6 is ${price6: }")

# below displays commas for each thousandths place
#print(f"Price 4 is ${price4:,}")
#print(f"Price 5 is ${price5:,}")
#print(f"Price 6 is ${price6:,}")

# below displays commas for each thousandths place along with decimal point precision of 2 digits as well as a plus sign in front of any positive values
#print(f"Price 4 is ${price4:+,.2f}")
#print(f"Price 5 is ${price5:+,.2f}")
#print(f"Price 6 is ${price6:+,.2f}")