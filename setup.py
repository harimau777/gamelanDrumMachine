import pygame
from config import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Gamelan Drum Machine')

clock = pygame.time.Clock()