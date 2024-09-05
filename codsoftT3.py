import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
