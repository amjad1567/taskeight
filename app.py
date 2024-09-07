import re

# Function to validate email using regular expressions
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Function to validate the form data
def register_user():
    fullname = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    gender = input("Enter your gender (male/female/other): ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    # Validate email
    if not is_valid_email(email):
        print("Invalid email address.")
        return

    # Check if passwords match
    if password != confirm_password:
        print("Passwords do not match.")
        return

    # Process registration (for example, print a success message)
    print(f"Welcome, {fullname}! You have successfully registered.")
    print(f"Details:\nEmail: {email}\nGender: {gender}\nDate of Birth: {dob}")

# Call the function to handle registration
if __name__ == "__main__":
    register_user()
