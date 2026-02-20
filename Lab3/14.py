import sys

def solve():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        n = int(input_data[0])

        arr = list(map(int, input_data[1:n+1]))
        
        q_idx = n + 1
        q = int(input_data[q_idx])
        
        operations = []
        
        current = q_idx + 1
        ops_processed = 0
        while ops_processed < q:
            op_name = input_data[current]
            
            if op_name == "abs":
                operations.append(lambda a: abs(a))
                current += 1
            else:
                x = int(input_data[current + 1])
                if op_name == "add":
                    operations.append(lambda a, x=x: a + x)
                elif op_name == "multiply":
                    operations.append(lambda a, x=x: a * x)
                elif op_name == "power":
                    operations.append(lambda a, x=x: a ** x)
                current += 2
            ops_processed += 1

        result = []
        for val in arr:
            temp = val
            for op in operations:
                temp = op(temp)
            result.append(int(temp))

        print(*(result))

    except EOFError:
        pass

if __name__ == "__main__":
    solve()