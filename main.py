# all static files (sprites) must be in the same path as 'main.pyw' for proper working
# importing modules
import pygame
import random
import sys

# importing sub-modules
from random import randint

# game settings
# game constants
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
SCREEN_TITLE = "BattleCity"

FPS = 60
TILE = 50

PLAYER_SPEED = 5
PLAYER_SIZE = TILE
BULLET_SPEED = PLAYER_SPEED * 2

ENEMY_SPEED = 5

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

direction = 0
bullet_counter = 0

# enemy settings
enemy_id = 20
max_enemy = 4

enemy_direction = random.randint(0, 3)
enemy_moving_range = random.randint(0, SCREEN_WIDTH)

enemy_fireing = 0

# game lists
# cpu spawn points
enemy_spawn = [0, 350, 650]
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

# level = [
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [1,  1], [1,  1], [1,  1], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]],
# [[0,  0], [0,  0], [0,  0], [0,  0], [0,  0], [1,  1], [0,  0], [1,  1], [0,  0], [0,  0], [0,  0], [0,  0], [0,  0]]]

# setting up screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TITLE = pygame.display.set_caption(f"{SCREEN_TITLE} {__version__}")
MOUSE_VISIBILITY = pygame.mouse.set_visible(False)

# initializing modules
pygame.init()
pygame.mixer.init()
pygame.font.init()

# game classes
# class player
class Player(pygame.sprite.Sprite):
	def __init__(self, img="static/herow.png", pos_x=5, pos_y=13):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x * 50 - 25, pos_y * 50 - 25])

	def update(self):
		# restricting player go out the world boundaries
		if self.rect.x >= SCREEN_WIDTH - PLAYER_SIZE:
			self.rect.x = SCREEN_WIDTH - PLAYER_SIZE
		if self.rect.y >= SCREEN_HEIGHT - PLAYER_SIZE:
			self.rect.y = SCREEN_WIDTH - PLAYER_SIZE
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.y <= 0:
			self.rect.y = 0

class Block(pygame.sprite.Sprite):
	def __init__(self, img="static/brick_wall.png", pos_x=6, pos_y=13):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x * 50 - 25, pos_y * 50 - 25])

	def update(self):
		pass

class Bullet(pygame.sprite.Sprite):
	def __init__(self, img="static/bullet.png", pos_x=25, pos_y=25):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	def update(self):
		# updating bullet movement
		if direction == 0:
			self.rect.y -= BULLET_SPEED
		if direction == 2:
			self.rect.y += BULLET_SPEED
		if direction == 3:
			self.rect.x -= BULLET_SPEED
		if direction == 1:
			self.rect.x += BULLET_SPEED

class Enemy(pygame.sprite.Sprite):
	def __init__(self, img="static/enemys.png", pos_x=enemy_spawn[random.randint(0, 2)], pos_y=25):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x - 25, pos_y - 25])

	def update(self):
		# restricting enemy go out the world boundaries
		if self.rect.x >= SCREEN_WIDTH - PLAYER_SIZE:
			self.rect.x = SCREEN_WIDTH - PLAYER_SIZE
		if self.rect.y >= SCREEN_HEIGHT - PLAYER_SIZE:
			self.rect.y = SCREEN_WIDTH - PLAYER_SIZE
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.y <= 0:
			self.rect.y = 0

# game functions
# exit game function
def exit():
	pygame.quit()
	sys.exit()
	running = False

def game_menu():
	pass

def game_pause():
	pass

# creating instance of class
player_group = pygame.sprite.Group()
player = Player(img="static/hero.png")
player_group.add(player)

flag_group = pygame.sprite.Group()
flag = Block(pos_x=7, pos_y=13, img="static/flag.png")
flag_group.add(flag)

brickwall_group = pygame.sprite.Group()
# primitive level construction
for item in board[1:12:]:
	for index, value in item[1:12:]:
		print(index, value)
		brickwall = Block(pos_x=index, pos_y=value, img="static/brick_wall.png")
		brickwall_group.add(brickwall)

# for item in level:
# 	for index, value in item:
# 		if index == 1 and value == 1:
# 			print(index, value)
# 			brickwall = Block(pos_x=index, pos_y=value, img="static/brick_wall.png")
# 			brickwall_group.add(brickwall)
# 		else:
# 			pass

bullet_group = pygame.sprite.Group()
bullet = Bullet(pos_x=player.rect.x, pos_y=player.rect.y)

enemy_group = pygame.sprite.Group()
enemy = Enemy(img="static/enemy.png")
enemy.image = pygame.transform.rotate(enemy.image, 180)
enemy_group.add(enemy)

# main game loop
while running:
	# events
	# key input
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# fiering bullet mechanism
	if keys[pygame.K_SPACE] and bullet_counter != 1:
		bullet_counter += 1

		bullet_group = pygame.sprite.Group()
		bullet = Bullet(pos_x=player.rect.x + PLAYER_SIZE // 2, pos_y=player.rect.y + PLAYER_SIZE // 2)
		bullet_group.add(bullet)

	# player movement mechanism
	if keys[pygame.K_w]:
		direction = 0
		player.rect.y -= PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image.set_colorkey(ALPHA)

	elif keys[pygame.K_a]:
		direction = 3
		player.rect.x -= PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 90)
		player.image.set_colorkey(ALPHA)

	elif keys[pygame.K_s]:
		direction = 2
		player.rect.y += PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 180)
		player.image.set_colorkey(ALPHA)

	elif keys[pygame.K_d]:
		direction = 1
		player.rect.x += PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 270)
		player.image.set_colorkey(ALPHA)

	# destroying bullet and reseting bullet conditions 
	if bullet.rect.y <= 0:
		bullet.kill()
		bullet_counter = 0

	if bullet.rect.y >= SCREEN_HEIGHT:
		bullet.kill()
		bullet_counter = 0

	if bullet.rect.x <= 0:
		bullet.kill()
		bullet_counter = 0

	if bullet.rect.x >= SCREEN_WIDTH:
		bullet.kill()
		bullet_counter = 0

	# direction
	if direction == 0:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image.set_colorkey(ALPHA)

	if direction == 3:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 90)
		bullet.image.set_colorkey(ALPHA)

	if direction == 2:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 180)
		bullet.image.set_colorkey(ALPHA)

	if direction == 1:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 270)
		bullet.image.set_colorkey(ALPHA)

	# enemy moving direction
	if enemy_direction == 0:
		enemy.rect.y -= ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image.set_colorkey(ALPHA)

		if enemy.rect.y <= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

	elif enemy_direction == 2:
		enemy.rect.y += ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image = pygame.transform.rotate(enemy.image, 180)
		enemy.image.set_colorkey(ALPHA)

		if enemy.rect.y >= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

	elif enemy_direction == 1:
		enemy.rect.x += ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image = pygame.transform.rotate(enemy.image, 270)
		enemy.image.set_colorkey(ALPHA)

		if enemy.rect.x >= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

	elif enemy_direction == 3:
		enemy.rect.x -= ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image = pygame.transform.rotate(enemy.image, 90)
		enemy.image.set_colorkey(ALPHA)

		if enemy.rect.x <= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

	# collision section
	# if players bullet hit enemy
	if pygame.sprite.groupcollide(bullet_group, enemy_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		enemy_id -= 1
		bullet_counter = 0

		if enemy_id >= 0:
			enemy_group = pygame.sprite.Group()
			enemy = Enemy(img="static/enemy.png", pos_x=enemy_spawn[random.randint(0, 2)])
			enemy.image = pygame.transform.rotate(enemy.image, 180)
			enemy_group.add(enemy)

			enemy_direction = random.randint(0, 3)
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
		else:
			enemy.kill()

	# if players bullet hit flag
	if pygame.sprite.groupcollide(bullet_group, flag_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		exit()

	# if players bullet hit brickwall
	if pygame.sprite.groupcollide(bullet_group, brickwall_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		bullet_counter = 0

	# if player hit enemy
	if pygame.sprite.groupcollide(player_group, enemy_group, False, False, pygame.sprite.collide_rect_ratio(.85)):
		enemy_direction = random.randint(0, 3)
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)

	# if enemy hit flag
	if pygame.sprite.groupcollide(enemy_group, flag_group, False, False, pygame.sprite.collide_rect_ratio(.85)):
		enemy_direction = random.randint(0, 3)
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)

	# drawing sprites on the screen
	SCREEN.fill(BLACK)

	brickwall_group.update()
	brickwall_group.draw(SCREEN)

	bullet_group.update()
	bullet_group.draw(SCREEN)

	player_group.update()
	player_group.draw(SCREEN)

	flag_group.update()
	flag_group.draw(SCREEN)

	enemy_group.update()
	enemy_group.draw(SCREEN)

	# for l1 in range(0, SCREEN_WIDTH, TILE):
	# 	pygame.draw.line(SCREEN, GREEN, (0, l1), (SCREEN_WIDTH, l1))
	# 	for l2 in range(0, SCREEN_WIDTH, TILE):
	# 		pygame.draw.line(SCREEN, GREEN, (l2, 0), (l2, SCREEN_HEIGHT))

	# fps counter
	pygame.display.flip()
	pygame.time.Clock().tick(FPS)