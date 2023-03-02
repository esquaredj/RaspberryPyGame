import asyncio
import pygame
import sys
from settings import *
from level import Level
from level_data import level_0

pygame.base.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Raspberry Pi Game")
clock = pygame.time.Clock()
level = Level(level_0, screen)


async def main():
    while True:
        screen.fill('black')#

        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.base.quit()
                sys.exit()

        level.run()
        await asyncio.sleep(0)
        pygame.display.update()
        clock.tick(30)


asyncio.run(main())
