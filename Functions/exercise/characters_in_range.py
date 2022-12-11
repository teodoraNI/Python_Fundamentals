def returns_symbols(a:chr,b:chr):
    list = []
    for item in range(ord(a) + 1, ord(b)):
        list.append(chr(item))
    return(list)

initial_char = input()
final_char = input()
result = returns_symbols(initial_char,final_char)
print(' '.join(result))