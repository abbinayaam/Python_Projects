

import pygame as pygame
from pygame.locals import *
import time

SIZE = 40

class Apple:

    def __init__(self,parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake:

    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "up"

    def draw(self):
        self.parent_screen.fill((3, 24, 61))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def mov_left(self):
        self.direction = "left"

    def mov_right(self):
        self.direction = "right"

    def mov_up(self):
        self.direction = "up"

    def mov_down(self):
        self.direction = "down"

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "right":
            self.x[0] += SIZE
            self.draw()
        if self.direction == "left":
            self.x[0] -= SIZE
            self.draw()
        if self.direction == "up":
            self.y[0] -= SIZE
            self.draw()
        if self.direction == "down":
            self.y[0] += SIZE
            self.draw()


class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((3, 24, 61))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

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

            self.play()
            time.sleep(0.9)


if __name__ == "__main__":
    game = Game()
    game.run()
