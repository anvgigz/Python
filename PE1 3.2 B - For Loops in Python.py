from sympy import li


def divisible_by_7():
    list = []
    for divisible in range(1,300):
        if divisible % 7 == 0:
            list.append(divisible)
    print(list)






divisible_by_7()