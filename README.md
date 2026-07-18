# Vowel or Consonant Checker in Python

## 📌 Overview

This project is a simple Python program that determines whether a user-entered alphabet is a **vowel** or a **consonant**.

The program first validates that the input is a **single alphabetic character**, converts it to uppercase for case-insensitive comparison, and then uses Python's **`match-case`** statement to identify whether the character is a vowel or consonant.

This project is ideal for beginners learning conditional statements, input validation, string methods, and pattern matching in Python.

---

## 🚀 Features

* Accepts a single alphabet as input
* Validates user input
* Handles both uppercase and lowercase letters
* Uses Python's `match-case` statement
* Identifies vowels and consonants
* Displays an error message for invalid input

---

## 🛠️ Technologies Used

* Python 3.10+

---

## 📂 Project Structure

```text
├── vowel_consonant_checker.py
└── README.md
```

---

## 💻 Source Code

```python
ch = input("Enter any alphabet : ")

if len(ch) == 1 and ch.isalpha():
    ch = ch.upper()

    match ch:
        case 'A' | 'E' | 'I' | 'O' | 'U':
            print("Vowel")
        case _:
            print("Consonant")
else:
    print("Error")
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-vowel-consonant-checker.git
cd python-vowel-consonant-checker
```

### Run the Program

```bash
python vowel_consonant_checker.py
```

---

## 📋 Sample Output

### Example 1

```text
Enter any alphabet : A
Vowel
```

### Example 2

```text
Enter any alphabet : m
Consonant
```

### Example 3

```text
Enter any alphabet : 8
Error
```

### Example 4

```text
Enter any alphabet : AB
Error
```

---

## 🧠 Concepts Covered

* User Input
* Conditional Statements (`if-else`)
* String Methods (`isalpha()`, `upper()`)
* Pattern Matching (`match-case`)
* Input Validation

---

## 🔍 How It Works

1. Accept a character from the user.
2. Check whether the input contains exactly one alphabetic character.
3. Convert the character to uppercase.
4. Compare it against the vowel characters (`A`, `E`, `I`, `O`, `U`) using `match-case`.
5. Display:

   * **Vowel** if it matches.
   * **Consonant** otherwise.
6. Print **Error** if the input is invalid.

---

## ⏱️ Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(1)**   |
| Space Complexity | **O(1)**   |

The program performs a fixed number of operations regardless of the input.

---

## 🔮 Future Improvements

* Accept complete words and count vowels and consonants
* Support multiple language alphabets
* Display the total number of vowels and consonants in a sentence
* Create a graphical version using Tkinter
* Build a web-based version using Flask

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* How to validate user input
* How to use string methods effectively
* How to implement pattern matching with `match-case`
* The difference between vowels and consonants in programming logic
* Writing clean and readable Python code

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software Engineer | Python | Java | SQL | Data Analytics

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="530" height="718" alt="image" src="https://github.com/user-attachments/assets/0985b31e-33e5-4869-bbd4-1fedb357a9fd" />
