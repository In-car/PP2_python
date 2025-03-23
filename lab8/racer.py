import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()



#colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)



#car settings
car_width, car_height = 50, 90
car_x, car_y = WIDTH // 2 - car_width // 2, HEIGHT - 120
car_speed = 5



#obstacles & Coins
obstacle_width, obstacle_height = 50, 90
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5



coin_size = 30
coin_x = random.randint(0, WIDTH - coin_size)
coin_y = -coin_size
coin_speed = 5
coins_collected = 0



font = pygame.font.Font(None, 36)
running = True



while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    #move car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed
    


    #move obstacles
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
    


    #move coins
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -coin_size
        coin_x = random.randint(0, WIDTH - coin_size)
    


    #check collision with coins
    if (car_x < coin_x < car_x + car_width or car_x < coin_x + coin_size < car_x + car_width) and (car_y < coin_y < car_y + car_height):
        coins_collected += 1
        coin_y = -coin_size
        coin_x = random.randint(0, WIDTH - coin_size)
    


    #draw car
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))
    


    #draw obstacles
    pygame.draw.rect(screen, (0, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    


    #draw coins
    pygame.draw.circle(screen, YELLOW, (coin_x + coin_size // 2, coin_y + coin_size // 2), coin_size // 2)
    


    #display score
    score_text = font.render(f'Coins: {coins_collected}', True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 120, 10))
    


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
