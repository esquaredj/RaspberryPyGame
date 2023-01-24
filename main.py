import sys
import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Raspberry Pi Game")
clock = pygame.time.Clock()

surface = pygame.Surface((100, 200))
surface.fill('deeppink')

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(surface, (0, 0))

        await asyncio.sleep(0)
        pygame.display.update()
        clock.tick(30)
asyncio.run(main())
