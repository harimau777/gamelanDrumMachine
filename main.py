import pygame

pygame.init()

WIDTH = 1400
HEIGHT = 700

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

LABEL_FONT = pygame.font.Font('freesansbold.ttf', 32)

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