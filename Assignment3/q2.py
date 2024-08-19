def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_digit:
        return "Password must contain at least one numeric digit."
    
    return "Password is valid."

password = input("Enter your password: ")
print(validate_password(password))
