# Password Strength Checker Program
def check_password_strength(password):
    # Initialize strength score
    score = 0
    # Length check
    if len(password) >= 8:
        score += 1
    # Uppercase letter check
    if any(char.isupper() for char in password):
        score += 1
    # Lowercase letter check
    if any(char.islower() for char in password):
        score += 1
    # Digit check
    if any(char.isdigit() for char in password):
        score += 1
    # Special character check
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(char in special_chars for char in password):
        score += 1
    # Evaluation
    if score == 5:
        return "Strong password!"
    elif score >= 3:
        return "Medium password - consider adding special characters or numbers."
    else:
        return "Weak password - must be at least 8 characters with mixed types."
# Main execution block
if __name__ == "__main__":
    user_input = input("Enter a password to test: ")
    result = check_password_strength(user_input)
    print(f"Strength Result: {result}")