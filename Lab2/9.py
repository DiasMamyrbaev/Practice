n = int(input())
numbers = list(map(int,input().split()))
max_index = max(numbers)
min_index = min(numbers)
for i in range(len(numbers)):
    if numbers[i] == max_index:
        numbers[i] = min_index
print(*numbers)