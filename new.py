import pygame

pygame.init()
#color = (255,255,255)
position = (0,0)

scr = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Nice One")


image = pygame.image.load("C:\\Users\\Dell\\Pictures\\Screenshots\\Screenshot (828).png")
exit = False
while not exit:
    #scr.fill(color)
    scr.blit(image,dest=position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()