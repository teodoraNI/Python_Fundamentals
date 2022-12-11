pieces_num = int(input())
pieces = {}
for _ in range(pieces_num):
    piece, composer, key = input().split('|')
    pieces[piece] = [composer, key]
while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Add':
        piece, composer, key  = command[1], command[2], command[3]
        if piece in pieces:
            print(f'{piece} is already in the collection!')
        else:
            pieces[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
    elif command[0] == 'Remove':
        piece = command[1]
        if piece in pieces:
            del pieces[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif command[0] == 'ChangeKey':
        piece, new_key = command[1], command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
for piece, value in pieces.items():
    print(f'{piece} -> Composer: {pieces[piece][0]}, Key: {pieces[piece][1]}')

