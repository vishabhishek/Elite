def create_acronym(phrase):
    # Split the phrase into words
    words = phrase.split()
    # Take the first letter of each word and convert it to uppercase
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

# Main function
def main():
    print("Welcome to the Acronym Creator!")
    phrase = input("Enter a phrase to create an acronym: ")
    acronym = create_acronym(phrase)
    print(f"The acronym for '{phrase}' is: {acronym}")

# Run the main function
if __name__ == "__main__":
    main()
