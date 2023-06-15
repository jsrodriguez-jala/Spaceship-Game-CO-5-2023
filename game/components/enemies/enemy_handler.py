import pygame

from game.components.enemies.ship import Ship

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.spawn_timer = pygame.time.get_ticks()
        self.spawn_delay = 2000

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            
            if not enemy.is_alive:
                self.remove_enemy(enemy)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3:
            self.enemies.append(Ship())
        
        current_time = pygame.time.get_ticks()

        if current_time - self.spawn_timer >= self.spawn_delay:
            self.enemies.append(Ship())
            self.spawn_timer = current_time

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)