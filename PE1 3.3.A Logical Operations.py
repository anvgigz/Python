def logic():#function name
    print("testing logic operattors")

    l1 = int(input("Enter a  within the range of 0 - 100: ")) # calling for user input and adding it to vabriable l1
    l2 = int(input("Enter another number witrhin the range of 0 - 100: "))# calling for user input and adding it to vabriable l2
    if l1 and l2 >100: 
        print(True) # if both numbers are greater than 100 then True is printed
    else:
        print(False) # if not then False
    if l1 <25 or l2 <25:
        print(True)  # If either Number is less than 25 then True is printed
    else:
        print(False) # if not then False
    if l1 not in range(0,101) or l2 not in range(0,101):
        print("you did not type a number within the range of 0 - 100") # If either number is not between 0-100 then this is printed
    else:
        print("you typed a number within the range of 0 - 100") # if between  0- 100 then this is printed
    

logic() # function called executing the code.
logic()
logic()
