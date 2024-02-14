# importing modules
import pygame
import random

# game settings
# game constants
LINE_THICKNESS = 1

SCREEN_WIDTH  = 650
SCREEN_HEIGHT = 650

SCREEN_TITLE = "BattleCity"

FPS = 60
TILE = 50

PLAYER_SIZE = TILE
PLAYER_SPEED = 4
BULLET_SPEED = PLAYER_SPEED + (PLAYER_SPEED // 2)
ENEMY_SPEED = 4

# rgb color tuples
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ALPHA = GREEN

# game variables
# settings
__version__ = "v2.0"
running = True
frame = 0

player_lives = 3

direction = 0
bullet_direction = 0
bullet_counter = 0

# enemy settings
enemy_id = 20
max_enemy = 3
current_enemy = 1

enemy_direction = random.randint(0, 3)
enemy_moving_range = random.randint(0, SCREEN_WIDTH)
enemy_fireing = random.randint(0, SCREEN_WIDTH)
enemy_bullet_direction = 0
enemy_bullet_counter = 0
enemy_health = 3
upgrade_counter = 0
enemy_spawn_switch = 0

# game lists
# cpu spawn points
enemy_spawn = [0, 350, 650]

# colors
color_list = [RED, GREEN, BLUE, BLACK, WHITE, ALPHA]

# tiles
basic_tile_set = [
"static/brick.png",
"static/steel.png",
"static/forrest.png",
"static/water.png",
"static/ice.png"]

# enemy sprites
enemy_list = [
"static/enemy.png",
"static/enemy2.png"]

# player sprites
player_list = [
"static/hero.png",
"static/hero2.png"]

# upgrade sprites
upgrade_list = [
"static/1up.png",
"static/bulletsp.png",
"static/speed.png"]

# explosion prefabs
# loading images
exp0 = pygame.image.load("static/explosion/explosion0.png")
exp1 = pygame.image.load("static/explosion/explosion1.png")
exp2 = pygame.image.load("static/explosion/explosion2.png")
exp3 = pygame.image.load("static/explosion/explosion3.png")
exp4 = pygame.image.load("static/explosion/explosion4.png")
exp5 = pygame.image.load("static/explosion/explosion5.png")
exp6 = pygame.image.load("static/explosion/explosion6.png")
exp7 = pygame.image.load("static/explosion/explosion7.png")

# scaling images to requiered size
exp0 = pygame.transform.scale(exp0, (TILE, TILE))
exp1 = pygame.transform.scale(exp1, (TILE, TILE))
exp2 = pygame.transform.scale(exp2, (TILE, TILE))
exp3 = pygame.transform.scale(exp3, (TILE, TILE))
exp4 = pygame.transform.scale(exp4, (TILE, TILE))
exp5 = pygame.transform.scale(exp5, (TILE, TILE))
exp6 = pygame.transform.scale(exp6, (TILE, TILE))
exp7 = pygame.transform.scale(exp7, (TILE, TILE))

# setting up colorkey
exp0.set_colorkey(ALPHA)
exp1.set_colorkey(ALPHA)
exp2.set_colorkey(ALPHA)
exp3.set_colorkey(ALPHA)
exp4.set_colorkey(ALPHA)
exp5.set_colorkey(ALPHA)
exp6.set_colorkey(ALPHA)
exp7.set_colorkey(ALPHA)

# creating explosion list
# adding explosion seqences to list
explosion = []
explosion.append(exp0)
explosion.append(exp1)
explosion.append(exp2)
explosion.append(exp3)
explosion.append(exp4)
explosion.append(exp5)
explosion.append(exp6)
explosion.append(exp7)

""" 	  blank world
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,1,0,0,0,0,0],
[0,0,0,0,0,1,9,1,0,0,0,0,0]]
"""

world = [
[0,0,0,2,0,0,0,2,0,0,0,0,0],
[0,1,0,2,0,0,0,1,0,1,0,1,0],
[0,1,0,0,0,0,1,1,0,1,2,1,0],
[0,0,0,1,0,0,0,0,0,2,0,0,0],
[3,0,0,1,0,0,2,0,0,1,3,1,2],
[3,3,0,0,0,1,0,0,2,0,3,0,0],
[0,1,1,1,3,3,3,2,0,0,3,1,0],
[0,0,0,2,3,1,0,1,0,1,0,1,0],
[2,1,4,2,0,1,0,1,0,0,0,1,0],
[0,1,0,1,0,1,1,1,0,1,2,1,0],
[0,1,0,1,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,1,1,1,0,1,0,1,0],
[0,1,0,1,0,1,9,1,0,1,1,1,0]]

board = [
[[1,  1], [1,  2], [1,  3], [1,  4], [1,  5], [1,  6], [1,  7], [1,  8], [1,  9], [1,  10], [1,  11], [1,  12], [1,  13]],
[[2,  1], [2,  2], [2,  3], [2,  4], [2,  5], [2,  6], [2,  7], [2,  8], [2,  9], [2,  10], [2,  11], [2,  12], [2,  13]],
[[3,  1], [3,  2], [3,  3], [3,  4], [3,  5], [3,  6], [3,  7], [3,  8], [3,  9], [3,  10], [3,  11], [3,  12], [3,  13]],
[[4,  1], [4,  2], [4,  3], [4,  4], [4,  5], [4,  6], [4,  7], [4,  8], [4,  9], [4,  10], [4,  11], [4,  12], [4,  13]],
[[5,  1], [5,  2], [5,  3], [5,  4], [5,  5], [5,  6], [5,  7], [5,  8], [5,  9], [5,  10], [5,  11], [5,  12], [5,  13]],
[[6,  1], [6,  2], [6,  3], [6,  4], [6,  5], [6,  6], [6,  7], [6,  8], [6,  9], [6,  10], [6,  11], [6,  12], [6,  13]],
[[7,  1], [7,  2], [7,  3], [7,  4], [7,  5], [7,  6], [7,  7], [7,  8], [7,  9], [7,  10], [7,  11], [7,  12], [7,  13]],
[[8,  1], [8,  2], [8,  3], [8,  4], [8,  5], [8,  6], [8,  7], [8,  8], [8,  9], [8,  10], [8,  11], [8,  12], [8,  13]],
[[9,  1], [9,  2], [9,  3], [9,  4], [9,  5], [9,  6], [9,  7], [9,  8], [9,  9], [9,  10], [9,  11], [9,  12], [9,  13]],
[[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13]],
[[11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11], [11, 12], [11, 13]],
[[12, 1], [12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [12, 13]],
[[13, 1], [13, 2], [13, 3], [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13]]]

# setting up screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TITLE = pygame.display.set_caption(f"{SCREEN_TITLE} {__version__}")
MOUSE_VISIBILITY = pygame.mouse.set_visible(False)