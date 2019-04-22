import pygame
import sys

#some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#grid dimensions
WIDTH = 5
HEIGHT = 5
#space between each cell
MARGIN = 1

#create 2d array to store grid values
grid = []
for row in range(120):
    grid.append([])
    for column in range(213):
        grid[row].append(0)

pygame.init() #initialize
pygame.display.set_caption("Conway's Game of Life!")
screen = pygame.display.set_mode((1280,720)) #set window resolution
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)

clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #get mouse position
            pos = pygame.mouse.get_pos()
            #change coordinates to grid coordinates
            column = pos[0]//(WIDTH + MARGIN)
            row = pos[1]//(HEIGHT + MARGIN)
            #set position to 1
            if grid[row][column] == 0:
                grid[row][column] = 1
            else:
                grid[row][column] = 0

    screen.blit(background, (0,0))

    for row in range(120):
        for column in range(213):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                             (MARGIN + HEIGHT) * row + MARGIN,
                                             WIDTH,
                                             HEIGHT])

    pygame.display.flip()