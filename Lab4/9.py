import sys

def powers_of_two(n):
    for i in range(n+1):
        yield 2 ** i
    
def main():
    n = int(sys.stdin.readline().strip())
    gen = powers_of_two(n)

    first = next(gen)
    sys.stdout.write(str(first))

    for n in gen:
        sys.stdout.write(" " + str(n))

if __name__ == "__main__":
    main()