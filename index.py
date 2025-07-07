
import pygame
import time
import random

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")


white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


block_size = 20
speed = 5
clock = pygame.time.Clock()


font_style = pygame.font.SysFont(None, 40)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake = []
    length = 1

    # khana banao
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(black)
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > length:
            del snake[0]

      
        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

  
        for block in snake:
            pygame.draw.rect(screen, white, [block[0], block[1], block_size, block_size])

        pygame.display.update()

        # khana kaho baby snake
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()
