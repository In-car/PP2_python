import pygame
import random



pygame.init()



WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")



#colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)



#snake settings
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_dir = (GRID_SIZE, 0)
speed = 10
score = 0
level = 1



#generate food avoiding snake
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        if (x, y) not in snake:
            return x, y



food = generate_food()



#game loop
running = True
clock = pygame.time.Clock()



while running:
    screen.fill(WHITE)



    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)



    #move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])



    #check collisions
    if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        running = False  # Game over



    #check if food is eaten
    if new_head == food:
        score += 1
        food = generate_food()
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()



    #update snake
    snake.insert(0, new_head)

    #draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))



    #draw food
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))



    #draw score and level
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))



    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
