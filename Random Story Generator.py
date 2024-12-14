import random

# Updated lists of story elements
characters = ["a fearless explorer", "an ingenious inventor", "a daring pirate", "a mysterious alien"]
settings = ["on a remote island", "in an underground laboratory", "in a parallel universe", "on the edge of a volcano"]
actions = ["discovered a powerful artifact", "uncovered a hidden conspiracy", "escaped from danger", "changed the course of history"]

# Function to generate a random story
def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    action = random.choice(actions)
    
    story = f"Once upon a time, {character} {setting} {action}."
    return story

# Main function
def main():
    print("Welcome to the Random Story Generator!")
    while True:
        print("\n" + generate_story())
        cont = input("Would you like to generate another story? (yes/no): ")
        if cont.lower() != 'yes':
            print("Thank you for using the Random Story Generator! Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
