n = int(input())

numbers = list(map(int, input().split()))
positive = 0
for i in numbers:
    if i > 0:
        positive += 1
print(positive)