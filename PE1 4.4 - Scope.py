#BMI Calculator Assignment




# Global constants for conversion
POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

def user_input():
    try:
        weight_in_pounds = float(input("Please provide your weight in pounds: "))
        height_in_inches = float(input("Please provide your height in inches: "))
        return weight_in_pounds, height_in_inches
    except ValueError:
        print("Please enter a valid number")

def calculate_bmi(weight_pounds, height_inches):
    # Convert weight and height to metric units
    weight_kg = weight_pounds * POUNDS_TO_KG
    height_meters = height_inches * INCHES_TO_METERS
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    return bmi


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
def main():
    # Get user input
    weight_pounds, height_inches = user_input()
    # Calculate BMI
    bmi = calculate_bmi(weight_pounds, height_inches)
    # Determine BMI category
    bmi_category = determine_bmi_category(bmi)
    # Output results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {bmi_category}")

if __name__ == "__main__": #calls the code function main only if the script is run directly
    main() #calls the main function