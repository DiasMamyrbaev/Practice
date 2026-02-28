import sys

def square_generator(start, end):
    for i in range(start, end + 1):
        yield i * i

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    a, b = map(int, data[:2])
    
    for sq in square_generator(a, b):
        print(sq)

if __name__ == "__main__":
    main()