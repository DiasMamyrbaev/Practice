def squares_n_m(n, m):
    for i in range(n, m+1):
        yield i ** 2

a = int(input())
b = int(input())

for j in squares_n_m(a, b):
    print(j)