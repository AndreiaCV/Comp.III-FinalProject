import pygame
import random
#define colours using RGB
WHITE = (255, 255, 255)
#Define Car class
class Car(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()
        self.original_image = pygame.image.load(image)
        self.original_image = pygame.transform.scale(self.original_image, (55, 70))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.initial_x = 0
        #set initial powerup states
        self.invincible = False
        self.shooting_enabled = False
        self.inverted = False
        self.player_number = 0

    #move right function
    def moveRight(self, pixels):
            if self.inverted and self.rect.x > 200: # Check if the car is inverted and adjust movement accordingly
                self.rect.x -= pixels
            elif not self.inverted and self.rect.x < 550:
                self.rect.x += pixels
#move left function 
    def moveLeft(self, pixels):
            if self.inverted and self.rect.x < 550: # Check if the car is inverted and adjust movement accordingly
                self.rect.x += pixels
            elif not self.inverted and self.rect.x > 200:
                self.rect.x -= pixels
#move forward function
    def moveForward(self):
        #Move the car forward by adjusting its y-coordinate based on its speed
        self.rect.y += self.speed / 25
#move backwars function
    def moveBackward(self):
        #Move the car backwards by adjusting its y-coordinate based on its speed.
        self.rect.y -= self.speed / 20
#changing speed function
    def changeSpeed(self, speed):
        self.speed = speed
    
    def changeImage(self, images):
        #Change the image of the car randomly from a given list of images.
        self.original_image = pygame.image.load(random.choice(images))
        self.original_image = pygame.transform.scale(self.original_image, (55, 70))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
    
    def slow_down(self):
        #Slow down the car's speed, ensuring it doesn't go below 1.
        self.speed = max(1, self.speed - 1)
    
    #powerup functions
    
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




