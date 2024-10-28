import pygame

def game_over(win, score):
    font_big = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)

    game_over_text = font_big.render("Game Over", True, (0, 0, 0))
    score_text = font_big.render(f"Score: {score}", True, (0, 0, 0))
    restart_text = font_small.render("Press Enter or Space to restart, D to exit", True, (0, 0, 0))

    win.fill((173, 216, 230))
    win.blit(game_over_text, (300 - game_over_text.get_width() // 2, 200))
    win.blit(score_text, (300 - score_text.get_width() // 2, 300))
    win.blit(restart_text, (300 - restart_text.get_width() // 2, 400))
    pygame.display.update()
    wait_for_exit()

def wait_for_exit():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RETURN, pygame.K_SPACE]:  # Restart on Enter or Space
                    main()
                    waiting = False
                elif event.key == pygame.K_d:  # Exit on D
                    pygame.quit()
                    exit()
