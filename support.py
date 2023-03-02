from csv import reader
import pygame
from settings import *
def import_csv_layout(path):
    terrain_layout = []
    with open(path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrain_layout.append(list(row))
        return terrain_layout

def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    tile_list = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface((tile_size, tile_size))
            new_surface.blit(surface, (x, y), pygame.Rect(x, y, tile_size, tile_size))
            tile_list.append(new_surface)

    return tile_list