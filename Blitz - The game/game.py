import pygame
import random
from car import Car
from slowing import SlowingPowerUp
from invincibility import *
from powerUp import PowerUp
from shoot import *
from invert import *
import interface
import math
import sys

BLACK = (0,0,0)
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREENWIDTH = 800
SCREENHEIGHT = 600

a_small, b_small= 100, 50

a_big, b_big = 150, 88

def game_over(screen, font, yes_button_image, no_button_image):
    screen.fill(BLACK)

    game_over_font = pygame.font.Font('images/game_over.ttf', 280)
    game_over_text = game_over_font.render("Game Over", True, RED)

    text_rect = game_over_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 5))
    screen.blit(game_over_text, text_rect)

    continue_prompt_text = font.render("Would you like to continue?", True, WHITE)
    screen.blit(continue_prompt_text, (SCREENWIDTH // 2 - 200, SCREENHEIGHT // 2 + 30))

    yes_button_rect = yes_button_image.get_rect(center=(SCREENWIDTH // 2 - 70, SCREENHEIGHT // 2 + 100))
    no_button_rect = no_button_image.get_rect(center=(SCREENWIDTH // 2 + 70, SCREENHEIGHT // 2 + 100))

    screen.blit(yes_button_image, yes_button_rect)
    screen.blit(no_button_image, no_button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if yes_button_rect.collidepoint(event.pos):
                    return "restart"
                elif no_button_rect.collidepoint(event.pos):
                    return "menu"

        # Get the current mouse position
        mouse = pygame.mouse.get_pos()

        yes_button_image = pygame.image.load('images/yes_pressed.png') if yes_button_rect.collidepoint(mouse) else pygame.image.load('images/yes.png')
        no_button_image = pygame.image.load('images/no_pressed.png') if no_button_rect.collidepoint(mouse) else pygame.image.load('images/no.png')

        yes_button_image = pygame.transform.scale(yes_button_image, (100, 40))
        no_button_image = pygame.transform.scale(no_button_image, (100, 40))

        screen.blit(yes_button_image, yes_button_rect)
        screen.blit(no_button_image, no_button_rect)

        pygame.display.flip()


def pause(screen, font, restart_button_image, menu_button_image):
    paused_text = font.render("Paused", True, WHITE)
    
    overlay = pygame.Surface((SCREENWIDTH, SCREENHEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))  # Adjust the fourth parameter for transparency

    screen.blit(overlay, (0, 0))  # Draw the transparent overlay
    screen.blit(paused_text, (SCREENWIDTH // 2 - 47, SCREENHEIGHT // 2 - 30))
    
    restart_button_rect = restart_button_image.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 50))
    menu_button_rect = menu_button_image.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 100))

    screen.blit(restart_button_image, restart_button_rect)
    screen.blit(menu_button_image, menu_button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_button_rect.collidepoint(event.pos):
                    return "restart"
                elif menu_button_rect.collidepoint(event.pos):
                    return "menu"
                else:
                    return "unpause"

        # Get the current mouse position
        mouse = pygame.mouse.get_pos()

        restart_button_image = pygame.image.load('images/restart_pressed.png') if restart_button_rect.collidepoint(mouse) else pygame.image.load('images/restart.png')
        menu_button_image = pygame.image.load('images/menu_pressed.png') if menu_button_rect.collidepoint(mouse) else pygame.image.load('images/menu.png')

        restart_button_image = pygame.transform.scale(restart_button_image, (100, 40))
        menu_button_image = pygame.transform.scale(menu_button_image, (100, 40))

        screen.blit(restart_button_image, restart_button_rect)
        screen.blit(menu_button_image, menu_button_rect)

        pygame.display.flip()

def car_racing(num_players, background, selected_cars):
    pygame.init()

    # Load background music
    pygame.mixer.music.load('music/race_msc.mp3')

    # Start playing background music
    pygame.mixer.music.play(-1)  # The -1 argument makes the music loop indefinitely

    car_images = ["images/carro1.png", "images/carro2.png", "images/carro3.png", "images/carro4.png"]

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    all_sprites_list = pygame.sprite.Group()
    all_coming_cars = pygame.sprite.Group()
    all_player_cars = pygame.sprite.Group()
    all_power_ups = pygame.sprite.Group()

    # Create player cars based on the selected cars
    player_cars = [Car(selected_cars[i], 70) for i in range(num_players)]
    
    for i, playerCar in enumerate(player_cars):
        playerCar.rect.x = 160 + i * 100  # Adjust the initial x position for multiple players
        playerCar.rect.y = SCREENHEIGHT - 100
        playerCar.player_number = i + 1  # Assign a unique player number
        all_sprites_list.add(playerCar)
        all_player_cars.add(playerCar)

    for i in range(1, 5):
        car = Car(random.choice(car_images), random.uniform(50, 100))
        car.initial_x = (i-1) * 100 + 60
        car.rect.y = i* (-200)
        all_sprites_list.add(car)
        all_coming_cars.add(car)

    # Create a list of power-ups
    power_ups = [
        SlowingPowerUp(speed=random.uniform(50, 100)),
        InvincibilityPowerUp(speed=random.uniform(50, 100)),
        ShootPowerUp(speed=random.uniform(50, 100)),
        InvertPowerUp(speed=random.uniform(50, 100)),
    ]

    snowFall = [[random.randrange(0, 800), random.randrange(0, 600)] for _ in range(200)]

    all_power_ups.add(power_ups)

    pause_button_image = pygame.image.load('images/pause.png')
    #scale image
    pause_button_image = pygame.transform.scale(pause_button_image, (60, 20))
    #image position
    pause_button_rect = pause_button_image.get_rect(topright=(SCREENWIDTH-10, 10))

    carry_on = True
    clock = pygame.time.Clock()
    paused = False

    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pause_button_rect.collidepoint(event.pos):
                    paused = not paused
        if paused:
            restart_button_image = pygame.image.load('images/restart.png')
            restart_button_image = pygame.transform.scale(restart_button_image, (100, 40))
            menu_button_image = pygame.image.load('images/menu.png')
            menu_button_image = pygame.transform.scale(menu_button_image, (100, 40))
            font = pygame.font.SysFont('Consolas', 28)

            # Call pause function with necessary arguments
            pause_result = pause(screen, font, restart_button_image, menu_button_image)

            if pause_result == "restart":
                car_racing(num_players, background, selected_cars)
            elif pause_result == "menu":
                interface.interface()
            elif pause_result == "unpause":
                paused = False
            
        else:

            keys = pygame.key.get_pressed()
            for playerCar in player_cars:
                if playerCar.player_number == 1:  # Player 1 controls
                    if keys[pygame.K_LEFT]:
                            playerCar.moveLeft(5)
                    if keys[pygame.K_RIGHT]:
                            playerCar.moveRight(5)
                            print(f"Player Car {i+1} Rect: {playerCar.rect}")
                    if keys[pygame.K_UP]:
                        playerCar.moveBackward()
                    if keys[pygame.K_DOWN]:
                        playerCar.moveForward()
                    if keys[pygame.K_SPACE] and playerCar.shooting_enabled:
                        for power_up in power_ups:
                            if isinstance(power_up, ShootPowerUp):
                                power_up.shoot(playerCar.rect.x + 26, playerCar.rect.y)

                elif playerCar.player_number == 2:  # Player 2 controls
                    if keys[pygame.K_a]:
                            playerCar.moveLeft(5)
                    if keys[pygame.K_d]:
                            playerCar.moveRight(5)
                    if keys[pygame.K_w]:
                        playerCar.moveBackward()
                    if keys[pygame.K_s]:
                        playerCar.moveForward()
                    if keys[pygame.K_SPACE] and playerCar.shooting_enabled:
                        for power_up in power_ups:
                            if isinstance(power_up, ShootPowerUp):
                                power_up.shoot(playerCar.rect.x + 26, playerCar.rect.y)

        for car in all_coming_cars:
            if isinstance(car, Car):    
                car.rect.x = car.initial_x
                car.moveForward()
            if car.rect.y > SCREENHEIGHT:
                car.reset_position(car_images)

        for power_up in power_ups:
                power_up.move()

        # Check collisions for all player cars
        for playerCar in player_cars:
            powerup_collision_list = pygame.sprite.spritecollide(playerCar, all_power_ups, False)
            for collided_powerup in powerup_collision_list:
                    if not collided_powerup.active:
                        collided_powerup.activate(playerCar)
                        collided_powerup.reset_position()

        # Now, outside the loop over player cars
        for power_up in all_power_ups:
            if isinstance(power_up, SlowingPowerUp) and power_up.active:
                power_up.affect_traffic(all_coming_cars)
            elif isinstance(power_up, InvincibilityPowerUp) and power_up.active:    
                power_up.affect_player()
            elif isinstance(power_up, ShootPowerUp) and power_up.active:
                power_up.affect_player()
                power_up.affect_traffic(all_coming_cars, car_images)
            elif isinstance(power_up, InvertPowerUp) and power_up.active:
                power_up.affect_player()

        # Check if there is a car collision
        for playerCar in player_cars:
                car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
                print(f"Player Car {playerCar.player_number} Collision List: {car_collision_list}")
                for collided_car in car_collision_list:
                    if playerCar != collided_car and not playerCar.invincible:
                        print(f"Player {playerCar.player_number} car crash!")
                        all_sprites_list.remove(playerCar)
                        all_player_cars.remove(playerCar)
                        player_cars.remove(playerCar)
                    elif  playerCar != collided_car and playerCar.invincible:
                        if isinstance(collided_car, Car):   
                            collided_car.reset_position(car_images)
        
        if len(player_cars) == 0:
            # Load Yes and No button images
            font = pygame.font.SysFont('Consolas', 28)

            yes_button_image = pygame.image.load('images/yes.png')
            yes_button_image = pygame.transform.scale(yes_button_image, (100, 40))

            no_button_image = pygame.image.load('images/no.png')
            no_button_image = pygame.transform.scale(no_button_image, (100, 40))

            game_over_result = game_over(screen, font, yes_button_image, no_button_image)

            if game_over_result == "restart":
                car_racing(num_players, background, selected_cars)
            elif game_over_result == "menu":
                interface.interface()

        if background == "normal_background":
            # Draw background
            screen.fill(GREEN)
            pygame.draw.rect(screen, GREY, [40, 0, 400, SCREENHEIGHT])
            pygame.draw.line(screen, WHITE, [140, 0], [140, SCREENHEIGHT], 5)
            pygame.draw.line(screen, WHITE, [240, 0], [240, SCREENHEIGHT], 5)
            pygame.draw.line(screen, WHITE, [340, 0], [340, SCREENHEIGHT], 5)

        elif background == "snowy_background":
            back_image = pygame.image.load("images/snowy_grass.png")
            back_image = pygame.transform.scale(back_image, (SCREENWIDTH, SCREENHEIGHT))
            screen.blit(back_image, (0, 0))
            pygame.draw.rect(screen, GREY, [40, 0, 400, SCREENHEIGHT])
            pygame.draw.line(screen, WHITE, [140, 0], [140, SCREENHEIGHT], 5)
            pygame.draw.line(screen, WHITE, [240, 0], [240, SCREENHEIGHT], 5)
            pygame.draw.line(screen, WHITE, [340, 0], [340, SCREENHEIGHT], 5)

            # Draw the wires
            small_wire1 = pygame.Rect(0, -55, 200, 100)  # (x, y, width, height)
            pygame.draw.ellipse(screen, BLACK, small_wire1, 2)  # (surface, color, rect, width)
            small_wire2 = pygame.Rect(500, -55, 200, 100)
            pygame.draw.ellipse(screen, BLACK, small_wire2, 2)

            big_wire = pygame.Rect(200, -90, 300, 175)
            pygame.draw.ellipse(screen, BLACK, big_wire, 2)

            # Calculate the color based on time
            color = (
                int(127 * (1 + math.sin(pygame.time.get_ticks() / 1000))),
                int(127 * (1 + math.sin(pygame.time.get_ticks() / 1000 + (2 * math.pi / 3)))),
                int(127 * (1 + math.sin(pygame.time.get_ticks() / 1000 + (4 * math.pi / 3))))
            )

            # Iterate through positions on the ellipse using a for loop
            num_balls_small_wire = 25
            num_balls_big_wire = 35
            for i in range(num_balls_small_wire):
                t = 2 * math.pi * i / num_balls_small_wire
                x1 = int(100 + a_small * math.cos(t))
                y1 = int(-4 + b_small * math.sin(t))

                pygame.draw.circle(screen, color, (x1, y1), 5)

            for i in range(num_balls_big_wire):
                t = 2 * math.pi * i / num_balls_big_wire
                x2 = int(350 + a_big * math.cos(t))
                y2 = int(-4 + b_big * math.sin(t))

                pygame.draw.circle(screen, color, (x2, y2), 5)

            for i in range(num_balls_small_wire):
                t = 2 * math.pi * i / num_balls_small_wire
                x3 = int(600 + a_small * math.cos(t))
                y3 = int(-4 + b_small * math.sin(t))

                pygame.draw.circle(screen, color, (x3, y3), 5)

            # Create new snowflakes at the top
            for i in range(len(snowFall)):
                pygame.draw.circle(screen, WHITE, snowFall[i], 3)

                # Move the snowballs
                snowFall[i][1] += 1
                if snowFall[i][1] > 600:
                    y = random.randrange(-50, -10)
                    snowFall[i][1] = y

                    x = random.randrange(0, 700)
                    snowFall[i][0] = x

        all_sprites_list.update()

        all_power_ups.draw(screen)

        # Draw bullets in the game loop
        bullet_group = pygame.sprite.Group([power_up.get_bullets() for power_up in power_ups if isinstance(power_up, ShootPowerUp)])
        bullet_group.draw(screen)
    
        all_sprites_list.draw(screen)

        # Draw the pause button image
        screen.blit(pause_button_image, pause_button_rect)

        # Draw active power-ups and their timers
        for playerCar in player_cars:
            active_power_ups = [power_up for power_up in all_power_ups if power_up.active and power_up.player == playerCar]

            # Calculate the height of the rectangle based on the number of active power-ups
            rect_height = 50 + len(active_power_ups) * 30

            pygame.draw.rect(screen, WHITE, [SCREENWIDTH - 180, 50 + playerCar.player_number * 140, 170, rect_height])  # Rectangle indicating active power-ups
            font = pygame.font.Font(None, 24)
            player_text = font.render(f"Player {playerCar.player_number}:", True, BLACK)
            screen.blit(player_text, [SCREENWIDTH - 170, 60 + playerCar.player_number * 140])

            for j, active_power_up in enumerate(active_power_ups):
                power_up_text = font.render(active_power_up.powerup_type, True, BLACK)
                timer_text = font.render(f"{active_power_up.remaining_duration} s", True, BLACK)

                screen.blit(power_up_text, [SCREENWIDTH - 170, 90 + playerCar.player_number * 140 + j * 30])
                screen.blit(timer_text, [SCREENWIDTH - 80, 90 + playerCar.player_number * 140 + j * 30])

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


