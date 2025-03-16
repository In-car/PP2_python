import pygame
import time
from datetime import datetime


pygame.init()

WIDTH, HEIGHT = 350 , 320

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")


clock_img = pygame.image.load("images/mickeyclock.jpeg") 
right_hand_img = pygame.image.load("images/righthand.png")  
left_hand_img = pygame.image.load("images/lefthand.png")


hand_size = (150,120)
right_hand_img = pygame.transform.scale(right_hand_img, hand_size)
left_hand_img = pygame.transform.scale(left_hand_img, hand_size)


center_x, center_y = WIDTH // 2, HEIGHT // 2

def rotate_hand(image, angle, offset_x, offset_y):
    """Rotate the hand around the clock center."""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(center_x + offset_x, center_y + offset_y))
    return rotated_image, new_rect.topleft


running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0)) 


    now = datetime.now()
    minutes = now.minute
    seconds = now.second


    minute_angle = - (minutes * 6) 
    second_angle = - (seconds * 6)


    rotated_minute, min_pos = rotate_hand(right_hand_img, minute_angle, 0, 0)
    rotated_second, sec_pos = rotate_hand(left_hand_img, second_angle, 0, 0)

 
    screen.blit(rotated_minute, min_pos)
    screen.blit(rotated_second, sec_pos)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    time.sleep(1)

pygame.quit()