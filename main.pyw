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

# initializing modules
pygame.init()
pygame.mixer.init()
pygame.font.init()

# creating instance of class
player_group = pygame.sprite.Group()
player = Player(img="static/hero.png")
player_group.add(player)

flag_group = pygame.sprite.Group()
flag = Block(pos_x=7, pos_y=13, img="static/flag.png")
flag_group.add(flag)

brickwall_group = pygame.sprite.Group()
# primitive level construction
# base wrapper
for item in board[5:8:]:
	for index, value in item[11:13:]:
		brickwall = Block(pos_x=index, pos_y=value, img=tile_set[0])
		brickwall_group.add(brickwall)

# level creator
for item in board[3:10:]:
	for index, value in item[3:10:]:
		brickwall = Block(pos_x=index, pos_y=value, img=random.choice(tile_set))
		brickwall_group.add(brickwall)

bullet_group = pygame.sprite.Group()
bullet = Bullet(pos_x=player.rect.x, pos_y=player.rect.y)

enemy_group = pygame.sprite.Group()
enemy = Enemy(img="static/enemy.png")
enemy.image = pygame.transform.rotate(enemy.image, 180)
enemy_group.add(enemy)

enemy_bullet_group = pygame.sprite.Group()
enemy_bullet = Bullet(pos_x=enemy.rect.x, pos_y=enemy.rect.y)

# main game loop
while running:
	# events
	# key input
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# fiering bullet mechanism
	# fireing players bullet
	if keys[pygame.K_SPACE] and bullet_counter != 1:
		bullet_counter += 1

		bullet_group = pygame.sprite.Group()
		bullet = Bullet(pos_x=player.rect.x + TILE // 2, pos_y=player.rect.y + TILE // 2)
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

		enemy_bullet.image = pygame.image.load("static/bullet.png").convert()
		enemy_bullet.image.set_colorkey(ALPHA)

		if enemy.rect.y <= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

			# enemy fiering mechanism
			if enemy.rect.y <= enemy_fireing:
				enemy_bullet_group = pygame.sprite.Group()
				enemy_bullet = Bullet(pos_x=enemy.rect.x + TILE // 2, pos_y=enemy.rect.y + TILE // 2)
				enemy_bullet_group.add(enemy_bullet)

	elif enemy_direction == 2:
		enemy.rect.y += ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image = pygame.transform.rotate(enemy.image, 180)
		enemy.image.set_colorkey(ALPHA)

		enemy_bullet.image = pygame.image.load("static/bullet.png").convert()
		enemy_bullet.image = pygame.transform.rotate(bullet.image, 180)
		enemy_bullet.image.set_colorkey(ALPHA)

		if enemy.rect.y >= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

			# enemy fiering mechanism
			if enemy.rect.y >= enemy_fireing:
				enemy_bullet_group = pygame.sprite.Group()
				enemy_bullet = Bullet(pos_x=enemy.rect.x + TILE // 2, pos_y=enemy.rect.y + TILE // 2)
				enemy_bullet_group.add(enemy_bullet)

	elif enemy_direction == 1:
		enemy.rect.x += ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image = pygame.transform.rotate(enemy.image, 270)
		enemy.image.set_colorkey(ALPHA)

		enemy_bullet.image = pygame.image.load("static/bullet.png").convert()
		enemy_bullet.image = pygame.transform.rotate(bullet.image, 270)
		enemy_bullet.image.set_colorkey(ALPHA)

		if enemy.rect.x >= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

			# enemy fiering mechanism
			if enemy.rect.x >= enemy_fireing:
				enemy_bullet_group = pygame.sprite.Group()
				enemy_bullet = Bullet(pos_x=enemy.rect.x + TILE // 2, pos_y=enemy.rect.y + TILE // 2)
				enemy_bullet_group.add(enemy_bullet)

	elif enemy_direction == 3:
		enemy.rect.x -= ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image = pygame.transform.rotate(enemy.image, 90)
		enemy.image.set_colorkey(ALPHA)

		enemy_bullet.image = pygame.image.load("static/bullet.png").convert()
		enemy_bullet.image = pygame.transform.rotate(bullet.image, 90)
		enemy_bullet.image.set_colorkey(ALPHA)

		if enemy.rect.x <= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

			# enemy fiering mechanism
			if enemy.rect.x <= enemy_fireing:
				enemy_bullet_group = pygame.sprite.Group()
				enemy_bullet = Bullet(pos_x=enemy.rect.x + TILE // 2, pos_y=enemy.rect.y + TILE // 2)
				enemy_bullet_group.add(enemy_bullet)

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

	# if enemy bullet hit player
	if pygame.sprite.groupcollide(enemy_bullet_group, player_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		exit()

	# if players bullet hit flag
	if pygame.sprite.groupcollide(bullet_group, flag_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		exit()

	# if enemy bullet hit flag
	if pygame.sprite.groupcollide(enemy_bullet_group, flag_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		exit()

	# if players bullet hit brickwall
	if pygame.sprite.groupcollide(bullet_group, brickwall_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		bullet_counter = 0

	# if enemy bullet hit brickwall
	if pygame.sprite.groupcollide(enemy_bullet_group, brickwall_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		bullet_counter = 0

	# if player hit enemy
	if pygame.sprite.groupcollide(player_group, enemy_group, False, False, pygame.sprite.collide_rect_ratio(.85)):
		enemy_direction = random.randint(0, 3)
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)

	# if enemy hit flag
	if pygame.sprite.groupcollide(enemy_group, flag_group, False, False, pygame.sprite.collide_rect_ratio(.85)):
		enemy_direction = random.randint(0, 3)
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)

	# if enemy bullet hit player bullet
	if pygame.sprite.groupcollide(enemy_bullet_group, bullet_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		pass

	# drawing sprites on the screen
	SCREEN.fill(BLACK)

	bullet_group.update()
	bullet_group.draw(SCREEN)

	player_group.update()
	player_group.draw(SCREEN)

	enemy_bullet_group.update()
	enemy_bullet_group.draw(SCREEN)

	enemy_group.update()
	enemy_group.draw(SCREEN)

	brickwall_group.update()
	brickwall_group.draw(SCREEN)

	flag_group.update()
	flag_group.draw(SCREEN)

	# for l1 in range(0, SCREEN_WIDTH, TILE):
	# 	pygame.draw.line(SCREEN, GREEN, (0, l1), (SCREEN_WIDTH, l1))
	# 	for l2 in range(0, SCREEN_WIDTH, TILE):
	# 		pygame.draw.line(SCREEN, GREEN, (l2, 0), (l2, SCREEN_HEIGHT))

	# fps counter
	pygame.display.flip()
	pygame.time.Clock().tick(FPS)