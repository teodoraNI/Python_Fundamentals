def palindrome_check(list):
    for item in list:
        if item[0:] == item[::-1]:
            print('True')
        else:
            print('False')


my_list = input().split(', ')
palindrome_check(my_list)








