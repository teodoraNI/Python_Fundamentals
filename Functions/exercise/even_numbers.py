my_list = list(map(int,input().split()))
result = filter(lambda x: x % 2 == 0, my_list)
print(list(result))

