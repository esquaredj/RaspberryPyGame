import sys
import asyncio
import pygame
from settings import *
from level import Level

pygame.base.init()
screen_width = 1200
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Raspberry Pi Game")
clock = pygame.time.Clock()
level = Level(level_map, screen)

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.base.quit()
                sys.exit()

        screen.fill('black')
        level.run()

        await asyncio.sleep(0)
        pygame.display.update()
        clock.tick(30)

asyncio.run(main())