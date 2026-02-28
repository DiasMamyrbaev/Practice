import math

def solve():
    try:
        r = float(input())
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
    except EOFError:
        return

    dx = x2 - x1
    dy = y2 - y1
    
    # Квадратное уравнение: at^2 + bt + c = 0
    a = dx**2 + dy**2
    b = 2 * (x1 * dx + y1 * dy)
    c = x1**2 + y1**2 - r**2
    
    # Если точки A и B совпадают
    if a == 0:
        print(f"{r if x1**2 + y1**2 <= r**2 else 0:.10f}")
        return

    dist_ab = math.sqrt(a)
    d = b**2 - 4*a*c
    
    if d <= 0:
        # Прямая касается или не пересекает. 
        # Проверяем, не лежит ли весь (точечный) отрезок на границе
        print(f"{0.0:.10f}")
        return
    
    t1 = (-b - math.sqrt(d)) / (2 * a)
    t2 = (-b + math.sqrt(d)) / (2 * a)
    
    # Находим пересечение интервалов [t1, t2] и [0, 1]
    t_start = max(0, min(t1, t2))
    t_end = min(1, max(t1, t2))
    
    if t_start < t_end:
        result = (t_end - t_start) * dist_ab
        print(f"{result:.10f}")
    else:
        print(f"{0.0:.10f}")

solve()