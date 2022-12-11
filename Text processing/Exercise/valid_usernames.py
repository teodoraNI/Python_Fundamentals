def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_valid(name):
    for char in name:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True

def no_redundant_symbols(name):
    if ' ' in name:
        return False
    return True

def name_validation(name):
    if (valid_length(name) and characters_valid(name) and no_redundant_symbols(name)):
        return True
    return False


usernames = input().split(', ')
for username in usernames:
    if name_validation(username):
        print(username)