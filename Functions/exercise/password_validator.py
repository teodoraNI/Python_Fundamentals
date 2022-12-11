def password_validator(password:str):
    warnings = []
    counter_digits = 0
    for item in password:
        if item.isdigit():
            counter_digits += 1
    if len(password) > 10 or len(password) < 6:
        warnings.append("Password must be between 6 and 10 characters")
    if password.isalnum() == False:
        warnings.append("Password must consist only of letters and digits")
    if counter_digits < 2:
        warnings.append("Password must have at least 2 digits")
    if warnings == []:
        warnings.append('Password is valid')
    return warnings


password = input()
result = password_validator(password)
print(*result, sep='\n')

