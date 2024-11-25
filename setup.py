import pygame
from config import WIDTH, HEIGHT

def setup():
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Gamelan Drum Machine')

    clock = pygame.time.Clock()

    return screen, clock
