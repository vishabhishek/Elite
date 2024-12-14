def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function
def main():
    print("Welcome to the BMI Calculator!")
    
    # Get user input for weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Validate inputs
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        # Classify BMI
        classification = classify_bmi(bmi)
        
        # Display the result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {classification}")
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

# Run the main function
if __name__ == "__main__":
    main()
