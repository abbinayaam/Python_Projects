import pygame as pygame
from pygame.locals import *


class Snake:

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((3, 24, 61))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def mov_left(self):
        self.x -= 10
        self.draw()

    def mov_right(self):
        self.x += 10
        self.draw()

    def mov_up(self):
        self.y -= 10
        self.draw()

    def mov_down(self):
        self.y += 10
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((3, 24, 61))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.mov_up()
                    if event.key == K_DOWN:
                        self.snake.mov_down()
                    if event.key == K_LEFT:
                        self.snake.mov_left()
                    if event.key == K_RIGHT:
                        self.snake.mov_right()
                elif event.type == QUIT:
                    running = False

if __name__ == "__main__":
    game = Game()
    game.run()
