import re

messages_number = int(input())
attacked_planets = []
destroyed_planets = []
for i in range(messages_number):
    encrypted_message = input()
    key = len(re.findall('[star]', encrypted_message.lower()))
    decrypted_message = ''
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - key)
    pattern = r'@([A-Za-z]+)[^@\-\!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-\!:>]*->(\d+)'
    match = re.search(pattern, decrypted_message, re.IGNORECASE)
    if match:
        planet_name, attack_type = match.group(1), match.group(3)
        if attack_type == 'A':
            attacked_planets.append(planet_name)
        elif attack_type == 'D':
            destroyed_planets.append(planet_name)
print(f'Attacked planets: {len(attacked_planets)}')
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
