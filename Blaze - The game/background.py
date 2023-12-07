import pygame
from pygame.locals import *
import sys

def choose_background():
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Choose Background")

    background = pygame.transform.scale(pygame.image.load("images/customization_new.png"), size)

    clock = pygame.time.Clock()

    carry_on = True

    # Define the button dimensions and positioning
    button_width, button_height = 250, 150
    button_padding = 40  # Adjust the horizontal spacing between buttons
    button_top_margin = 100  # Adjust the vertical position of the buttons

    # Define the border color
    border_color = (238, 99, 99, 255)

    normal_background_image = pygame.transform.scale(pygame.image.load("images/normal_background.png"), (button_width, button_height))
    snowy_background_image = pygame.transform.scale(pygame.image.load("images/snow_background.png"), (button_width, button_height))

    while carry_on:
        for event in pygame.event.get():
            if event.type == QUIT:
                carry_on = False
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if normal_background_image.get_rect(center=(SCREEN_WIDTH // 2 - button_padding - button_width // 2, 300 + button_top_margin)).colliderect((x, y, 1, 1)):
                    return "normal_background"
                elif snowy_background_image.get_rect(center=(SCREEN_WIDTH // 2 + button_padding + button_width // 2, 300 + button_top_margin)).colliderect((x, y, 1, 1)):
                    return "snowy_background"

        screen.blit(background, (0, 0))

        # Calculate the positions of buttons
        normal_button_rect = normal_background_image.get_rect(center=(SCREEN_WIDTH // 2 - button_padding - button_width // 2, 300 + button_top_margin))
        snowy_button_rect = snowy_background_image.get_rect(center=(SCREEN_WIDTH // 2 + button_padding + button_width // 2, 300 + button_top_margin))

        # Draw buttons
        screen.blit(normal_background_image, normal_button_rect)
        screen.blit(snowy_background_image, snowy_button_rect)

        # Check for mouse hover and draw border accordingly
        if normal_button_rect.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))):
            pygame.draw.rect(screen, border_color, normal_button_rect, 3)

        if snowy_button_rect.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))):
            pygame.draw.rect(screen, border_color, snowy_button_rect, 3)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


