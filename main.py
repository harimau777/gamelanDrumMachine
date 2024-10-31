import pygame
from config import WIDTH, HEIGHT, FPS, BLACK, WHITE, GRAY, LABEL_FONT

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Gamelan Drum Machine')

clock = pygame.time.Clock()

run = True

while run:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()