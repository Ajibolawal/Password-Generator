# 🔐 Secure Password Generator

## 🌟 Overview

As part of my **SOC automation** efforts, I built this Python script to make generating strong, unpredictable passwords quick and effortless. Manually creating passwords can lead to weak choices, but by automating the process, I ensure that every password is **secure and random** — perfect for protecting accounts and systems.

This script lets me generate a secure password using a mix of uppercase letters, lowercase letters, digits, and symbols. I simply enter the desired password length, and the script does the rest, creating a strong password instantly.

## 📝 Code Breakdown

![image](https://github.com/user-attachments/assets/b2bca149-8210-44f9-8d20-d4f6d9ffa9fb)

***Ref 1: Password generator script***

```python
import secrets
import string
```

🔹 `secrets` module: Used to generate **cryptographically secure** random values, making the password more secure than using `random`.

🔹 `string` module: Provides predefined sets of characters such as lowercase letters, uppercase letters, digits, and punctuation.

```python
passLen = input("\n\nEnter length of your password: ")
```

🔹 🖥️ `input()`: Prompts me to enter the desired password length.

🔹 🏷️ `\n\n`: Adds line breaks for better readability.

```python
lowerLetter = string.ascii_lowercase
upperLetter = string.ascii_uppercase
number = string.digits
symbols = string.punctuation
```

🔡 `string.ascii_lowercase`: Contains all lowercase letters (`a-z`).

🔠 `string.ascii_uppercase`: Contains all uppercase letters (`A-Z`).

🔢 `string.digits`: Contains all numeric digits (`0-9`).

🔣 `string.punctuation`: Contains common special characters (e.g., `!@#$%^&*()`).

```python
allChar = lowerLetter + upperLetter + number + symbols
```

🔗 Combines all character types into one string, ensuring the password is a mix of characters.

```python
password = ''.join(secrets.choice(allChar) for i in range(int(passLen)))
```

🎲 `secrets.choice(allChar)`: Randomly picks a character from `allChar`.

🔄 `''.join(...)`: Joins selected characters into a single string.

🔁 `for i in range(int(passLen))`: Repeats the selection process based on the user's input.

🔢 `int(passLen)`: Converts the input into an integer to ensure it's a valid number.

```python
print("\n\nYour Password is: "+password+"\n\n")
```

🖥️ Displays the generated password with additional line breaks for better formatting.

---

## ⚙️ Example Usage

### Input:
![image](https://github.com/user-attachments/assets/aeadbff8-5ee4-4595-8987-207a21886409)

### Output:
![image](https://github.com/user-attachments/assets/d8524e68-7c0d-4623-9750-736b1954b549)

---

## 🛠️ Tools Used

  🐍 Python 3
  
  🔐 `secrets` module (for secure random selection)
  
  🔡 `string` module (for character sets)

---

## 🚀 Skills Gained

  ✅ Understanding **secure password generation**
  
  ✅ Working with Python modules (`secrets` and `string`)
  
  ✅ Handling user input and data conversion
  
  ✅ String manipulation and concatenation
  
  ✅ Using list comprehensions for random selection
  
  ✅ Implementing automation in **SOC workflows** to improve security processes

---

## 🔮 Future Enhancements

  ⚠️ **Error Handling**: Ensure the user inputs a valid integer and handle exceptions gracefully.
  
  🎭 **Character Customisation**: Let users choose whether they want numbers, symbols, or specific character sets.
  
  🖥️ **GUI Version**: Build a user-friendly graphical interface for non-technical users.
  
  🛡️ **Strength Analysis**: Check password strength and provide feedback on complexity.
  
  🤖 **Integration with SOC Tools**: Use this password generator in **SIEM tools, privileged access management systems, and automated security workflows**.


