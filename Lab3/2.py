def is_usual(n):
    if n <= 0:
        return False
    
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1

try:
    num = int(input())
    if is_usual(num):
        print("Yes")
    else:
        print("No")
except ValueError:
    print("Please, enter an integer")