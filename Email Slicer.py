def email_slicer(email):
    # Split the email into username and domain
    username, domain = email.split('@')
    return username, domain

# Main function
def main():
    # Get email input from the user
    email = input("Enter your email address: ")
    
    # Validate the input
    if '@' in email and '.' in email:
        username, domain = email_slicer(email)
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email address. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
