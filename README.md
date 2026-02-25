# password-strength-checker

A Python-based password validation tool that evaluates password strength using composition rules and real-world breach data.

This is my first Python project, built to apply core programming concepts while exploring practical cybersecurity fundamentals such as hashing, API integration, and defensive validation logic.

## Features

### Composition Requirements
The password must:

- Be at least 8 characters long  
- Contain at least one uppercase letter  
- Contain at least one lowercase letter  
- Contain at least one number  
- Contain at least one special character  
- Not contain spaces  

### Breach Detection

The program checks whether a password has appeared in known data breaches using the **Have I Been Pwned (HIBP) Pwned Passwords API**.

It uses the k-anonymity model:

- The password is hashed locally using SHA-1.
- Only the first 5 characters of the hash are sent to the API.
- The full password is never transmitted.

### User Guidance

After 3 failed attempts, the program provides structured suggestions for creating stronger passwords using memorable phrases.

## Requirements

- Python 3.8+
- `requests` library

## How to Run

1. Download this repository.

2. Navigate to the project folder.

3. Install the required dependency:

pip install requests

4. Run the script:

python Password_Checker.py

5. Enter a password when prompted.

*An internet connection is required for breach detection.

## Disclaimer

This project is intended for educational and demonstration purposes. It is not designed to replace production-grade authentication systems or enterprise password validation tools.
