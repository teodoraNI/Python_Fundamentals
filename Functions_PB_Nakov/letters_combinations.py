start_letter = input()
final_letter = input()
excluded_letter = input()
counter = 0
for a in range(ord(start_letter), ord(final_letter) + 1):
    if chr(a) != excluded_letter:
        for b in range(ord(start_letter), ord(final_letter) + 1):
            if chr(b) != excluded_letter:
                for c in range(ord(start_letter), ord(final_letter) + 1):
                    if chr(c) != excluded_letter:
                        counter += 1
                        print(f"{chr(a)}{chr(b)}{chr(c)} ", end='')
print(counter)

