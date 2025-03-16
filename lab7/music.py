import pygame
import os


pygame.init()
pygame.mixer.init()

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

font = pygame.font.SysFont("comicsansms", 24)
text = font.render("P-play , B-go back , Q-quit , S-stop, N-next" ,True, (0, 128, 0))


MUSIC_FOLDER = "lab7\music" 


songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
if not songs:
    print("No MP3 files found in the folder.")
    exit()


songs.sort()


current_song = 0


def play_song(index):
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[index]))
    pygame.mixer.music.play()
    print(f"Now Playing: {songs[index]}")


play_song(current_song)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_p]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            print("Paused")
        else:
            pygame.mixer.music.unpause()
            print("Resumed")

    if keys[pygame.K_s]:
        pygame.mixer.music.stop()
        print("Stopped")

    if keys[pygame.K_n]:
        current_song = (current_song + 1) % len(songs)
        play_song(current_song)

    if keys[pygame.K_b]:
        current_song = (current_song - 1) % len(songs)
        play_song(current_song)

    if keys[pygame.K_q]:
        running = False

    screen.fill((255, 255, 255))
    screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
   
    pygame.display.update()  


pygame.mixer.music.stop()
pygame.quit()