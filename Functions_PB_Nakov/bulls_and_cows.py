# secret_num = input()
# bulls = int(input())
# cows = int(input())
# solution_found = False
# for digit_1 in range(1, 10):
#     for digit_2 in range(1, 10):
#         for digit_3 in range(1, 10):
#             for digit_4 in range(1, 10):
#                 potential_num = str(digit_1) + str(digit_2) + str(digit_3) + str(digit_4)
#                 counter_bulls = 0
#                 counter_cows = 0
#                 for i in range(0, 4):
#                     for j in range(0, 4):
#                         if potential_num[i] == secret_num[j] and i == j:
#                             counter_bulls += 1
#                             break
#                         elif potential_num[i] == secret_num[j] and \
#                                 potential_num[j] != secret_num[j] and \
#                                 potential_num[i] != secret_num[i]:
#                             counter_cows += 1
#                             break
#                 if counter_bulls == bulls and counter_cows == cows:
#                     solution_found = True
#                     print(potential_num, end=' ')
#
# if not solution_found:
#     print("No")

