n = int(input())
arr = []
power = 1
while power <= n:
    arr.append(power)
    power <<= 1

print(*arr)