# from math import sqrt
# from math import floor
#
# def defining_cathetus_length(a,b):
#     if a >=0 and b >= 0 or a < 0 and b < 0:
#         if abs(a) >= abs(b):
#             cathetus = abs(a) - abs(b)
#         else: cathetus = abs(b) - abs(a)
#     else:
#         cathetus = abs(a) + abs(b)
#     return cathetus
#
#
# def line_length_calc(cath1, cath2):
#     line_length = sqrt(cath1 * cath1 + cath2 * cath2)
#     return line_length
#
#
# def closer_to_center(x1, y1, x2, y2):
#     if sqrt(x1 * x1 + y1 * y1) <= sqrt(x2 * x2 + y2 * y2):
#         return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
#     else:
#         return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
#
# def longer_line(x1,y1,x2,y2,x3,y3,x4,y4):
#     cathetus1 = defining_cathetus_length(x1,x2)
#     cathetus2 = defining_cathetus_length(y1,y2)
#     length_line1 = line_length_calc(cathetus1,cathetus2)
#     cathetus3 = defining_cathetus_length(x3,x4)
#     cathetus4 = defining_cathetus_length(y3,y4)
#     length_line2 = line_length_calc(cathetus3,cathetus4)
#     if length_line1 >= length_line2:
#         result = closer_to_center(x1,y1,x2,y2)
#     else:
#         result = closer_to_center(x3,y3,x4,y4)
#     return(result)
#
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x3 = float(input())
# y3 = float(input())
# x4 = float(input())
# y4 = float(input())
# result = longer_line(x1,y1,x2,y2,x3,y3,x4,y4)
# print(result)


