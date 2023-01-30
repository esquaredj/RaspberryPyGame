import pygame
from os import walk
def import_folder(path):
    surfaces = []

    for _, __, images in walk(path):
        for image in images:
            final_path = path + '/' + image
            image_surface = pygame.image.load(final_path).convert_alpha()
            surfaces.append(image_surface)

    return surfaces