import pygame
from powerUp import PowerUp
from car import *

#shoot powerup
class ShootPowerUp(PowerUp):
    def __init__(self, speed):
        super().__init__('images/gun.png', effect_duration=20000, speed=speed, powerup_type='shoot')
        self.bullets = []
        self.bullet_speed = 7
        self.elapsed_time = 0
        
    #affects player for a given amount of time
    def affect_player(self):
        if self.active and self.player:  
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.activation_time

            if elapsed_time <= self.duration:
                if isinstance(self.player, Car):
                    self.player.enable_shooting()
            else:
                self.active = False
                if isinstance(self.player, Car):
                    self.player.disable_shooting()
                    # Clean up bullets when power-up deactivates
                    self.bullets = []
    #affects traffic
    def affect_traffic(self, traffic, images):
            for bullet in self.bullets:
                bullet.move()
                for car in traffic:
                    if isinstance(car, Car) and pygame.sprite.collide_rect(bullet, car):
                        car.reset_position(images)  # Replace reset_position with the logic to set y=-200
                        self.bullets.remove(bullet)

            # Remove off-screen bullets
            self.bullets = [bullet for bullet in self.bullets if bullet.rect.y > 0]
    #shooting function
    def shoot(self, x, y):
        bullet = Bullet(x, y, self.bullet_speed)
        self.bullets.append(bullet)

    def get_bullets(self):
        return self.bullets


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))  # Red bullet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self):
        self.rect.y -= self.speed
