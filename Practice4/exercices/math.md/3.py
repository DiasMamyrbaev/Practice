import math

sides = int(input())
side_length = int(input())
area = (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))

print(int(area))