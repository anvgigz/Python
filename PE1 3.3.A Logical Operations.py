def logic():
    print("testing logic operattors")

    l1 = int(input("Enter a  within the range of 0 - 100: "))
    l2 = int(input("Enter another number witrhin the range of 0 - 100: "))
    if l1 and l2 >100:
        print(True)
    else:
        print(False)
    if l1 <25 or l2 <25:
        print(True)
    else:
        print(False)
    if l1 not in range(0,101) or l2 not in range(0,101):
        print("you did not type a number within the range of 0 - 100")
    else:
        print("you typed a number within the range of 0 - 100")
    

logic()

