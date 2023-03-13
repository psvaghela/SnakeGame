import pygame
pygame.init()

screen_length = 900
screen_height = 600

# Create Game Window
gwindow = pygame.display.set_mode((screen_length,screen_height))

pygame.display.set_caption("PSV")
gwindow.fill((0,0,0))
pygame.display.update()

game_exit = False
fps = 60
clock = pygame.time.Clock()

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    clock.tick(fps)
    pygame.display.update()