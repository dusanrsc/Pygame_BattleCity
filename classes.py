# importing modules
import sys

# importing sub-modules
from settings import *

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