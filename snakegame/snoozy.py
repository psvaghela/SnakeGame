from tkinter.font import ROMAN
import pygame
from pygame import mixer
import random
pygame.init()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen_length = 800
screen_height = 500

# Create Game Window
gwindow = pygame.display.set_mode((screen_length,screen_height))

bgimg = pygame.image.load('E:\\PSV_vs\\snakegame\\gamebg.jpeg')
bgimg = pygame.transform.scale(bgimg, (screen_length,screen_height)).convert_alpha()
startimg = pygame.image.load('E:\\PSV_vs\\snakegame\\start.jpeg')
startimg = pygame.transform.scale(startimg, (screen_length,screen_height)).convert_alpha()
overimg = pygame.image.load('E:\\PSV_vs\\snakegame\\overbg.jpeg')
overimg = pygame.transform.scale(overimg, (screen_length,screen_height)).convert_alpha()

pygame.display.set_caption("Snoozy")
gwindow.fill(white)
pygame.display.update()


def plot_snk(window, color, snk_list, snk_size):
    for x,y in snk_list:
        pygame.draw.rect(window, color, [x,y,snk_size,snk_size])


def screen_text(text, color, x, y):
    text_s = font.render(text, True, color)
    gwindow.blit(text_s, [x,y])


fps = 60
font = pygame.font.SysFont(ROMAN, 30)
clock = pygame.time.Clock()

def welcomescreen():
    game_exit = False
    
    while not game_exit:
        gwindow.fill((160,230,190))
        gwindow.blit(startimg,(0,0))
        screen_text("Welcome to Snoozy", black, 260, 50)
        screen_text("Press Spacebar to Play...", black, 240, 90)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mixer.music.load('E:\\PSV_vs\\snakegame\\gmusic.mp3',)
                    mixer.music.play(loops=-1)
                    mygame()
            if event.type == pygame.QUIT:
                game_exit = True
        pygame.display.update()
        clock.tick(fps)

# Gameloop
def mygame():
    score = 0
    game_exit = False
    game_over = False
    snake_x = 25
    snake_y = 50
    vel_x = 0
    vel_y = 0
    with open("E:\\PSV_vs\\snakegame\\highscore.txt", "r") as f:
        hscore = f.read()

    snk_list = []
    snk_length = 1

    food_x = random.randint(100,screen_length-100)
    food_y = random.randint(100,screen_height-100)
    snake_size = 15

    while not game_exit:
        if game_over:
            
            with open("E:\\PSV_vs\\snakegame\\highscore.txt", "w") as f:
                f.write(str(hscore))

            gwindow.fill(white)
            gwindow.blit(overimg,(0,0))
            screen_text("Game Over!  Press Enter to Restart", red,200,150)
            screen_text("Your Score is " + str(score), black, 300,200)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        mixer.music.load('E:\\PSV_vs\\snakegame\\gmusic.mp3',)
                        mixer.music.play(loops=-1)
                        mygame()
                if event.type == pygame.QUIT:
                    game_exit = True
        else:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                                
                if event.type == pygame.KEYDOWN:       # key pressed?
                    if event.key == pygame.K_RIGHT:     # Down key pressed?
                        vel_x = 2
                        vel_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        vel_x = -2
                        vel_y = 0
                    
                    if event.key == pygame.K_UP:
                        vel_y = -2
                        vel_x = 0
                    
                    if event.key == pygame.K_DOWN:
                        vel_y = 2
                        vel_x = 0
                    
                    if event.key == pygame.K_q:
                        score +=10
                        snk_length += 5

            snake_x += vel_x
            snake_y += vel_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score += 10
                if score>int(hscore):
                    hscore = score
                #print("Score:", score)
                food_x = random.randint(100,screen_length-100)
                food_y = random.randint(100,screen_height-100)
                snk_length += 5
                #snake_length += 10
            

            gwindow.fill(white)
            gwindow.blit(bgimg,(0,0))
            pygame.draw.rect(gwindow, red, [food_x,food_y,snake_size,snake_size])

            screen_text("Score: "+str(score)+"  "+"HighScore: "+str(hscore), (51,255,51), 5, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x>screen_length or snake_x<0 or snake_y>screen_height or snake_y<0:
                game_over = True
                pygame.mixer.music.load('E:\\PSV_vs\\snakegame\\govermusic.wav')
                pygame.mixer.music.play()
            
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('E:\\PSV_vs\\snakegame\\govermusic.wav')
                pygame.mixer.music.play()
            

            plot_snk(gwindow,(224,224,224),snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcomescreen()