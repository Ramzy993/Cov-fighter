import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'images')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')
MUSIC_DIR = os.path.join(ASSETS_DIR, 'music')
BUILDING_DIR = os.path.join(IMG_DIR, 'buildings')
PLAYER_DIR = os.path.join(IMG_DIR, 'player')
VIRUSES_DIR = os.path.join(IMG_DIR, 'viruses')
SHIELDS_DIR = os.path.join(IMG_DIR, 'shields')

IMG_Y_SHIFT = 50
SCREEN_HIEGHT = 640 + IMG_Y_SHIFT
SCREEN_WIDTH = 640

SPRAYER_NUM = 10
INFECTION_SPEED = 500


GAME_DAY_SPEED = 3
SAFE_PLAYER_SPEED = 10
INFECTED_PLAYER_SPEED = 4

PHOTO_128_PIXEL = 128
PHOTO_64_PIXEL = 64
PHOTO_32_PIXEL = 32
PHOTO_24_PIXEL = 24

VIRUS_X_RANGE = [i for i in range(0, int(SCREEN_WIDTH - PHOTO_24_PIXEL / 2))]
VIRUS_Y_RANGE = [i for i in range(IMG_Y_SHIFT, int(SCREEN_HIEGHT - PHOTO_24_PIXEL / 2))]
