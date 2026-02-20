def solve():
    try:
        line = input().split()
        if not line: return
        n = int(line[0])
    except EOFError:
        return

    first_occurrences = {}
    
    for i in range(1, n + 1):
        s = input().strip()
        if s not in first_occurrences:
            first_occurrences[s] = i
            
    unique_strings = sorted(first_occurrences.keys())
    
    for s in unique_strings:
        print(f"{s} {first_occurrences[s]}")

if __name__ == "__main__":
    solve()