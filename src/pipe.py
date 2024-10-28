import pygame
import random

# Define constants
PIPE_WIDTH = 70
PIPE_GAP = 155

class Pipe:
    def __init__(self):
        self.x = 600  # Starting position
        self.height = random.randint(50, 600 - PIPE_GAP - 50)
        self.top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, 600 - self.height - PIPE_GAP)

    def update(self):
        self.x -= 5
        self.top.topleft = (self.x, 0)
        self.bottom.topleft = (self.x, self.height + PIPE_GAP)

    def draw(self, win):
        pygame.draw.rect(win, (0, 128, 0), self.top)
        pygame.draw.rect(win, (0, 128, 0), self.bottom)
