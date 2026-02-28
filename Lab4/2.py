import sys

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    n = int(sys.stdin.readline().strip())
    gen = even_numbers(n)

    first = next(gen)
    sys.stdout.write(str(first))
    
    for num in gen:
        sys.stdout.write(',' + str(num))

if __name__ == "__main__":
    main()