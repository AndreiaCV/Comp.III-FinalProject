import pygame
import sys
from game import *
from customization import customize_cars
from background import *


YELLOW = (255, 255, 0)


def load_and_scale(image_path, rect):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, (rect.width, rect.height))

def create_button(image_path, pressed_image_path, rect, action):
    normal_image = load_and_scale(image_path, rect)
    pressed_image = load_and_scale(pressed_image_path, rect)
    return normal_image, pressed_image, rect, action

# Creating a function that creates the GUI
def interface():
    # initiating pygames
    pygame.init()

    res = (720, 720)
    screen = pygame.display.set_mode(res)

    # Load background music
    pygame.mixer.music.load('music/menu_msc.mp3')

    # Start playing background music
    pygame.mixer.music.play(-1)  # The -1 argument makes the music loop indefinitely

    buttons = [
        create_button('images/start.png', 'images/start_pressed.png', pygame.Rect(400, 300, 200, 60), lambda: start_game(1)),
        create_button('images/Multiplayer.png', 'images/multiplayer_pressed.png', pygame.Rect(130, 300, 250, 60), lambda: start_game(2)),
        create_button('images/Instructions.png', 'images/instructions_pressed.png', pygame.Rect(130, 385, 250, 60), instructions_),
        create_button('images/Credits.png', 'images/credits_pressed.png', pygame.Rect(130, 470, 200, 60), credits_),
        create_button('images/close.png', 'images/close.png', pygame.Rect(670, 20, 30, 30), sys.exit)
    ]
    
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button[2].collidepoint(mouse):
                        button[3]()

        screen.blit(pygame.image.load("images/ecra.png"), (0, 0))
        for button in buttons:
            image = button[1] if button[2].collidepoint(mouse) else button[0]
            screen.blit(image, button[2].topleft)

        pygame.display.update()

def start_game(players):
    background = choose_background()
    selected_cars = customize_cars(players)
    if selected_cars and background:
        car_racing(players, background, selected_cars)

def credits_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    font = pygame.font.SysFont('Consolas', 25)
    text_lines = [
        font.render('Andreia Vieira, 20221944@novaims.unl.pt', True, YELLOW),
        font.render('Isabel Liu, 20221913@novaims.unl.pt', True, YELLOW),
        font.render('Madalena Abreu, 20221884d@novaims.unl.pt', True, YELLOW)
    ]
    buttons = [create_button('images/back.png', 'images/back_pressed.png', pygame.Rect(450, 600, 200, 60), interface)]

    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button[2].collidepoint(mouse):
                        button[3]()

        screen.blit(pygame.image.load("images/credits_screen.png"), (0, 0))
        for i, text in enumerate(text_lines):
            screen.blit(text, (50, 300 + i * 25))
        for button in buttons:
            image = button[1] if button[2].collidepoint(mouse) else button[0]
            screen.blit(image, button[2].topleft)

        pygame.display.update()

def instructions_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    backgrounds = ['images/instruçoes0.png', 'images/instruçoes1.png', 'images/instruçoes2.png', 'images/instruçoes3.png']
    current_background_index = 0
    buttons = [create_button('images/back.png', 'images/back_pressed.png', pygame.Rect(450, 600, 200, 60), interface)]


    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button[2].collidepoint(mouse):
                        button[3]()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    current_background_index = (current_background_index - 1) % len(backgrounds)
                elif ev.key == pygame.K_RIGHT:
                    current_background_index = (current_background_index + 1) % len(backgrounds)

        # Load and display the current background image
        background_image = pygame.image.load(backgrounds[current_background_index])
        original_width, original_height = background_image.get_size()
        
        # Scale the image to almost the size of the display window
        scale_factor = min(res[0] / original_width, res[1] / original_height)
        scaled_width, scaled_height = int(original_width * scale_factor), int(original_height * scale_factor)
        scaled_image = pygame.transform.scale(background_image, (scaled_width, scaled_height))
        
        # Calculate the position to center the image on the screen
        x_offset = (res[0] - scaled_width) // 2
        y_offset = (res[1] - scaled_height) // 2

        screen.blit(scaled_image, (x_offset, y_offset))
        for button in buttons:
            image = button[1] if button[2].collidepoint(mouse) else button[0]
            screen.blit(image, button[2].topleft)

        pygame.display.update()
