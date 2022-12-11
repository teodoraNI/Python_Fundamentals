books = input(). split('&')
command = input()
while command != 'Done':
    action, *data = [int(item) if item.isnumeric() else item for item in command.split(' | ')]
    if action == 'Add Book':
        if data[0] not in books:
            books.insert(0, data[0])
    elif action == 'Take Book':
        if data[0] in books:
            books.remove(data[0])
    elif action == 'Insert Book':
        if data[0] not in books:
            books.append(data[0])
    elif action == 'Check Book':
        if 0 <= data[0] < len(books):
            print(f'{books[data[0]]}')
    elif action == 'Swap Books':
        if data[0] in books and data[1] in books:
            ind1 = books.index(data[0])
            ind2 = books.index(data[1])
            books[ind1], books[ind2] = books[ind2], books[ind1]
    command = input()
print(*books, sep=', ')
