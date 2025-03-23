import pygame



pygame.init()



WIDTH, HEIGHT = 800, 600
TOOLBAR_HEIGHT = 40 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [BLACK, RED, BLUE, GREEN]



current_color = BLACK
drawing = False
tool = "circle"
font = pygame.font.SysFont(None, 30)



#main loop
running = True
clock = pygame.time.Clock()

screen.fill(WHITE) 

def draw_toolbar():
    """Draws the toolbar with instructions and current tool info."""
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, TOOLBAR_HEIGHT))
    text = f"Tool: {tool.capitalize()} | Color: {current_color} | [R] Rectangle  [C] Circle  [E] Eraser  [1-4] Colors"
    label = font.render(text, True, BLACK)
    screen.blit(label, (10, 10))

while running:


    screen.fill(WHITE, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    draw_toolbar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        #mouse events
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] > TOOLBAR_HEIGHT:
            drawing = True
            start_pos = event.pos



        elif event.type == pygame.MOUSEBUTTONUP and event.pos[1] > TOOLBAR_HEIGHT:
            drawing = False
            end_pos = event.pos



            if tool == "rectangle":
                pygame.draw.rect(screen, current_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif tool == "circle":
                radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 // 2
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(screen, current_color, center, int(radius), 2)
            elif tool == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, 10)
            else:
                pygame.draw.line(screen, current_color, last_pos, event.pos, 3)
            last_pos = event.pos



        #keyboard events for tool selection
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
                current_color = WHITE
            elif event.key == pygame.K_1:
                current_color = COLORS[0]
            elif event.key == pygame.K_2:
                current_color = COLORS[1]
            elif event.key == pygame.K_3:
                current_color = COLORS[2]
            elif event.key == pygame.K_4:
                current_color = COLORS[3]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
