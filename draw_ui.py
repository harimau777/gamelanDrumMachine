import pygame
from config import WIDTH, HEIGHT, GRAY

def draw_ui(screen):
    PLAY_CONTROLS_HEIGHT = 100
    RHYTHM_DISPLAY_HEIGHT = 200
    INSTRUMENT_CONTROLS_HEIGHT = HEIGHT - PLAY_CONTROLS_HEIGHT - RHYTHM_DISPLAY_HEIGHT

    BORDER_WIDTH = 5

    play_controls = pygame.draw.rect(
        screen, GRAY, [0, HEIGHT - PLAY_CONTROLS_HEIGHT, WIDTH, PLAY_CONTROLS_HEIGHT], BORDER_WIDTH
    )
    rhythm_display = pygame.draw.rect(
        screen, GRAY, [0, 0, WIDTH, RHYTHM_DISPLAY_HEIGHT], BORDER_WIDTH
    )
    instrument_controls = pygame.draw.rect(
        screen, GRAY, [0, RHYTHM_DISPLAY_HEIGHT, WIDTH, INSTRUMENT_CONTROLS_HEIGHT], BORDER_WIDTH
    )
