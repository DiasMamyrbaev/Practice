n = int(input())
numbers = list(map(int,input().split()))
max_index = numbers.index(max(numbers))
print(max_index + 1)