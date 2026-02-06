import math
n = int(input())
numbers = list(map(int, input().split()))
zero = -10000000
j = 0
for i in range(len(numbers)):
    if zero >= numbers[i]:
        zero = numbers[i]
    j += 1
print(j-1)