import sys

def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def main():
    n = int(sys.stdin.readline().strip())
    
    if not n:
        return
    if n <= 0:
        return
    
    gen = Fibonacci(n)

    first = next(gen)
    sys.stdout.write(str(first))
    
    for num in gen:
        sys.stdout.write(',' + str(num))

if __name__ == "__main__":
    main()