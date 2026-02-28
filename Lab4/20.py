import sys

def solve():
    # Читаем все входные данные сразу
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m = int(input_data[0])
    g = 0
    n = 0
    
    # Итерируемся по парам (команда, значение)
    # Начинаем с индекса 1, шаг 2
    for i in range(1, 2 * m, 2):
        scope = input_data[i]
        value = int(input_data[i+1])
        
        if scope == "global":
            g += value
        elif scope == "nonlocal":
            n += value
        # Случай "local" просто пропускаем
            
    print(f"{g} {n}")

if __name__ == "__main__":
    solve()