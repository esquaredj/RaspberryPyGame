import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tiles import Tile, StaticTile, Crate, AnimatedTile, Coin

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = -5

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        boxes_layout = import_csv_layout(level_data['boxes'])
        self.boxes_sprites = self.create_tile_group(boxes_layout, 'boxes')

        coins_layout = import_csv_layout(level_data['coins'])
        self.coins_sprites = self.create_tile_group(coins_layout, 'coins')

    def create_tile_group(self, layout, tile_type):
        tile_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                if value != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if tile_type == 'terrain':
                        terrain_tile_list = import_cut_graphics('./assets/Terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        tile_group.add(sprite)
                    if type == 'grass':
                        grass_tile_list = import_cut_graphics('./assets/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        tile_group.add(sprite)
                    if type == 'boxes':
                        sprite = Crate(tile_size, x, y)
                        tile_group.add(sprite)

                    if type == 'coins':
                        sprite = Coin(tile_size, x, y, './assets/coins/gold')

        return tile_group

    def run(self):
        self.terrain_sprites.update(self.world_shift, 0)
        self.terrain_sprites.draw(self.display_surface)

        self.grass_sprites.update(self.world_shift, 0)
        self.grass_sprites.draw(self.display_surface)

        self.boxes_sprites.update(self.world_shift, 0)
        self.boxes_sprites.draw(self.display_surface)

        self.coins_sprites.update(self.world_shift, 0)
        self.coins_sprites.draw(self.display_surface)