words = input().split(' ')
palindrome = input()
palindrome_lst = [word for word in words if word == word[::-1]]
counter = palindrome_lst.count(palindrome)
print(palindrome_lst)
print(f'Found palindrome {counter} times')