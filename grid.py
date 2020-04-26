import os
import threading

import general

from pygame import time, display, image, font


class Grid:

    def __init__(self, screen):
        self.screen = screen
        self.background_img = image.load(os.path.join(general.IMG_DIR, 'background.jpg'))
        self.icon = image.load(os.path.join(general.SHIELDS_DIR, 'safe.png'))

        self.quarantine_days = 15
        self.quarantine_days_X = 10
        self.quarantine_days_Y = 10

        self.sprayer_nums = general.SPRAYER_NUM
        self.sprayer_X = 180
        self.sprayer_Y = 10

        self.distance_X = 280
        self.distance_Y = 10

        self.infection_nums = 0
        self.infection_X = 390
        self.infection_Y = 10

        self.safe_guard_img = image.load(os.path.join(general.SHIELDS_DIR, 'safe.png'))
        self.unsafe_guard_img = image.load(os.path.join(general.SHIELDS_DIR, 'unsafe.png'))
        self.home = {'home': {'image': image.load(os.path.join(general.BUILDING_DIR, 'home.png')),
                              'origin': (270, 540), 'guard': self.safe_guard_img}}
        self.buildings = {
            'hospital': {'image': image.load(os.path.join(general.BUILDING_DIR, 'hospital.png')),
                         'origin': (150, 70), 'guard': self.safe_guard_img},
            'market': {'image': image.load(os.path.join(general.BUILDING_DIR, 'market.png')),
                       'origin': (540, 80), 'guard': self.safe_guard_img},
            'building': {'image': image.load(os.path.join(general.BUILDING_DIR, 'building.png')),
                         'origin': (170, 220), 'guard': self.safe_guard_img},
            'building1': {'image': image.load(os.path.join(general.BUILDING_DIR, 'building1.png')),
                          'origin': (50, 400), 'guard': self.safe_guard_img},
            'building2': {'image': image.load(os.path.join(general.BUILDING_DIR, 'building2.png')),
                          'origin': (40, 580), 'guard': self.safe_guard_img},
            'building3': {'image': image.load(os.path.join(general.BUILDING_DIR, 'building3.png')),
                          'origin': (420, 180), 'guard': self.safe_guard_img},
            'building4': {'image': image.load(os.path.join(general.BUILDING_DIR, 'building4.png')),
                          'origin': (540, 300), 'guard': self.safe_guard_img},
            # 'fence': {'image': image.load(os.path.join(general.BUILDING_DIR, 'fence.png')),
            #           'origin': (280, 260), 'guard': self.safe_guard_img},
        }

        self.dist_font = font.Font('freesansbold.ttf', 10)
        self.screen_font = font.Font(str(os.path.join(general.FONTS_DIR, 'GrandHotel-Regular.otf')), 24)
        self.text_font = font.Font(str(os.path.join(general.FONTS_DIR, 'GrandHotel-Regular.otf')), 50)
        self.game_over_font = font.Font(str(os.path.join(general.FONTS_DIR, 'Sensations and Qualities.ttf')), 64)

        self.game_status = 'home'
        self.game_end = 0

    def grid_init(self):
        self.screen.fill((50, 0, 0))
        self.screen.blit(self.background_img, (0, general.IMG_Y_SHIFT))
        display.set_caption("Fighting Corona Virus                              #STAY_HOME_STAY_SAFE")
        display.set_icon(self.icon)

        score = self.screen_font.render("Quarantine Days: {}".format(self.quarantine_days), True, (255, 255, 225))
        self.screen.blit(score, (self.quarantine_days_X, self.quarantine_days_Y))

        sprayer = self.screen_font.render("Sprayer: {}".format(self.sprayer_nums), True, (255, 255, 225))
        self.screen.blit(sprayer, (self.sprayer_X, self.sprayer_Y))

        dist = self.dist_font.render("|-- Social Distance --|", True, (255, 255, 225))
        self.screen.blit(dist, (self.distance_X, self.distance_Y))

        infection = self.screen_font.render("Number of Infected People: {}".format(self.infection_nums), True,
                                            (255, 255, 225))
        self.screen.blit(infection, (self.infection_X, self.infection_Y))

        for key, value in self.buildings.items():
            self.screen.blit(value['image'], value['origin'] + (0, general.IMG_Y_SHIFT))
            self.screen.blit(value['guard'], value['origin'] + (0, general.IMG_Y_SHIFT))

    def blit_home(self):
        self.screen.blit(self.home['home']['image'], self.home['home']['origin'] + (0, general.IMG_Y_SHIFT))
        self.screen.blit(self.home['home']['guard'], self.home['home']['origin'] + (0, general.IMG_Y_SHIFT))

    def check_building_vs_virus(self, virus_x, virus_y):
        for key, value in self.buildings.items():
            if virus_x + general.PHOTO_24_PIXEL / 2 in range(value['origin'][0],
                                                             value['origin'][0] + general.PHOTO_64_PIXEL) \
                    and virus_y + general.PHOTO_24_PIXEL / 2 in range(value['origin'][1],
                                                                      value['origin'][1] + general.PHOTO_64_PIXEL):
                self.buildings[key]['guard'] = self.unsafe_guard_img

    def update_quarantine_days(self):
        timer = threading.Timer(float(general.GAME_DAY_SPEED), self.update_quarantine_days)
        timer.start()
        if self.game_status == "home":
            self.quarantine_days -= 1
        if self.game_end:
            timer.cancel()

    def blit_text(self):
        self.screen.blit(self.text_font.render("Go to Market and take care", True, (255, 255, 255), (0, 0, 0)), (130, 400))

    def blit_text2(self):
        self.screen.blit(self.text_font.render("Go to Home and take care", True, (255, 255, 255), (0, 0, 0)), (150, 400))

    def blit_text3(self):
        self.screen.blit(self.text_font.render("Go to Hospital", True, (255, 255, 255), (0, 0, 0)), (190, 400))

    def blit_game_over(self):
        self.screen.blit(self.game_over_font.render("GAME OVER", True, (255, 255, 255), (255, 0, 0)), (170, 350))

    def blit_game_ended(self):
        self.screen.blit(self.game_over_font.render("You Overcome the Virus", True, (0, 0, 0), (0, 255, 0)), (170, 350))
