import random

# Function to roll dice
def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

# Main function
def main():
    print("Welcome to the Dice Roll Simulator!")
    
    try:
        # Get user input for number of dice and sides
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides on each die: "))
        
        # Validate inputs
        if num_dice <= 0 or num_sides <= 0:
            print("Both the number of dice and sides must be positive integers.")
            return
        
        # Roll the dice
        results = roll_dice(num_dice, num_sides)
        
        # Display the results
        print("\nRolling the dice...")
        print(f"Results: {', '.join(map(str, results))}")
        print(f"Total: {sum(results)}")
    
    except ValueError:
        print("Invalid input. Please enter positive integers for the number of dice and sides.")

# Run the main function
if __name__ == "__main__":
    main()
