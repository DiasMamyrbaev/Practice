def squares_n(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input())

for sq in squares_n(n):
    print(sq)