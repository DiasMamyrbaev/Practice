import pygame
import math

def get_color(index, color_mode):
    idx = index % 256 
    c1 = max(0, min(255, 2 * idx - 256))
    c2 = max(0, min(255, 2 * idx))
    
    if color_mode == 'blue': return (c1, c1, c2)
    elif color_mode == 'red': return (c2, c1, c1)
    elif color_mode == 'green': return (c1, c2, c1)
    return (255, 255, 255) # Default white color

def drawLineBetween(surface, start, end, width, color):

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

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Extended Paint")
    
    canvas = pygame.Surface((800, 600))
    canvas.fill((0, 0, 0))
    

    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Verdana", 14)
    
    brush_size = 15
    mode = 'blue'       
    tool = 'brush'

    drawing = False
    start_pos = None
    last_pos = None
    color_index = 0     
    

    while True:
        pressed = pygame.key.get_pressed()
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return # Ctrl+W to exit
                if event.key == pygame.K_ESCAPE: return          # ESC to exit
                

                if event.key == pygame.K_UP: 
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
                elif event.key == pygame.K_e: tool = 'eraser'
                

                elif event.key == pygame.K_c: canvas.fill((0, 0, 0)) 
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                elif event.button == 4: 
                    brush_size = min(200, brush_size + 2)
                elif event.button == 5:
                    brush_size = max(1, brush_size - 2)
            

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    color = get_color(255, mode)
                    

                    if tool == 'rect' and start_pos:
                        rect_w = event.pos[0] - start_pos[0]
                        rect_h = event.pos[1] - start_pos[1]
                        pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], rect_w, rect_h), brush_size)
                    elif tool == 'circle' and start_pos:
                        dist = math.hypot(event.pos[0] - start_pos[0], event.pos[1] - start_pos[1])
                        pygame.draw.circle(canvas, color, start_pos, int(dist), brush_size)
                    
         
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
        

        if drawing and start_pos:
            mouse_pos = pygame.mouse.get_pos()
            color = get_color(255, mode)
            
            if tool == 'rect':
                rect_w = mouse_pos[0] - start_pos[0]
                rect_h = mouse_pos[1] - start_pos[1]
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], rect_w, rect_h), brush_size)
            elif tool == 'circle':
                dist = math.hypot(mouse_pos[0] - start_pos[0], mouse_pos[1] - start_pos[1])
                pygame.draw.circle(screen, color, start_pos, int(dist), brush_size)
            elif tool in ['square', 'right_tri', 'equi_tri', 'rhombus']:
                draw_custom_shape(screen, tool, color, start_pos, mouse_pos, brush_size)


        ui_bg = pygame.Surface((800, 30))
        ui_bg.set_alpha(180) 
        screen.blit(ui_bg, (0, 0))
        
        ui_text = font.render(f"Tool: {tool} (1-7) | Color: {mode} (RGB) | Size: {brush_size} | Arrows UP/DOWN to change size", True, (255, 255, 255))
        screen.blit(ui_text, (10, 5))
        
        pygame.display.flip()
        
        clock.tick(60)

if __name__ == '__main__':
    main()

