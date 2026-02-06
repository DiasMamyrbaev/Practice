n = int(input())
def is_prime(n):
    if n < 2: 
        return "NO"
    for i in range(2, n):
        if n % i == 0:
            return "NO"
    return "YES"

print(is_prime(n))