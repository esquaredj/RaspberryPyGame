import pygame
from support import import_folder
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface, create_jump_particles):
        super().__init__()
        self.import_assets()
        self.frame_index = 0
        self.animation_speed = 0.25
        self.image = self.animation_list['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # dust
        self.import_dust()
        self.dust_index = 0
        self.dust_speed = 0.25
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 3
        self.jump_power = -35
        self.status = 'idle'
        self.player_facing_right = True
        self.on_ground = False
        self.jump_count = 0
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        # sound effects
        self.jump_sound = pygame.mixer.Sound('sound/character/jump.wav')
        self.jump_sound.set_volume(0.2)

    def import_assets(self):
        character_path = './assets/Characters/Mask Dude/'
        self.animation_list = {'idle': [], 'run': [], 'jump': [], 'fall': [], 'double_jump': [], 'fall_double_jumped': []}

        for animation in self.animation_list.keys():
            full_path = character_path + animation
            self.animation_list[animation] = import_folder(full_path)

    def import_dust(self):
        self.running_dust = import_folder('./assets/dust_particles/run')

    def animate_player(self):
        animation = self.animation_list[self.status]

        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        if self.player_facing_right:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def dust_animation(self):
        if self.on_ground and self.status == 'run':
            self.dust_index += self.dust_speed

            if self.dust_index >= len(self.running_dust):
                self.dust_index = 0

            dust_particle = self.running_dust[int(self.dust_index)]

            if self.player_facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.display_surface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                self.display_surface.blit(pygame.transform.flip(dust_particle, True, False), pos)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.player_facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.player_facing_right = False
        else:
            self.direction.x = 0

    def event_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.base.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.jump_count < 2:
                    self.jump_count += 1
                    self.jump_sound.play()
                    self.jump()
                    self.create_jump_particles(self.rect.midbottom)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_power

    def player_status(self):
        if self.direction.y > 0:
            if self.jump_count == 0:
                self.jump_count = 1
            if self.jump_count == 1:
                self.status = 'fall'
            elif self.jump_count == 2:
                self.status = 'fall_double_jumped'
        elif self.direction.y < 0:
            if self.jump_count == 1:
                self.status = 'jump'
            else:
                self.status = 'double_jump'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def update(self):
        self.get_input()
        self.player_status()
        self.animate_player()
        self.dust_animation()
        self.event_logic()
