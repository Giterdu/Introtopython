# for loops = execute a block of code a fixed number of times.
            # you can iterate over a range, string, sequence, etc.

# Counting Forwards

#for x in range(1, 11):
    #print(x)

# Counting Backwards

#for x in reversed(range(1,11)):
    #print(x)

#print("HAPPY NEW YEAR")

# Counting backwards by intervals of two

#for x in reversed(range(0, 12, 2)):
    #print(x)

#print("HAPPY NEW YEAR")

# Skipping over unlucky number 13

#for x in (range(1, 21)):
    #if x == 13:
        #continue #while break command would stop counting after 12
    #else:
        #print(x)