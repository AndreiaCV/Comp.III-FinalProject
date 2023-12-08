#import necessary libraries
import pygame
from car import Car
from game import *
import sys

def customize_cars(num_players):
    """
    Customize players car before starting the game.

    Parameters:
    - num_players (int): The number of players in the game.

    Returns:
    - list: A list of paths to the selected car images for each player.
    """
    #Intializing pygame
    pygame.init()

    #Set screen dimensions
    SCREENWIDTH, SCREENHEIGHT= 800, 600

    #Define screen size
    size = (SCREENWIDTH, SCREENHEIGHT)
    #Create the window
    screen = pygame.display.set_mode(size)
    #Set window title
    pygame.display.set_caption("Car Customization")

    # Create a sprite group to manage all sprites
    all_sprites_list = pygame.sprite.Group()

    # Load and scale the background image
    background = pygame.transform.scale(pygame.image.load("images/customization_new.png"), size)

    # Set the font for displaying text
    font = pygame.font.SysFont('Consolas', 25)

    # Initialize lists to store player objects and car images
    players = []
    car_images = ["images/carro_top1.png", "images/carro_top2.png", "images/carro_top3.png"]
    current_car_index = [0] * num_players  # Track the currently selected car for each player
    selected_cars = [car_images[0]] * num_players  # List to store selected cars with default values

    # Create player objects based on the number of players
    for i in range(num_players):
        # Create a Car object with the default car image and size
        player = Car(car_images[0], 70)

        # Set the initial position of the player on the screen
        player.rect.x = SCREENWIDTH // 4 + i * SCREENWIDTH // 4 + 100
        player.rect.y = SCREENHEIGHT // 1.5

        # Add the player to the sprite group
        players.append(player)
        all_sprites_list.add(player)

    # Load and scale the Start and Start Pressed buttons
    start_button = pygame.transform.scale(pygame.image.load("images/start.png"), (150, 50))
    start_pressed_button = pygame.transform.scale(pygame.image.load("images/start_pressed.png"), (150, 50))

    # Get the rectangle for the Start button and center it at the bottom of the screen
    start_button_rect = start_button.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT - 26))

    # Initialize variables for the game loop
    carry_on = True
    clock = pygame.time.Clock()

    while carry_on:
        #Get mouse position
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Check if the user has clicked the close button (X) on the window
            if event.type == pygame.QUIT:
                carry_on = False # Set the flag to exit the game loop
                sys.exit() #exit system
            
            #Check for key presses
            elif event.type == pygame.KEYDOWN:
                # Iterate over the number of players
                for i in range(num_players):
                    # Player 1 controls (arrow keys)
                    if i == 0 and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        # Update the selected car index based on arrow key pressed
                        current_car_index[i] = (current_car_index[i] - 1 + 2 * (event.key == pygame.K_RIGHT)) % len(car_images)
                    
                    # Player 2 controls (a and d keys)
                    elif i == 1 and event.key in [pygame.K_a, pygame.K_d]:
                        # Update the selected car index based on a or d key pressed
                        current_car_index[i] = (current_car_index[i] - 1 + 2 * (event.key == pygame.K_d)) % len(car_images)

                # Update the list of selected cars
                selected_cars = [car_images[index] for index in current_car_index]

            elif event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
                carry_on = False  # Exit the loop when the Confirm button is clicked
        
        #Update all sprites
        all_sprites_list.update()

        #Draw the background
        screen.blit(background, (0, 0))

        # Draw player cars and text
        for i, player in enumerate(players):
            # Load and scale the image of the selected car for the current player
            car_image = pygame.transform.scale(pygame.image.load(car_images[current_car_index[i]]), (player.rect.width, player.rect.height))
            
            # Blit the car image onto the screen, centered around the player's position
            screen.blit(car_image, (player.rect.centerx - player.rect.width // 2, player.rect.centery - player.rect.height // 2))

            # Render text indicating the player number above the player's car
            player_text = font.render(f'Player {i + 1}', True, (238, 99, 99, 255))

            # Blit the player text above the player's car, centered horizontally
            screen.blit(player_text, (player.rect.centerx - player_text.get_width() // 2, player.rect.y - player.rect.height - 10))

        # Draw Start button
        screen.blit(start_pressed_button if start_button_rect.collidepoint(mouse) else start_button, start_button_rect.topleft)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 frames per second
        clock.tick(60)

    #Quit pygame
    pygame.quit()

    # Return the list of selected cars
    return selected_cars
