# 🔐 Password Strength Checker

A Python-based **Password Strength Checker** designed to evaluate password security and provide users with actionable feedback for creating stronger passwords.

This project demonstrates fundamental **cybersecurity, password security, input validation, and secure authentication concepts**.

---

## 📌 Project Overview

Weak passwords are one of the most common causes of account compromise. This project provides a simple security tool that analyses a password and determines its overall strength.

The checker evaluates passwords based on multiple security characteristics, including:

* Password length
* Uppercase characters
* Lowercase characters
* Numbers
* Special characters
* Common password patterns
* Password complexity
* Estimated password entropy

The tool then provides a strength rating and recommendations for improving weak passwords.

---

## 🎯 Objectives

The main objectives of this project are to:

* Understand password security principles
* Implement password strength validation using Python
* Identify weak password characteristics
* Demonstrate secure password practices
* Provide useful feedback to users
* Understand the importance of password entropy and complexity
* Apply basic cybersecurity concepts in a practical project

---

## 🛠️ Technologies Used

| Technology          | Purpose                          |
| ------------------- | -------------------------------- |
| Python              | Core programming language        |
| Regular Expressions | Character and pattern validation |
| Entropy Calculation | Password randomness estimation   |
| CLI                 | User interaction                 |

---

## ⚙️ Features

### 🔍 Password Strength Analysis

The application checks:

* ✅ Password length
* ✅ Uppercase letters
* ✅ Lowercase letters
* ✅ Numeric characters
* ✅ Special characters
* ✅ Common password patterns
* ✅ Overall password complexity

### 📊 Strength Rating

Passwords are classified into different strength levels such as:

* 🔴 Very Weak
* 🟠 Weak
* 🟡 Moderate
* 🟢 Strong
* 🔵 Very Strong

### 💡 Security Recommendations

The application provides suggestions when a password is weak, such as:

* Increase password length
* Add uppercase characters
* Add lowercase characters
* Include numbers
* Include special characters
* Avoid common password patterns

---

## 📂 Project Structure

```text
Password-Strength-Checker/
│
├── password_strength_checker.py
├── README.md
├── requirements.txt
└── .gitignore
```

> The exact file structure may vary depending on the final project implementation.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Password-Strength-Checker.git
```

### 2. Navigate to the Project

```bash
cd Password-Strength-Checker
```

### 3. Install Dependencies

If the project uses external Python packages:

```bash
pip install -r requirements.txt
```

If no external packages are required, this step can be skipped.

---

## ▶️ Usage

Run the Python application:

```bash
python password_strength_checker.py
```

Enter a password when prompted.

The application will analyse the password and display:

* Password strength
* Security score
* Detected weaknesses
* Recommendations for improvement

---

## 🧪 Example

```text
========================================
       PASSWORD STRENGTH CHECKER
========================================

Enter password: Example@123

Password Strength: STRONG

Security Analysis:
[✓] Minimum length requirement satisfied
[✓] Contains uppercase letters
[✓] Contains lowercase letters
[✓] Contains numbers
[✓] Contains special characters

Recommendation:
Consider using a longer passphrase for increased security.
```

---

## 🔐 Security Concepts Demonstrated

This project demonstrates several important cybersecurity concepts.

### Password Complexity

A password becomes more difficult to guess when it contains a combination of different character types.

### Password Length

Longer passwords generally provide significantly better resistance against brute-force attacks.

### Entropy

Password entropy is an estimation of how unpredictable a password is.

Higher entropy generally indicates a more difficult password to guess.

### Brute-Force Resistance

The project demonstrates why short and predictable passwords are more vulnerable to automated guessing attacks.

### Common Password Detection

Common passwords and predictable patterns should be avoided because attackers can test them very quickly using password dictionaries.

---

## ⚠️ Security Considerations

This project is intended for **educational and demonstration purposes**.

A password strength checker should not be treated as a complete authentication security solution.

In a production authentication system:

* Passwords should never be stored in plaintext
* Passwords should be securely hashed
* Strong password hashing algorithms such as Argon2id, bcrypt, or scrypt should be considered
* Multi-factor authentication should be implemented where appropriate
* Rate limiting should be used to reduce automated guessing
* Password breach detection can be used to identify compromised passwords

---

## 📚 What I Learned

Through this project, I gained practical experience with:

* Python programming
* Regular expressions
* Input validation
* Password security
* Entropy concepts
* Brute-force attack concepts
* Secure authentication principles
* Cybersecurity-focused problem solving
* Git and GitHub project management

---

## 🔮 Future Improvements

Possible future improvements include:

* [ ] Add graphical user interface
* [ ] Add password entropy visualization
* [ ] Add compromised-password checking using a privacy-preserving API
* [ ] Add password generation functionality
* [ ] Add unit tests
* [ ] Add configurable security policies
* [ ] Add multilingual support
* [ ] Add password-strength meter
* [ ] Improve common-password detection

---

## ⚖️ Disclaimer

This project is created for **educational and cybersecurity learning purposes only**.

It should not be considered a complete password security solution for production authentication systems.

---

## 👨‍💻 Author

**Minindu Madhubhashana Jayalath**

Cybersecurity Student | Aspiring Cybersecurity Professional

---

## ⭐ Support

If you found this project useful for learning cybersecurity concepts, consider giving the repository a ⭐.
