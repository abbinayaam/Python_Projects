

import pygame as pygame
from pygame.locals import *
import time
import random

SIZE = 40
XMODE = 1000
YMODE = 800



class Apple:

    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 25) * SIZE
        self.y = random.randint(1, 20) * SIZE


class Snake:

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.length = 1
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * self.length
        self.y = [SIZE] * self.length
        self.direction = "down"

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):

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
        pygame.mixer.init()
        self.background_music()
        pygame.display.set_caption("SNAKE AND APPLE GAME")
        self.surface = pygame.display.set_mode((XMODE, YMODE))

        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):

        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    def render_bg(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def play_sound(self,sound):
        sound = pygame.mixer.Sound(f"resources/{sound}")
        pygame.mixer.Sound.play(sound)

    def play(self):
        self.render_bg()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

    #collision occurs when the snake hits Apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("1_snake_game_resources_ding.mp3")
            self.snake.increase_length()
            self.apple.move()

    #collision occurs when the snake hit itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("1_snake_game_resources_crash.mp3")
                raise "Game Over"

    #collision occurs when hits out of window size
        if not(0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound("1_snake_game_resources_crash.mp3")
            raise "Hit the boundaries"


    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score:{self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def show_game_over(self):
        self.render_bg()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game over.Your Score {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render(f"Press Enter to Restart. To Exit Press ESC", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()

        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)


    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False
                    pygame.mixer.music.unpause()

                    if not pause:

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

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
