import pygame
from powerUp import PowerUp
from car import Car
import random

SCREENHEIGHT = 600
#inviciblility powerup class, inherits from PowerUp
class InvincibilityPowerUp(PowerUp):
    def __init__(self, speed):
        """
        Initialize the Invincibility PowerUp.

        Parameters:
        - speed: Movement speed of the powerup on the screen.
        """
        super().__init__('images/lightning.png', effect_duration=10000, speed=speed, powerup_type='invincibility')
        #starts not affecting any player
        self.player = None
        self.elapsed_time = 0
    def affect_player(self):
        """
        Affect the player when catching the powerup during a set amount of time.
        """
        if self.active and self.player:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.activation_time

            if elapsed_time <= self.duration:
                if isinstance(self.player, Car):
                    self.player.activate_invincibility()
            else:
                self.active = False
                if isinstance(self.player, Car):
                    self.player.deactivate_invincibility()
    def affect_traffic(self, traffic):
        """
            Placeholder for the traffic affect.Does not affect traffic.

            Parameters:
            - traffic: List of traffic objects.
        """
        pass
