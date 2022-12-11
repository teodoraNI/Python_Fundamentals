def tribonachi_sequence(n):
    tribonachi_sequence = [1]
    if n <= 3:
        for i in range(1,n):
            new_member = sum(tribonachi_sequence[0:i])
            tribonachi_sequence.append(new_member)
        return (tribonachi_sequence)
    else:
        tribonachi_sequence = [1, 1, 2]
        for i in range(3,n):
            new_member = sum(tribonachi_sequence[i-3:i])
            tribonachi_sequence.append(new_member)
        return(tribonachi_sequence)

num = int(input())
result = tribonachi_sequence(num)
print(*result)