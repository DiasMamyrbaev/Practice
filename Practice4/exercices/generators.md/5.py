def down_sequens(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for i in down_sequens(n):
    print(i)
