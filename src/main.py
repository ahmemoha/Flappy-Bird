import pygame
import random
from bird import Bird
from pipe import Pipe
from utils import game_over, wait_for_exit

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Define colors
BLUE = (173, 216, 230)

# Define constants
FPS = 30

# Main game loop
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    font = pygame.font.SysFont(None, 36)

    run = True
    while run:
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Update bird
        bird.update()

        # Update pipes
        if pipes[-1].x < WIDTH // 2:
            pipes.append(Pipe())

        for pipe in pipes[:]:
            pipe.update()
            if pipe.x + pipe.width < 0:
                pipes.remove(pipe)
                score += 1

        # Check collisions
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top) or bird.rect.colliderect(pipe.bottom):
                game_over(win, score)
                run = False

        if bird.y > HEIGHT or bird.y < 0:
            game_over(win, score)
            run = False

        # Draw everything
        win.fill(BLUE)
        bird.draw(win)
        for pipe in pipes:
            pipe.draw(win)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        win.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
