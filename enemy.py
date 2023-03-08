import pygame
from tiles import AnimatedTile
from random import randint
from support import resource_path


class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        self.enemy_idle = resource_path('./assets/Enemies/Ghost/idle/')
        super().__init__(size, x, y, self.enemy_idle)
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 4)

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()
