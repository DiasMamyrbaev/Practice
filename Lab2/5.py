n = int(input())
a = True
while n % 2 == 0:
    n //= 2
    a = True
else:
    a = False

if a:
    print("YES")
else:
    print("NO")