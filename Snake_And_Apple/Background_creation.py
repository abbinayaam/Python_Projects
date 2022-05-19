import pygame as pygame
#import time
from pygame.locals import *

def draw_block():
    surface.fill((3, 24, 61))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((500, 500))
    surface.fill((3, 24, 61))

    block_x = 100
    block_y = 100
    block = pygame.image.load("resources/block.jpg").convert()
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    #   time.sleep(5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running= False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False