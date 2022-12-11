from math import sqrt
from math import floor


def closer_to_center(x1, y1, x2, y2):
    if sqrt(x1 * x1 + y1 * y1) <= sqrt(x2 * x2 + y2 * y2):
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
result = closer_to_center(x1, y1, x2, y2)
print(result)
