import sys
import math

def prime_generator(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

def main():
    n = int(sys.stdin.readline().strip())
    gen = prime_generator(n)
    
    first = True
    for p in gen:
        if first:
            sys.stdout.write(str(p))
            first = False
        else:
            sys.stdout.write(' ' + str(p))
    sys.stdout.write('\n') 

if __name__ == "__main__":
    main()