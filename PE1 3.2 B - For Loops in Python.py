def divisible_by_7():
    list = [] # empty list to beused for appending numbers that are divisible by 7
    for divisible in range(1,301): # numbers 1 - 300 will be used
        if divisible % 7 == 0: # range(1,300) each number checked for perfect divisibility == 0 remainder
            list.append(divisible) # numbers 0 remainder are added to the list
    print(list) #print new list






divisible_by_7() #call function
