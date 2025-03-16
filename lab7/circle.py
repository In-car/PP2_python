import pygame 

pygame.init()
WIDTH,HEIGHT = 500,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
BALL_RADIUS = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2 
MOVE_SPEED = 20

screen_color = pygame.Color('White')
ball_color = pygame.Color('Red')

done = True 
while done :
        for event in pygame.event.get():
                if event.type == pygame.QUIT : 
                     done = False 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ball_x - BALL_RADIUS - MOVE_SPEED >= 0:
                ball_x -= MOVE_SPEED
        if keys[pygame.K_RIGHT] and ball_x + BALL_RADIUS + MOVE_SPEED <= WIDTH:
                ball_x += MOVE_SPEED
        if keys[pygame.K_UP] and ball_y - BALL_RADIUS - MOVE_SPEED >= 0:
                ball_y -= MOVE_SPEED
        if keys[pygame.K_DOWN] and ball_y + BALL_RADIUS + MOVE_SPEED <= HEIGHT:
                ball_y += MOVE_SPEED

        screen.fill(screen_color)  
        pygame.draw.circle(screen, ball_color , (ball_x, ball_y), BALL_RADIUS) 
        pygame.display.update()  
        
pygame.quit()