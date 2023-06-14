import pygame
import random

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class Ship(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        if random.choice([True, False]):
            self.image = ENEMY_1
        else:
            self.image = ENEMY_2
            
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)