import pygame
import math
import datetime
import os

# Импортируем все наши функции из соседнего файла tools.py
from tools import get_color, drawLineBetween, draw_custom_shape, flood_fill

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Extended Paint")
    
    canvas = pygame.Surface((800, 600))
    canvas.fill((0, 0, 0))
    
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Verdana", 14)
    text_font = pygame.font.SysFont("Verdana", 24) 
    
    brush_size = 15
    mode = 'blue'       
    tool = 'brush'

    drawing = False
    start_pos = None
    last_pos = None
    color_index = 0     
    
    typing = False
    current_text = ""
    text_pos = None

    while True:
        pressed = pygame.key.get_pressed()
        # Добавлена поддержка Cmd на macOS (K_LMETA / K_RMETA)
        ctrl_held = (pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL] or 
                     pressed[pygame.K_LMETA] or pressed[pygame.K_RMETA])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return # Ctrl/Cmd + W to exit
                if event.key == pygame.K_ESCAPE and not typing: return # ESC to exit
                
                # Сохранение (Ctrl/Cmd + S) в папку assets
                if event.key == pygame.K_s and ctrl_held:
                    # Получаем абсолютный путь к папке, в которой лежит paint.py
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    # Создаем точный путь к TSIS2/assets/
                    assets_dir = os.path.join(script_dir, "assets")
                    
                    if not os.path.exists(assets_dir):
                        os.makedirs(assets_dir)
                        
                    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    file_path = os.path.join(assets_dir, f"canvas_{now}.png")
                    
                    pygame.image.save(canvas, file_path)
                    print(f"Успешно сохранено в: {file_path}") 
                    continue

                if typing:
                    if event.key == pygame.K_RETURN:
                        if current_text:
                            color = get_color(255, mode)
                            rendered = text_font.render(current_text, True, color)
                            canvas.blit(rendered, text_pos)
                        typing = False
                        current_text = ""
                    elif event.key == pygame.K_ESCAPE:
                        typing = False
                        current_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        current_text = current_text[:-1]
                    else:
                        current_text += event.unicode
                    continue 
                
                if event.key == pygame.K_8: brush_size = 2   
                elif event.key == pygame.K_9: brush_size = 5 
                elif event.key == pygame.K_0: brush_size = 10 
                
                elif event.key == pygame.K_UP: 
                    brush_size = min(200, brush_size + 2)
                elif event.key == pygame.K_DOWN: 
                    brush_size = max(1, brush_size - 2) 

                elif event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
                elif event.key == pygame.K_1: tool = 'brush'
                elif event.key == pygame.K_2: tool = 'rect'
                elif event.key == pygame.K_3: tool = 'circle'
                elif event.key == pygame.K_4: tool = 'square'
                elif event.key == pygame.K_5: tool = 'right_tri'
                elif event.key == pygame.K_6: tool = 'equi_tri'
                elif event.key == pygame.K_7: tool = 'rhombus'
                elif event.key == pygame.K_l: tool = 'line'    
                elif event.key == pygame.K_f: tool = 'fill'    
                elif event.key == pygame.K_t: tool = 'text'    
                elif event.key == pygame.K_e: tool = 'eraser'
                
                elif event.key == pygame.K_c: canvas.fill((0, 0, 0)) 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tool == 'text':
                        typing = True
                        current_text = ""
                        text_pos = event.pos
                    elif tool == 'fill':
                        color = get_color(255, mode)
                        flood_fill(canvas, event.pos, color)
                    else:
                        drawing = True
                        start_pos = event.pos
                        last_pos = event.pos
                elif event.button == 4: 
                    brush_size = min(200, brush_size + 2)
                elif event.button == 5:
                    brush_size = max(1, brush_size - 2)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    color = get_color(255, mode)
                    
                    if tool == 'rect' and start_pos:
                        rect_w = event.pos[0] - start_pos[0]
                        rect_h = event.pos[1] - start_pos[1]
                        pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], rect_w, rect_h), brush_size)
                    elif tool == 'circle' and start_pos:
                        dist = math.hypot(event.pos[0] - start_pos[0], event.pos[1] - start_pos[1])
                        pygame.draw.circle(canvas, color, start_pos, int(dist), brush_size)
                    elif tool == 'line' and start_pos:
                        pygame.draw.line(canvas, color, start_pos, event.pos, brush_size)
                    elif tool in ['square', 'right_tri', 'equi_tri', 'rhombus'] and start_pos:
                        draw_custom_shape(canvas, tool, color, start_pos, event.pos, brush_size)
                    
                    start_pos = None
                    last_pos = None
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'brush':
                        color = get_color(color_index, mode)
                        drawLineBetween(canvas, last_pos, event.pos, brush_size, color)
                        color_index += 1 
                        last_pos = event.pos
                    elif tool == 'eraser':
                        drawLineBetween(canvas, last_pos, event.pos, brush_size, (0, 0, 0))
                        last_pos = event.pos
        
        screen.blit(canvas, (0, 0))
        
        color = get_color(255, mode)
        if drawing and start_pos:
            mouse_pos = pygame.mouse.get_pos()
            
            if tool == 'rect':
                rect_w = mouse_pos[0] - start_pos[0]
                rect_h = mouse_pos[1] - start_pos[1]
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], rect_w, rect_h), brush_size)
            elif tool == 'circle':
                dist = math.hypot(mouse_pos[0] - start_pos[0], mouse_pos[1] - start_pos[1])
                pygame.draw.circle(screen, color, start_pos, int(dist), brush_size)
            elif tool == 'line':
                pygame.draw.line(screen, color, start_pos, mouse_pos, brush_size)
            elif tool in ['square', 'right_tri', 'equi_tri', 'rhombus']:
                draw_custom_shape(screen, tool, color, start_pos, mouse_pos, brush_size)

        if typing and text_pos:
            cursor = "|" if pygame.time.get_ticks() % 1000 < 500 else ""
            rendered = text_font.render(current_text + cursor, True, color)
            screen.blit(rendered, text_pos)

        ui_bg = pygame.Surface((800, 30))
        ui_bg.set_alpha(180) 
        screen.blit(ui_bg, (0, 0))
        
        ui_text = font.render(f"Tool: {tool} (L=Line, F=Fill, T=Text) | Size: {brush_size} | Cmd+S: Save", True, (255, 255, 255))
        screen.blit(ui_text, (10, 5))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
