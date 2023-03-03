import pygame
from settings import *
from level import Level
from game_data import level_0
import asyncio

# Pygame setup
pygame.init()
pygame.display.set_caption('Raspberry PyGame')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_0, screen)


async def main():
    while True:
        level.run()

        pygame.display.update()
        clock.tick(45)
        await asyncio.sleep(0)


asyncio.run(main())
