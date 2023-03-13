import pygame
import random

# Initialize pygame and create window
pygame.init()
win = pygame.display.set_mode((500, 500))

# Load and set up the ball and paddle images
#ball_img = pygame.image.load("ball.png")
#paddle_img = pygame.image.load("paddle.png")

# Create the ball and paddle objects
ball = pygame.Rect(235, 435, 30, 30)
paddle = pygame.Rect(220, 450, 60, 10)

# Set up the bricks
bricks = []
for i in range(7):
    for j in range(5):
        bricks.append(pygame.Rect(i*70+20, j*30+20, 60, 20))

# Set up ball speed and direction
ball_speed = [2, -2]

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Check if the ball hits a wall
    if ball.left <= 0 or ball.right >= 500:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Check if the ball hits the paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]
        ball.top = paddle.top - ball.height

    # Check if the ball hits a brick
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
            break

    # Move the paddle based on mouse position
    pos = pygame.mouse.get_pos()
    paddle.left = pos[0] - paddle.width // 2

    # Redraw the window
    win.fill((255, 255, 255))
    #win.blit(ball_img, ball)
    #win.blit(paddle_img, paddle)
    for brick in bricks:
        pygame.draw.rect(win, (255, 0, 0), brick)
    pygame.display.update()

# Quit pygame
pygame.quit()
