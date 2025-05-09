# 🔐 random-password-generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Author](https://img.shields.io/badge/GitHub-rafaelmoreirax-blue)

## ✨ Description

A **Random Password Generator** built in Python!  
It allows users to create strong, customizable passwords with just a few inputs.

🎯 **Features**:
- Set password length
- Option to include digits (`0–9`)
- Option to include special characters (`!@#$%^&*()` etc.)

This is a great mini project for Python beginners to get comfortable with:
- `random` module
- String manipulation
- Basic input/output

---

## 🛠️ How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/rafaelmoreirax/random-password-generator.git
   cd random-password-generator
   ```

2. **Run the script**  
   Make sure you have Python 3 installed.
   ```bash
   python password_generator.py
   ```

3. **Follow the prompts**  
   Input the desired length and character options. Get your password instantly!

---

## 📂 File Structure

```
random-password-generator/
│
├── password_generator.py    # Main Python script
└── README.md                # This file
```

---

## 🧠 Topics Covered

- ✅ Random number generation
- ✅ String concatenation
- ✅ Handling user input
- ✅ Simple CLI interaction

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Feel free to fork this project and submit a pull request. Let's improve it together! 🙌

---

## 🙋‍♂️ Author

**rafaelmoreirax**  
[GitHub Profile](https://github.com/rafaelmoreirax)

---

## 🏷️ Tags

`#Python` `#Beginner` `#CLI` `#PasswordGenerator` `#Security` `#OpenSource`

---

## 🐍 password_generator.py

```python
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
```
