import pygame
import math

def get_color(index, color_mode):
    """Вычисляет текущий цвет в зависимости от выбранного режима."""
    idx = index % 256 
    c1 = max(0, min(255, 2 * idx - 256))
    c2 = max(0, min(255, 2 * idx))
    
    if color_mode == 'blue': return (c1, c1, c2)
    elif color_mode == 'red': return (c2, c1, c1)
    elif color_mode == 'green': return (c1, c2, c1)
    return (255, 255, 255) 

def drawLineBetween(surface, start, end, width, color):
    """Отрисовывает плавную линию между двумя точками для кисти и ластика."""
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    
    iterations = max(abs(dx), abs(dy))
    
    if iterations == 0:
        pygame.draw.circle(surface, color, start, width)
        return
        
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

def draw_custom_shape(surface, tool, color, start_pos, end_pos, brush_size):
    """Отрисовывает кастомные геометрические фигуры."""
    sx, sy = start_pos
    ex, ey = end_pos
    w = ex - sx
    h = ey - sy
    
    if tool == 'square':
        size = max(abs(w), abs(h))
        sign_x = 1 if w > 0 else -1
        sign_y = 1 if h > 0 else -1
        pygame.draw.rect(surface, color, (sx, sy, size * sign_x, size * sign_y), brush_size)
        
    elif tool == 'right_tri':
        points = [(sx, sy), (sx, ey), (ex, ey)]
        pygame.draw.polygon(surface, color, points, brush_size)
        
    elif tool == 'equi_tri':
        mid_x = sx + w / 2
        points = [(mid_x, sy), (sx, ey), (ex, ey)]
        pygame.draw.polygon(surface, color, points, brush_size)
        
    elif tool == 'rhombus':
        mid_x = sx + w / 2
        mid_y = sy + h / 2
        points = [(mid_x, sy), (ex, mid_y), (mid_x, ey), (sx, mid_y)]
        pygame.draw.polygon(surface, color, points, brush_size)

def flood_fill(surface, pos, fill_color):
    """Собственная реализация Flood-fill с использованием get_at и set_at."""
    target_color = surface.get_at(pos)[:3] 
    fill_color = fill_color[:3]
    
    if target_color == fill_color:
        return
        
    w, h = surface.get_size()
    stack = [pos]
    visited = set([pos])
    
    while stack:
        x, y = stack.pop()
        surface.set_at((x, y), fill_color)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                if (nx, ny) not in visited:
                    if surface.get_at((nx, ny))[:3] == target_color:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
                        