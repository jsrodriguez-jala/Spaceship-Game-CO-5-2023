import random
import pygame

from game.components.enemies.ship import Ship

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.spawn_timer = pygame.time.get_ticks()
        self.spawn_delay = 2000

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.spawn_timer >= self.spawn_delay:
            self.enemies.append(Ship())
            self.spawn_timer = current_time

        for enemy in self.enemies:
            enemy.update()
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)