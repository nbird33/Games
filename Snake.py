# create a snake and setup the snake list
# import modules
import pygame
from pygame.locals import *

pygame.init()

# create blank game window
screen_width = 600
screen_height = 600

# create game window 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

#define game variables
cell_size = 10


# create snake
snake_position = [[int(screen_width / 2), int(screen_height / 2)]]
snake_position.append([int(screen_width / 2), int(screen_height / 2) + cell_size])
snake_position.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 2])
snake_position.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 3])

# define colors
bg = (255, 200, 150)
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)
red = (255, 0, 0)

def draw_screen():
    screen.fill(bg)

# setup loop exit event handler
run = True
while run:

    draw_screen()

    # iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw snake
    head = 1
    for x in snake_position:
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, red, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
            head = 0

            
    # update the display
    pygame.display.update()

# end pygame
pygame.quit()
