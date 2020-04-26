import random
import os

import pygame
from pygame import mixer

from grid import Grid
from player import Player
from virus import Virus

import general

pygame.init()
screen = pygame.display.set_mode((general.SCREEN_WIDTH, general.SCREEN_HIEGHT))

mixer.music.load(os.path.join(general.MUSIC_DIR, "background.mp3"))
mixer.music.play(-1)
# spray_sound = mixer.Sound(os.path.join(general.MUSIC_DIR, "spray.mp3"))

grid = Grid(screen)
grid.update_quarantine_days()

player = Player(screen)

viruses = []

running = True
while running:

    grid.grid_init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if grid.game_status != "home":

            if event.type == pygame.KEYDOWN:
                player.move_player(event.key)

                if event.key == pygame.K_SPACE and grid.sprayer_nums > 0:
                    grid.sprayer_nums -= 1
                    player.blit_spray_img()
                    pygame.display.update()
                    pygame.time.wait(300)
                    spray_sound.play()
                    for virus in viruses:
                        if player.check_distance(virus.virus_position_x + general.PHOTO_24_PIXEL / 2,
                                                 virus.virus_position_y + general.PHOTO_24_PIXEL / 2,
                                                 general.PHOTO_64_PIXEL / 2 + general.PHOTO_24_PIXEL / 2 + 20):
                            virus.virus_img = virus.notkiller_virus_img
                            virus.virus_dead = 1

    if grid.game_status != "home":
        if not player.player_infected:
            for virus in viruses:
                if player.check_distance(virus.virus_position_x + general.PHOTO_24_PIXEL / 2,
                                         virus.virus_position_y + general.PHOTO_24_PIXEL / 2,
                                         general.PHOTO_64_PIXEL / 2 + general.PHOTO_24_PIXEL / 2) and virus.virus_dead == 0:
                    player.player_infected = 1
                    grid.blit_text3()
                    pygame.display.update()
                    pygame.time.wait(2900)
                    grid.quarantine_days = 14
                    break

        # check hospital position
        if player.check_player_position(150, 20 + general.IMG_Y_SHIFT, general.PHOTO_64_PIXEL) \
                and player.player_infected:
            grid.blit_text2()
            pygame.display.update()
            pygame.time.wait(2900)
            player.player_infected = 0

        # check market position
        if player.check_player_position(530, 20 + general.IMG_Y_SHIFT, 32) and grid.game_status == "market":
            grid.blit_text2()
            pygame.display.update()
            pygame.time.wait(2900)
            grid.game_status = 'move'
            grid.quarantine_days -= 1

        # check if player infect his family
        if player.check_player_position(280, 500 + general.IMG_Y_SHIFT, general.PHOTO_128_PIXEL):
            if player.player_infected:
                grid.blit_game_over()
                pygame.display.update()
                pygame.time.wait(5000)
                running = False

        # check home position
        if player.check_player_position(280, 500 + general.IMG_Y_SHIFT, general.PHOTO_64_PIXEL) \
                and grid.game_status == "move":
            grid.game_status = 'home'

    # create virus
    if random.randint(0, general.INFECTION_SPEED) == 0:
        v = Virus(screen)
        viruses.append(v)
        grid.check_building_vs_virus(v.virus_position_x, v.virus_position_y)
        grid.infection_nums += 1

    # blit viruses
    for virus in viruses:
        virus.blit_virus()

    # home game status
    if grid.game_status == 'home':
        if grid.quarantine_days in [1, 5, 10]:
            grid.blit_text()
            pygame.display.update()
            pygame.time.wait(2900)
            grid.game_status = 'market'

        if grid.quarantine_days < 0:
            grid.blit_game_ended()
            pygame.display.update()
            pygame.time.wait(5000)
            running = False

    player.blit_player_img()
    grid.blit_home()
    pygame.display.update()

grid.game_end = 1
