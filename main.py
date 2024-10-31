import pygame
from config import WIDTH, HEIGHT, FPS, BLACK, WHITE, GRAY, LABEL_FONT
from setup import screen, clock

run = True

while run:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()