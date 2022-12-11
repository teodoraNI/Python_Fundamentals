morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'
                    }
words = input().split(' | ')
decrypted_message = []

for word in words:
    letters = word.split()
    decrypted_word = ''
    for letter in letters:
        decrypted_word += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(letter)]
    decrypted_message.append(decrypted_word)
print(*decrypted_message)
