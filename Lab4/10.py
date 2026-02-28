import sys

def limited_cycle(elements, k):
    for _ in range(k):
        for elem in elements:
            yield elem

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    elements = data[0].split()

    k = int(data[1]) if len(data) > 1 else 0

    out = sys.stdout
    first = True
    for item in limited_cycle(elements, k):
        if first:
            out.write(item)
            first = False
        else:
            out.write(' ' + item)


if __name__ == "__main__":
    main()