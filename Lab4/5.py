import sys

def Down(n):
    for i in range(n,-1,-1):
        yield i

def main():
    n = int(input().strip())
    
    for i in Down(n):
        print(i)

if __name__ == "__main__":
    main()