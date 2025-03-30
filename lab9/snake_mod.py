import pygame
import random

pygame.init()



#screen settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")



#colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

running = True 
font = pygame.font.SysFont(None, 30)



def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        if (x, y) not in snake:
            return x, y, random.choice([1, 2, 3])



def reset_game():
    global snake, snake_dir, speed, score, level, food_x, food_y, food_weight, food_timer, running, game_over
    snake = [(WIDTH // 2, HEIGHT // 2)]
    snake_dir = (GRID_SIZE, 0)
    speed = 10
    score = 0
    level = 1
    food_x, food_y, food_weight = generate_food(snake)
    food_timer = 100
    game_over = False



reset_game()
clock = pygame.time.Clock()



while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                    snake_dir = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                    snake_dir = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                    snake_dir = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                    snake_dir = (GRID_SIZE, 0)
            if game_over and event.key == pygame.K_SPACE:
                reset_game()
    


    if not game_over:
        new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        
        if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            game_over = True
        else:
            if new_head == (food_x, food_y):
                score += food_weight
                food_x, food_y, food_weight = generate_food(snake)
                food_timer = 100
                if score % 3 == 0:
                    level += 1
                    speed += 2
            else:
                snake.pop()
            
            food_timer -= 1
            if food_timer <= 0:
                food_x, food_y, food_weight = generate_food(snake)
                food_timer = 100
            
            snake.insert(0, new_head)
    


    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
    
    pygame.draw.rect(screen, RED, (food_x, food_y, GRID_SIZE * food_weight // 3, GRID_SIZE * food_weight // 3))
    


    score_text = font.render(f"Score: {score}  Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    

    
    if game_over:
        game_over_text = font.render("You lost, to restart press Space", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 120, HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
