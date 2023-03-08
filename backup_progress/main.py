import pygame
from settings import *
from level import Level
from overworld import Overworld
import asyncio


class Game:
    def __init__(self):
        self.max_level = 2
        self.overworld = Overworld(1, self.max_level, screen, self.create_level)
        self.status = 'overworld'

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld)
        self.status = 'level'

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()


# Pygame setup
pygame.init()
pygame.display.set_caption('Raspberry PyGame')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()


async def main():
    while True:
        game.run()

        pygame.display.update()
        clock.tick(37)
        await asyncio.sleep(0)


asyncio.run(main())
