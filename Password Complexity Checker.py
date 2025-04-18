import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria Checks
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Strength Evaluation
    if strength == 5:
        return "Strong Password 💪", []
    elif strength >= 3:
        return "Moderate Password ⚠️", feedback
    else:
        return "Weak Password ❌", feedback


# Example Usage
user_input = input("Enter your password: ")
strength, tips = check_password_strength(user_input)

print("\nPassword Strength:", strength)
if tips:
    print("Suggestions to improve your password:")
    for tip in tips:
        print("-", tip)
