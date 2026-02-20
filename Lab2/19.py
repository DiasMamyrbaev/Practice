import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    dorama_counts = {}

    for i in range(1, n + 1):
        line = input_data[i].split()
        if not line:
            continue
            
        name = line[0]
        episodes = int(line[1])
        
        if name in dorama_counts:
            dorama_counts[name] += episodes
        else:
            dorama_counts[name] = episodes

    sorted_names = sorted(dorama_counts.keys())

    for name in sorted_names:
        print(f"{name} {dorama_counts[name]}")

if __name__ == "__main__":
    solve()