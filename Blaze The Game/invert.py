import pygame
from powerUp import PowerUp
from car import Car
import random

SCREENHEIGHT = 600

class InvertPowerUp(PowerUp):
    def __init__(self, speed):
        super().__init__('images/invert.png', effect_duration=10000, speed=speed, powerup_type='invert')
        self.elapsed_time = 0
        
    def affect_player(self):
        if self.active and self.player:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.activation_time

            if elapsed_time <= self.duration:
                if isinstance(self.player, Car):
                    self.player.invert_commands()    
            else:
                self.active = False
                if isinstance(self.player, Car):
                    self.player.revert_commands()
                    
    def affect_traffic(self, traffic):
        pass