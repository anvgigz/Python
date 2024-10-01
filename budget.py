def mybudget():
    # Prompting the user to enter the total budget
    print("Please enter the amount of money you have in your budget:")
    budget = float(input())
    
    # Creating question and answer prompts for budget items
    print("How much of this budget is for your rent?")
    rent = float(input())
    print("How much of this budget is for your utilities?")
    utilities = float(input())
    print("How much of this budget is for your groceries?")
    groceries = float(input())
    print("How much of this budget is for your transportation?")
    transportation = float(input())
    print("How much of this budget is for your healthcare?")
    healthcare = float(input())
    print("How much of this budget is for your personal care?")
    personalcare = float(input())
    print("How much of this budget is for your clothing?")
    clothing = float(input())
    print("How much of this budget is for your debt?")
    debt = float(input())
    
    # Calculating the total amount spent
    total = rent + utilities + groceries + transportation + healthcare + personalcare + clothing + debt
    
    # Calculating the amount left over
    left_over = budget - total
    
    # Calculating the amount over budget
    over_by = total - budget
    
    # Calculating the percentage of the budget spent on each item
    rent_percentage = (rent / budget) * 100
    utilities_percentage = (utilities / budget) * 100
    groceries_percentage = (groceries / budget) * 100
    transportation_percentage = (transportation / budget) * 100
    healthcare_percentage = (healthcare / budget) * 100
    personalcare_percentage = (personalcare / budget) * 100
    clothing_percentage = (clothing / budget) * 100
    debt_percentage = (debt / budget) * 100
    
    # Printing the results
    print(f"Percentage of budget spent on rent: {rent_percentage:.2f}%")
    print(f"Percentage of budget spent on utilities: {utilities_percentage:.2f}%")
    print(f"Percentage of budget spent on groceries: {groceries_percentage:.2f}%")
    print(f"Percentage of budget spent on transportation: {transportation_percentage:.2f}%")
    print(f"Percentage of budget spent on healthcare: {healthcare_percentage:.2f}%")
    print(f"Percentage of budget spent on personal care: {personalcare_percentage:.2f}%")
    print(f"Percentage of budget spent on clothing: {clothing_percentage:.2f}%")
    print(f"Percentage of budget spent on debt: {debt_percentage:.2f}%")

    # Checking if the budget has been exceeded
    if total > budget:
        print(f"You have exceeded your budget by {over_by:.2f}")
    # Checking if the budget has not been exceeded   
    else:
        print(f"You have not exceeded your budget. You have {left_over:.2f} left over.")
        
# Calling the function
mybudget()
