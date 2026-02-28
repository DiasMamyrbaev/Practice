import math
import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        r = float(line1.strip())
        x1, y1 = map(float, sys.stdin.readline().split())
        x2, y2 = map(float, sys.stdin.readline().split())
    except EOFError:
        return

    # Расстояния до центра
    d1 = math.sqrt(x1**2 + y1**2)
    d2 = math.sqrt(x2**2 + y2**2)
    
    # Расстояние между точками
    dist_ab = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    # Угол между OA и OB через скалярное произведение
    dot_product = x1*x2 + y1*y2
    # Ограничиваем значение для acos из-за точности
    cos_gamma = max(-1.0, min(1.0, dot_product / (d1 * d2)))
    gamma = math.acos(cos_gamma)
    
    # Проверка: пересекает ли отрезок круг?
    # Высота в треугольнике OAB
    h = abs(x1*y2 - x2*y1) / dist_ab
    
    # Проверяем, падает ли высота на отрезок
    # Углы при основании A и B должны быть острыми
    is_intersect = False
    if h < r - 1e-9:
        # Угол между OA и AB
        dot_a = (x2-x1)*(-x1) + (y2-y1)*(-y1)
        # Угол между OB и BA
        dot_b = (x1-x2)*(-x2) + (y1-y2)*(-y2)
        if dot_a > 0 and dot_b > 0:
            is_intersect = True

    if not is_intersect:
        print(f"{dist_ab:.10f}")
    else:
        # Путь в обход
        l1 = math.sqrt(max(0, d1**2 - r**2))
        l2 = math.sqrt(max(0, d2**2 - r**2))
        
        alpha1 = math.acos(min(1.0, r / d1))
        alpha2 = math.acos(min(1.0, r / d2))
        
        phi = gamma - alpha1 - alpha2
        l_arc = r * max(0, phi)
        
        print(f"{l1 + l2 + l_arc:.10f}")

solve()