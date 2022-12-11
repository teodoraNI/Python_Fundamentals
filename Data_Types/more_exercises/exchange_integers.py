a = int(input())
b = int(input())
print(f"Before:\na = {a} \nb = {b}")
transfer_var = a
a = b
b = transfer_var
print(f"After: \na = {a} \nb = {b}")