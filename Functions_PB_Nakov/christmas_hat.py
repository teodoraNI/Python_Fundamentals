n= int(input())

print((2*n - 1) * '.', '/|', '\\', (2*n - 1) * '.', sep='')
print((2*n - 1) * '.', '\|', '/', (2*n - 1) * '.',sep='')
for row in range(2 * n):
    print((2*n - 1 - row) * '.' + '*' + row * '-' + '*' + row * '-' + '*' + (2*n - 1 - row) * '.')
print((4*n + 1) * "*")
print((2*n) * '*.' + '*')
print((4*n + 1) * "*")





