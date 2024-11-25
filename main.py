import pygame
from draw_ui import draw_ui
from config import WIDTH, HEIGHT, FPS, BLACK, WHITE, GRAY, LABEL_FONT
from setup import setup

screen, clock = setup()

run = True

while run:
    clock.tick(FPS)
    screen.fill(BLACK)
    draw_ui(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()