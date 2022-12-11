string_to_be_removed = input()
string_to_be_matched = input()
while string_to_be_removed in string_to_be_matched:
    string_to_be_matched = string_to_be_matched.replace(string_to_be_removed, "")
print(string_to_be_matched)
