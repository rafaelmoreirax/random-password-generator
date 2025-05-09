import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator")
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_specials = input("Include special characters? (y/n): ").lower() == 'y'
        password = generate_password(length, use_digits, use_specials)
        print(f"\n✅ Generated Password: {password}")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
