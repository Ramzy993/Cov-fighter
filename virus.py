import os
from random import choice

import general

import pygame


class Virus:
    def __init__(self, screen):
        self.screen = screen

        self.killer_virus_img = pygame.image.load(os.path.join(general.VIRUSES_DIR, 'killer.png'))
        self.notkiller_virus_img = pygame.image.load(os.path.join(general.VIRUSES_DIR, 'notkiller.png'))

        self.virus_img = self.killer_virus_img
        self.virus_dead = 0

        self.virus_img_width = general.PHOTO_24_PIXEL
        self.virus_img_height = general.PHOTO_24_PIXEL

        self.virus_position_x = 0
        self.virus_position_y = 0

        self._get_random_XY()

        while self._check_virus_position():
            self._get_random_XY()

    def _get_random_XY(self):
        self.virus_position_x = choice(general.VIRUS_X_RANGE)
        self.virus_position_y = choice(general.VIRUS_Y_RANGE)

    def _check_virus_position(self):
        return (self.virus_position_x in range(250, 250 + general.PHOTO_128_PIXEL) and self.virus_position_y in
                range(490 + general.IMG_Y_SHIFT, 490 + general.IMG_Y_SHIFT + general.PHOTO_128_PIXEL))\
               or (self.virus_position_x in range(140, 140 + general.PHOTO_128_PIXEL) and self.virus_position_y in
                   range(20 + general.IMG_Y_SHIFT, 20 + general.IMG_Y_SHIFT + general.PHOTO_128_PIXEL))

    def blit_virus(self):
        self.screen.blit(self.virus_img, (self.virus_position_x, self.virus_position_y))
