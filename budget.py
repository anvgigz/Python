
def mybudget():
    print("please enter the amount of money you have in your budget")
    budget = float(input())
    print("how much of this budget is for your rent?")
    rent = float(input())
    print("how much of this budget is for your Utilities?")
    utilities = float(input())
    print("how much of this budget is for your groceries?")
    groceries = float(input())
    print("how much of this budget is for your transportation?")
    transportation = float(input())
    print("how much of this budget is for your Healthcare?")  
    healthcare = float(input())
    print("how much of this budget is for your Personal Care?")
    personalcare = float(input())
    print("how much of this budget is for your Clothing?")
    clothing = float(input())
    print("how much of this budget is for your Debt?")
    debt = float(input())
    total = rent + utilities + groceries + transportation + healthcare + personalcare + clothing + debt
    left_over = budget - total
    over_by = budget - total
    rent_percentage = (rent / total) * 100
    utilities_percentage = (utilities / total) * 100
    groceries_percentage = (groceries / total) * 100
    transportation_percentage = (transportation / total) * 100
    healthcare_percentage = (healthcare / total) * 100
    personalcare_percentage = (personalcare / total) * 100
    clothing_percentage = (clothing / total) * 100
    debt_percentage = (debt / total) * 100
            
    print(f"Percentage of budget spent on rent: {rent_percentage:.2f}%")
    print(f"Percentage of budget spent on utilities: {utilities_percentage:.2f}%")
    print(f"Percentage of budget spent on groceries: {groceries_percentage:.2f}%")
    print(f"Percentage of budget spent on transportation: {transportation_percentage:.2f}%")
    print(f"Percentage of budget spent on healthcare: {healthcare_percentage:.2f}%")
    print(f"Percentage of budget spent on personal care: {personalcare_percentage:.2f}%")
    print(f"Percentage of budget spent on clothing: {clothing_percentage:.2f}%")
    print(f"Percentage of budget spent on debt: {debt_percentage:.2f}%")


    if total > budget:
        print(f"""you have exceeded your budget
              by {over_by}""")
        
    else:
        print(f"""you have not exceeded your budget
              you have {left_over} left over""")
        

mybudget()



