import pygame
import random

#Power up parent class
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image, effect_duration, speed, powerup_type):
        """
        Initialize the PowerUp object.

        Parameters:
        - image (str): Filename of the power-up image.
        - effect_duration (int): Duration of the power-up effect in seconds.
        - speed (float): Movement speed of the power-up.
        - powerup_type (str): Type of the power-up (e.g., 'slow', 'invincibility', 'shoot', 'invert').
        """
        super().__init__()
        #load and sclae powerup images
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        #duration of the powerups
        self.effect_duration = effect_duration
        self.speed = speed
        self.screen_width = 800
        self.rect.x = random.choice([200, 300, 400, 500])  # Set initial x position
        self.powerup_type = powerup_type
        self.active = False
        self.activation_time = 0
        self.duration = effect_duration
        self.remaining_duration = effect_duration
        self.original_y = self.rect.y = self.get_initial_y()
        
    def get_initial_y(self):
        """Get the initial y-coordinate based on the type of power-up."""
        if self.powerup_type == 'slow':
            return -3000
        elif self.powerup_type == 'invincibility':
            return -7000
        elif self.powerup_type == 'shoot':
            return -5000
        elif self.powerup_type == 'invert':
            return -4000
    def get_points(self):
        """Get the points added/taken for each power-up the user gets."""

        if self.powerup_type == 'slow':
            return 1000
        elif self.powerup_type == 'invincibility':
            return 2000
        elif self.powerup_type == 'shoot':
            return 3000
        elif self.powerup_type == 'invert':
            return -1000
    #activate powerup
    def activate(self, player):
        """
        Activate the power-up.

        Parameters:
        - player: The player affected by the power-up.
        """
        self.active = True
        self.player = player
        self.activation_time = pygame.time.get_ticks()
        self.duration = self.effect_duration
    def move(self):
        """Move the power-up along the screen and handle activation duration."""

        # Define the movement behavior for power-ups here
        self.rect.y += self.speed / 20  # Adjust the movement speed based on car speed
        if self.active:
            self.remaining_duration -=1
        # Respawn if the power-up goes off the screen
        if self.rect.y > self.screen_width:
            self.reset_position()
    def reset_position(self):
        """Reset the power-up position to a random location."""

        self.rect.x = random.choice([200, 300, 400, 500]) # x coordinates for powerup reset
        self.rect.y = self.original_y
    
    def affect_player(self, player):
        """How it affects the player"""
        pass  # To be implemented in child classes

    def affect_traffic(self, traffic):
        """How it affects the traffic"""
        pass  # To be implemented in child classes
