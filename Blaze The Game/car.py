import pygame
import random

WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()

        self.original_image = pygame.image.load(image)
        self.original_image = pygame.transform.scale(self.original_image, (55, 70))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.initial_x = 0
        self.invincible = False
        self.shooting_enabled = False
        self.inverted = False
        self.player_number = 0

    def moveRight(self, pixels):
            if self.inverted and self.rect.x > 200:
                self.rect.x -= pixels
            elif not self.inverted and self.rect.x < 550:
                self.rect.x += pixels

    def moveLeft(self, pixels):
            if self.inverted and self.rect.x < 550:
                self.rect.x += pixels
            elif not self.inverted and self.rect.x > 200:
                self.rect.x -= pixels

    def moveForward(self):
        self.rect.y += self.speed / 25

    def moveBackward(self):
        self.rect.y -= self.speed / 20

    def changeSpeed(self, speed):
        self.speed = speed
    
    def changeImage(self, images):
        self.original_image = pygame.image.load(random.choice(images))
        self.original_image = pygame.transform.scale(self.original_image, (55, 70))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
    
    def slow_down(self):
        self.speed = max(1, self.speed - 1)
    
    def activate_invincibility(self):
        self.invincible = True

    def deactivate_invincibility(self):
        self.invincible = False

    def reset_position(self, images):
        self.changeSpeed(random.randint(50,100))
        self.changeImage(images)
        self.rect.y = -300
    
    def enable_shooting(self):
        self.shooting_enabled = True

    def disable_shooting(self):
        self.shooting_enabled = False

    def invert_commands(self):
        self.inverted = True

    def revert_commands(self):
        self.inverted = False




