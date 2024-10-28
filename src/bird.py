import pygame

# Load bird image
bird_img = pygame.image.load("images/bird_image.png")  # Load your bird image file here
bird_img = pygame.transform.scale(bird_img, (55, 55))  # Adjust size as needed

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300  # Adjust if needed
        self.vel = 0
        self.rect = bird_img.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.vel += 1  # Use a constant gravity value
        self.y += self.vel
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.vel = -14  # Jump height

    def draw(self, win):
        win.blit(bird_img, (self.x, self.y))
