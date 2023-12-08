import pygame
import random
#define colours using RGB
WHITE = (255, 255, 255)
#Define Car class
class Car(pygame.sprite.Sprite):
    """
    Parent class representing the cars in the game.

    Attributes:
    - image (str): The path to the cars image file.
    - speed (float): The speed of the car.
    - original_image (pygame.Surface): The original image of the car.
    - image (pygame.Surface): The current image of the car.
    - rect (pygame.Rect): The rectangular area occupied by the car.
    - initial_x (int): The initial x-coordinate of the car.
    - invincible (bool): A flag indicating whether the car is invincible.
    - shooting_enabled (bool): A flag indicating whether the powerup for shooting is enabled .
    - inverted (bool): A flag indicating whether the powerup inverted is enabled.
    - player_number (int): The player number associated with the car.
    """
    def __init__(self, image, speed):
        """
        Initialize a new instance of the Car class.

        Parameters:
        - image (str): The path to the cars image file .
        - speed (float): The speed of the car.
        """

        super().__init__()
        self.original_image = pygame.image.load(image) #load original image
        self.original_image = pygame.transform.scale(self.original_image, (55, 70)) #scale image
        self.image = self.original_image.copy() 
        self.rect = self.image.get_rect() # rectangle area ocupied by the car
        self.speed = speed 
        self.initial_x = 0 
        #set initial powerup states
        self.invincible = False
        self.shooting_enabled = False
        self.inverted = False
        self.player_number = 0

    #move right function
    def moveRight(self, pixels):
        """
        Move the car to the right within the street limits.

        Parameters:
        - pixels (int): The number of pixels the cars move to move the car to the right.
        """
        if self.inverted and self.rect.x > 200: # Check if the car is inverted and adjust movement accordingly
            self.rect.x -= pixels
        elif not self.inverted and self.rect.x < 550:
            self.rect.x += pixels
#move left function 
    def moveLeft(self, pixels):
        """
        Move the car to the left within the street limits.

        Parameters:
        - pixels (int): The number of pixels the cars move to move the car to the left.
        """
        if self.inverted and self.rect.x < 550: # Check if the car is inverted and adjust movement accordingly
            self.rect.x += pixels
        elif not self.inverted and self.rect.x > 200:
            self.rect.x -= pixels
#move forward function
    def moveForward(self):
        """Move the car forward.
        Adjusting its y-coordinate based on its speed
        """
        self.rect.y += self.speed / 25  # Adjust y coordinate based on speed


#move backwars function
    def moveBackward(self):
        """Move the car backwards.
        Adjusting its y-coordinate based on its speed
        """
        self.rect.y -= self.speed / 20 # adjust y coordinate based on speed
#changing speed function
    def changeSpeed(self, speed):
        """
        Change the speed of the car.

        Parameters:
        - speed (float): The new speed of the car.
        """
        self.speed = speed #new speed
    
    def changeImage(self, images):
        """
        Change the image of the car randomly from a given list of images.

        Parameters:
        - images (list): A list of image paths to choose from.
        """
        self.original_image = pygame.image.load(random.choice(images)) #upload random image from list
        self.original_image = pygame.transform.scale(self.original_image, (55, 70)) #scale image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect() #area occupied by the car
    
    def slow_down(self):
        """Slow down the car's speed, ensuring it doesn't go below 1."""
        self.speed = max(1, self.speed - 1)
    
    #powerup functions
    
    def activate_invincibility(self):
        """Activate invincibility for the car."""
        self.invincible = True

    def deactivate_invincibility(self):
        """Deactivate invincibility for the car."""
        self.invincible = False

    def reset_position(self, images):
        """
        Reset the position of the car with a new speed and image.

        Parameters:
        - images (list): A list of image paths to choose from.
        """
        self.changeSpeed(random.randint(50,100))
        self.changeImage(images)
        self.rect.y = -300
    
    def enable_shooting(self):
        """Enable shooting for the car."""
        self.shooting_enabled = True

    def disable_shooting(self):
        """Disable shooting for the car."""
        self.shooting_enabled = False

    def invert_commands(self):
        """Invert the commands for the car."""
        self.inverted = True

    def revert_commands(self):
        """Revert the commands for the car to the original."""
        self.inverted = False




