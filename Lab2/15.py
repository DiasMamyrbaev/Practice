n = int(input())
surnames = []
for i in range(n):
    surnames.append(input().strip())

print(len(set(surnames)))