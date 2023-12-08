import pygame
from powerUp import PowerUp
from car import Car
import random

SCREENHEIGHT = 600
#slow traffic powerup
class SlowingPowerUp(PowerUp):
    def __init__(self, speed):
        super().__init__('images/snail.png', effect_duration=5000, speed=speed, powerup_type='slow')
        self.elapsed_time = 0
    #doesn't affect player
    def affect_player(self, player):
        pass 
    #affects oncoming cars velocity for a set amount of tima
    def affect_traffic(self, traffic):
        if self.active:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.activation_time

            if elapsed_time <= self.duration:
                for car in traffic:
                    if isinstance(car, Car):
                        # Temporarily reduce the speed of the car
                        car.changeSpeed(min(car.speed, self.speed / 2))
            else:
                self.active = False  # Reset the flag when the effect duration is over
                for car in traffic:
                    if isinstance(car, Car):
                        # Restore the original speed of the car
                        car.changeSpeed(car.speed + self.speed)
