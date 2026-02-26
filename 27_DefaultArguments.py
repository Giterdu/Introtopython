#default arguments = a default value for certain parameters. Default is used when that argument is omitted. This makes your functions more flexibles and reduces the # of arguments.

#def net_price(list_price, discount, tax):
    #return list_price * (1 - discount) * (1 + tax)

#print(net_price(500, 0, 0.05)) #rather than manually having to set the discount and tax parameters for every transaction you can keep a default argument value for them as shown below

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

#print(net_price(500)) #now what if the customer had a coupon for 10% off his next transaction...You can see an example of this on the next line
#print(net_price(500, 0.1))