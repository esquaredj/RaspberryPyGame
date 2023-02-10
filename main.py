import asyncio
import pygame
from settings import *
from level import Level
from player import Player

pygame.base.init()
screen_width = 1200
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Raspberry Pi Game")
clock = pygame.time.Clock()
level = Level(level_map, screen)
player = Player((100, 100), screen, level.create_jump_particles)


async def main():
    while True:
        screen.fill('black')
        level.run()

        await asyncio.sleep(0)
        pygame.display.update()
        clock.tick(30)


asyncio.run(main())
