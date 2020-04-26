import os
import math

import general

import pygame


class Player:
    def __init__(self, screen):
        self.screen = screen

        self.safe_player_img = pygame.image.load(os.path.join(general.PLAYER_DIR, 'safe.png'))
        self.infected_player_img = pygame.image.load(os.path.join(general.PLAYER_DIR, 'infected.png'))
        self.spray_img = pygame.image.load(os.path.join(general.PLAYER_DIR, 'spray.png'))

        self.player_infected = 0
        self.player_img = self.safe_player_img

        self.player_img_width = general.PHOTO_64_PIXEL - 4
        self.player_img_height = general.PHOTO_64_PIXEL

        self.player_position_x = int(general.SCREEN_WIDTH / 2 - self.player_img_width / 2)
        self.player_position_y = int(general.SCREEN_WIDTH - self.player_img_height)

        self.player_movement_pixels_x = general.SAFE_PLAYER_SPEED
        self.player_movement_pixels_y = general.SAFE_PLAYER_SPEED

    def move_player(self, key):

        if self.player_infected:
            self.player_img = self.infected_player_img
            self.player_movement_pixels_x = general.INFECTED_PLAYER_SPEED
            self.player_movement_pixels_y = general.INFECTED_PLAYER_SPEED
        else:
            self.player_img = self.safe_player_img
            self.player_movement_pixels_x = general.SAFE_PLAYER_SPEED
            self.player_movement_pixels_y = general.SAFE_PLAYER_SPEED

        if key == pygame.K_LEFT:
            self.player_position_x = self.player_position_x - self.player_movement_pixels_x

        if key == pygame.K_RIGHT:
            self.player_position_x = self.player_position_x + self.player_movement_pixels_x

        if key == pygame.K_UP:
            self.player_position_y = self.player_position_y - self.player_movement_pixels_y

        if key == pygame.K_DOWN:
            self.player_position_y = self.player_position_y + self.player_movement_pixels_y

        self._check_player_position()

    def _check_player_position(self):
        if self.player_position_x <= 0:
            self.player_position_x = 0

        if self.player_position_x >= general.SCREEN_WIDTH - self.player_img_width:
            self.player_position_x = general.SCREEN_WIDTH - self.player_img_width

        if self.player_position_y <= general.IMG_Y_SHIFT:
            self.player_position_y = general.IMG_Y_SHIFT

        if self.player_position_y >= general.SCREEN_HIEGHT + general.IMG_Y_SHIFT - self.player_img_height:
            self.player_position_x = general.SCREEN_HIEGHT + general.IMG_Y_SHIFT - self.player_img_height

    def check_distance(self, virus_x, virus_y, dist):
        distance = math.sqrt(math.pow(self.player_position_x + self.player_img_width/2 - virus_x, 2) +
                             math.pow(self.player_position_y + self.player_img_height/2 - virus_y, 2))
        if distance < dist:
            return True
        return False

    def check_player_position(self, object_x, object_y, object_h_w):
        return self.player_position_x in range(object_x, object_x + object_h_w) \
               and self.player_position_y in range(object_y, object_y + object_h_w)

    def blit_player_img(self):
        self.screen.blit(self.player_img, (self.player_position_x, self.player_position_y))

    def blit_spray_img(self):
        self.screen.blit(self.spray_img, (self.player_position_x - 25, self.player_position_y - 25))