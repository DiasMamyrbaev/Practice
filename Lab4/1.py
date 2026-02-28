n = int(input())

def power2_of_n(n):
    for i in range(1,n+1):
        yield i * i

for j in power2_of_n(n):
    print(j)