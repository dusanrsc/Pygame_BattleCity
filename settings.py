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
__version__ = "v1.0"
running = True

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
"static/steel.png",
"static/brick.png",
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