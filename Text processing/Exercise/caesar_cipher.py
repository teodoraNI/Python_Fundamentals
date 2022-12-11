list_chars = list(input())
encrypted_text = [chr(ord(char) + 3) for char in list_chars]
print(*encrypted_text, sep='')
