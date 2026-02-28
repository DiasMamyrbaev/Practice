import sys

def divisible_by_3_and_4(n):
    for i in range(0, n + 1, 12):
        yield i ** 2

def main():
    n = int(sys.stdin.readline().strip())
    gen = divisible_by_3_and_4(n)
    
    first = next(gen)
    sys.stdout.write(str(first))
    
    for num in gen:
        sys.stdout.write(' ' + str(num))

if __name__ == "__main__":
    main()