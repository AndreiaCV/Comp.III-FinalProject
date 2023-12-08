import pygame
from pygame.locals import *
import sys


def choose_background():
    """
    Opens a window for the user to choose a background image for customization.

    Returns:
    - str: Selected background option ("normal_background" or "snowy_background").
    """
    # Initialize pygame
    pygame.init()
    #define screen size (800x600)
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    # Create the game window
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Choose Background")
    # Load and scale the background image for customization
    background = pygame.transform.scale(pygame.image.load("images/customization_new.png"), size)
    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()
    # Flag to control the main loop
    carry_on = True

    # Define the button dimensions and positioning
    button_width, button_height = 250, 150
    button_padding = 40  # Adjust the horizontal spacing between buttons
    button_top_margin = 100  # Adjust the vertical position of the buttons

    # Define the border color
    border_color = (238, 99, 99, 255)
    #load background images
    normal_background_image = pygame.transform.scale(pygame.image.load("images/normal_background.png"), (button_width, button_height))
    snowy_background_image = pygame.transform.scale(pygame.image.load("images/snow_background.png"), (button_width, button_height))
    #user input
    while carry_on:
        for event in pygame.event.get():
            # Check for quit event
            if event.type == QUIT:
                carry_on = False
                sys.exit()
            # Check for mouse click event
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check if the mouse click is on the normal background button
                if normal_background_image.get_rect(center=(SCREEN_WIDTH // 2 - button_padding - button_width // 2, 300 + button_top_margin)).colliderect((x, y, 1, 1)):
                    return "normal_background"
                # Check if the mouse click is on the snowy background button
                elif snowy_background_image.get_rect(center=(SCREEN_WIDTH // 2 + button_padding + button_width // 2, 300 + button_top_margin)).colliderect((x, y, 1, 1)):
                    return "snowy_background"
                    
        # Display the background image
        screen.blit(background, (0, 0))

        # Calculate the positions of buttons
        normal_button_rect = normal_background_image.get_rect(center=(SCREEN_WIDTH // 2 - button_padding - button_width // 2, 300 + button_top_margin))
        snowy_button_rect = snowy_background_image.get_rect(center=(SCREEN_WIDTH // 2 + button_padding + button_width // 2, 300 + button_top_margin))

        # Draw buttons
        screen.blit(normal_background_image, normal_button_rect)
        screen.blit(snowy_background_image, snowy_button_rect)

        # Check for mouse hover and draw border accordingly on normal background
        if normal_button_rect.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))):
            pygame.draw.rect(screen, border_color, normal_button_rect, 3)
        # Check for mouse hover and draw border accordingly on snowy background
        if snowy_button_rect.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))):
            pygame.draw.rect(screen, border_color, snowy_button_rect, 3)
        # Update the display
        pygame.display.flip()
        # Control the frame rate,60 frames per second
        clock.tick(60)
    # Quit pygame when the main loop exits
    pygame.quit()

