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
PLAYER_SPEED = 5
PLAYER_SIZE = 50
BULLET_SPEED = PLAYER_SPEED * 2

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
direction = "w"
running = True

# enemy settings
enemy_id = 20
max_enemy = 4
move_range = random.randint(25, 625)

# game lists
# cpu spawn points
enemy_spawn = [25, 325, 625]

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
	def __init__(self, img="static/herow.png", pos_x=275, pos_y=625):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

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

class Bullet(pygame.sprite.Sprite):
	def __init__(self, img="static/bullet.png", pos_x=25, pos_y=25):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	def update(self):
		# updating bullet movement
		if direction == "w":
			self.rect.y -= BULLET_SPEED
		if direction == "s":
			self.rect.y += BULLET_SPEED
		if direction == "a":
			self.rect.x -= BULLET_SPEED
		if direction == "d":
			self.rect.x += BULLET_SPEED

		# destroying bullet condition
		if self.rect.y <= 0:
			self.kill()
		if self.rect.y >= SCREEN_HEIGHT:
			self.kill()
		if self.rect.x <= 0:
			self.kill()
		if self.rect.x >= SCREEN_WIDTH:
			self.kill()

class Enemy(pygame.sprite.Sprite):
	def __init__(self, img="static/enemys.png", pos_x=enemy_spawn[random.randint(0, 2)], pos_y=25):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

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

		# movement mechanism


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

bullet_group = pygame.sprite.Group()
bullet = Bullet(pos_x=player.rect.x, pos_y=player.rect.y)

enemy_group = pygame.sprite.Group()
enemy = Enemy(img="static/enemy.png", pos_x=enemy_spawn[random.randint(0, 2)])
enemy.image = pygame.transform.rotate(enemy.image, 180)
enemy_group.add(enemy)

# main game loop
while running:
	# events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# key input
	keys = pygame.key.get_pressed()
	# player movement mechanism
	if keys[pygame.K_w]:
		direction = "w"
		player.rect.y -= PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image.set_colorkey(ALPHA)

	elif keys[pygame.K_a]:
		direction = "a"
		player.rect.x -= PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 90)
		player.image.set_colorkey(ALPHA)

	elif keys[pygame.K_s]:
		direction = "s"
		player.rect.y += PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 180)
		player.image.set_colorkey(ALPHA)

	elif keys[pygame.K_d]:
		direction = "d"
		player.rect.x += PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 270)
		player.image.set_colorkey(ALPHA)

	# direction
	if direction == "w":
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image.set_colorkey(ALPHA)

	elif direction == "a":
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 90)
		bullet.image.set_colorkey(ALPHA)

	elif direction == "s":
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 180)
		bullet.image.set_colorkey(ALPHA)

	elif direction == "d":
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 270)
		bullet.image.set_colorkey(ALPHA)

	# fiering bullet mechanism
	if keys[pygame.K_SPACE]:
		bullet_group = pygame.sprite.Group()
		bullet = Bullet(pos_x=player.rect.x + PLAYER_SIZE // 2, pos_y=player.rect.y + PLAYER_SIZE // 2)
		bullet_group.add(bullet)

	# if player bullet hit enemy
	if pygame.sprite.groupcollide(bullet_group, enemy_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		enemy_id -= 1

		if enemy_id >= 0:
			enemy_group = pygame.sprite.Group()
			enemy = Enemy(img="static/enemy.png", pos_x=enemy_spawn[random.randint(0, 2)])
			enemy.image = pygame.transform.rotate(enemy.image, 180)
			enemy_group.add(enemy)
		else:
			enemy.kill()

	# drawing sprites on the screen
	SCREEN.fill(BLACK)

	bullet_group.update()
	bullet_group.draw(SCREEN)

	player_group.update()
	player_group.draw(SCREEN)

	enemy_group.update()
	enemy_group.draw(SCREEN)

	# fps counter
	pygame.display.flip()
	pygame.time.Clock().tick(FPS)