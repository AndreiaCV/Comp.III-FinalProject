import pygame
from powerUp import PowerUp
from car import Car
import random

SCREENHEIGHT = 600

class InvincibilityPowerUp(PowerUp):
    def __init__(self, speed):
        super().__init__('images/lightning.png', effect_duration=10000, speed=speed, powerup_type='invincibility')
        self.player = None
        self.elapsed_time = 0
   
    def affect_player(self):
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
        pass