import sys

def solve():
    # Чтение входных данных
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        x1, y1 = map(float, line1)
        
        line2 = sys.stdin.readline().split()
        if not line2: return
        x2, y2 = map(float, line2)
    except EOFError:
        return

    # Если обе точки лежат по одну сторону от оси, используем стандартную формулу.
    # Если они по разные стороны, луч пройдет напрямую, но задача 
    # подразумевает отражение от зеркала, поэтому берем абсолютные значения y.
    ay1, ay2 = abs(y1), abs(y2)
    
    # Формула подобия треугольников:
    # x = x1 + (x2 - x1) * (y1 / (y1 + y2))
    res_x = x1 + (x2 - x1) * ay1 / (ay1 + ay2)
    
    # Вывод с заданной точностью
    print(f"{res_x:.10f} {0.0:.10f}")

if __name__ == "__main__":
    solve()