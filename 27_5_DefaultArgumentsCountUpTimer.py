#import time

#def count(start, end):
#    for x in range(start, end + 1):
#        print(x)
#        time.sleep(1) #this line makes the timer wait a second before counting up to next number
#    print("DONE!")

#count(0, 10) #no matter what number the user wants the timer to count up to
             #they are going to want to start at 0 so let's make a default argument for that

import time

def count(end, start = 0,): #make sure all default arguments are placed after non-default arguments for line 20 to execute without error
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(5)
#count(30, 20) #can still adjust both arguments if necessary

#def countdown(start, end):
    #for x in reversed(range(start - 1, end)):
        #print(x)
        #time.sleep(1)
    #print("BOOM!")

#countdown(2,11)
