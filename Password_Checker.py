import time
import hashlib
import requests
import string

print("Hey there, let's see if your password is strong.")
time.sleep(1)
password_is_strong = False

MAX_TRIES = 3
tries = 0

def is_pwned(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")

    hashes = (line.split(":") for line in response.text.splitlines())
    return any(suffix == h for h, count in hashes)

while not password_is_strong:
    user_input = input("Type your password: ")
    
    has_number = False
    has_upper = False
    has_lower = False
    has_special = False

    for char in user_input:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True

        import string
        if char in string.punctuation:
            has_special = True

    issues = []

    if is_pwned(user_input):
        issues.append("• Password has appeared in a data breach")

    if len(user_input) < 12:
        issues.append("• At least 12 characters required")

    if not has_number:
        issues.append("• At least one number required")

    if not has_upper:
        issues.append("• At least one uppercase letter required")

    if not has_lower:
        issues.append("• At least one lowercase letter required")
    
    if not has_special:
        issues.append("• At least one special character required")
    
    if " " in user_input:
        issues.append("• Spaces are not allowed")

    if not issues:
        print("Well done! Your password is strong.")
        password_is_strong = True
    
    else:
        tries += 1
        print("Your password has the following issues:")
    
        for problem in issues:
            print(problem)
        print("Try again.\n")

        if tries >= MAX_TRIES:
            print("Here are a few suggestions for creating passwords:")
            print("  • Take a line from your favorite song")
            print("  • Add the year it was released")
            print("  • Add at least one special character (!, @, #, etc.)")
            print("Example: 'NovemberRain1992!' or 'BohemianRhapsody1975#'\n")