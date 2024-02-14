# importing modules
import sys

# importing sub-modules
from settings import *

# game classes
# class player
class Player(pygame.sprite.Sprite):
	def __init__(self, img="static/hero.png", pos_x=5, pos_y=13):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x * 50 - 25, pos_y * 50 - 25])

	# update method
	def update(self):
		# restricting player go out the world boundaries
		if self.rect.x >= SCREEN_WIDTH - PLAYER_SIZE:
			self.rect.x = SCREEN_WIDTH - PLAYER_SIZE
		if self.rect.y >= SCREEN_HEIGHT - PLAYER_SIZE:
			self.rect.y = SCREEN_HEIGHT - PLAYER_SIZE
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.y <= 0:
			self.rect.y = 0

# class bullet
class Bullet(pygame.sprite.Sprite):
	def __init__(self, img="static/bullet.png", pos_x=25, pos_y=25):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	# update method
	def update(self):
		# updating bullet movement
		if bullet_direction == 0:
			self.rect.y -= BULLET_SPEED
		if bullet_direction == 2:
			self.rect.y += BULLET_SPEED
		if bullet_direction == 3:
			self.rect.x -= BULLET_SPEED
		if bullet_direction == 1:
			self.rect.x += BULLET_SPEED

# class enemy
class Enemy(pygame.sprite.Sprite):
	def __init__(self, img="static/enemy.png", pos_x=enemy_spawn[0], pos_y=25):
		super().__init__()
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x - 25, pos_y - 25])

	# update method
	def update(self):
		# restricting enemy go out the world boundaries
		if self.rect.x >= SCREEN_WIDTH - PLAYER_SIZE:
			self.rect.x = SCREEN_WIDTH - PLAYER_SIZE
		if self.rect.y >= SCREEN_HEIGHT - PLAYER_SIZE:
			self.rect.y = SCREEN_HEIGHT - PLAYER_SIZE
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.y <= 0:
			self.rect.y = 0

# class block
class Block(pygame.sprite.Sprite):
	def __init__(self, img="static/brick.png", pos_x=6, pos_y=13):
		super().__init__()
		self.img = img
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x * 50 - 25, pos_y * 50 - 25])

	# update method
	def update(self):
		pass

# game functions
# exit game function
def exit():
	pygame.quit()
	sys.exit()
	running = False

# start game menu
def game_menu():
	pass

# pause game function
def game_pause():
	pass

# initializing modules
pygame.init()
pygame.mixer.init()
pygame.font.init()

# creating instance of classes
# player instance of the class
player_group = pygame.sprite.Group()
player = Player(img="static/hero.png")
player_group.add(player)

# creating groups only
flag_group = pygame.sprite.Group()
upgrade_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()

# level creator primitive
# x axes
# for item in board[3:-3:]:
# 	# y axes
# 	for index, value in item[3:-3:]:
# 		block = Block(pos_x=index, pos_y=value, img=random.choice(basic_tile_set))
# 		block_group.add(block)

# level creation from world list
for row_index, row in enumerate(world, start=1):
	for col_index, tile in enumerate(row, start=1):
		if tile == 1:
			block = Block(pos_x=(col_index), pos_y=(row_index), img=basic_tile_set[0])
			block_group.add(block)

		elif tile == 2:
			block = Block(pos_x=(col_index), pos_y=(row_index), img=basic_tile_set[1])
			block_group.add(block)

		elif tile == 3:
			block = Block(pos_x=(col_index), pos_y=(row_index), img=basic_tile_set[2])
			block_group.add(block)

		elif tile == 4:
			block = Block(pos_x=(col_index), pos_y=(row_index), img=basic_tile_set[3])
			block_group.add(block)

		elif tile == 5:
			block = Block(pos_x=(col_index), pos_y=(row_index), img=basic_tile_set[4])
			block_group.add(block)

		elif tile == 9:
			flag = Block(pos_x=(col_index), pos_y=(row_index), img="static/flag.png")
			flag_group.add(flag)
		else:
			pass

# bullet instance of the class
bullet_group = pygame.sprite.Group()
bullet = Bullet(pos_x=player.rect.x, pos_y=player.rect.y)

# enemy instance of the class
enemy_group = pygame.sprite.Group()
enemy = Enemy(img="static/enemy.png")
enemy.image = pygame.transform.rotate(enemy.image, 180)
enemy_group.add(enemy)

# enemy bullet instance of the class
enemy_bullet_group = pygame.sprite.Group()
enemy_bullet = Bullet(pos_x=enemy.rect.x, pos_y=enemy.rect.y)

# main game loop
while running:

	# engine of the explosion animation
	frame += 1
	if frame >= len(explosion):
		frame = 0

	# checking for key input
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# if enemy collide with walls add new direction
	if enemy.rect.x == SCREEN_WIDTH - TILE:
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)
		enemy_direction = random.randint(0, 3)

	elif enemy.rect.x == SCREEN_WIDTH + TILE:
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)
		enemy_direction = random.randint(0, 3)

	elif enemy.rect.y == SCREEN_WIDTH - TILE:
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)
		enemy_direction = random.randint(0, 3)

	elif enemy.rect.y == SCREEN_WIDTH + TILE:
		enemy_moving_range = random.randint(0, SCREEN_WIDTH)
		enemy_direction = random.randint(0, 3)

	# fiering bullet triggering mechanism
	# fireing players bullet
	if keys[pygame.K_SPACE] and bullet_counter != 1:
		bullet_counter += 1

		# creating bullet instance of the classes
		bullet_group = pygame.sprite.Group()
		bullet = Bullet(pos_x=player.rect.x + TILE // 2, pos_y=player.rect.y + TILE // 2)
		bullet_group.add(bullet)

	# player movement mechanism
	# for key w
	if keys[pygame.K_w]:
		direction = 0
		player.rect.y -= PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image.set_colorkey(ALPHA)

	# for key a
	elif keys[pygame.K_a]:
		direction = 3
		player.rect.x -= PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 90)
		player.image.set_colorkey(ALPHA)

	# for key s
	elif keys[pygame.K_s]:
		direction = 2
		player.rect.y += PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 180)
		player.image.set_colorkey(ALPHA)

	# for key d
	elif keys[pygame.K_d]:
		direction = 1
		player.rect.x += PLAYER_SPEED

		# drawing proper player and bullet image for moving direction
		player.image = pygame.image.load("static/hero.png").convert()
		player.image = pygame.transform.rotate(player.image, 270)
		player.image.set_colorkey(ALPHA)

	# bullet constant direction mechanism
	# without this mechanic bullet do not going linear
	if bullet_counter == 0:
		if direction == 0 and bullet.rect.y >= 0:
			bullet_direction = 0

		if direction == 1 and bullet.rect.y <= SCREEN_WIDTH:
			bullet_direction = 1

		if direction == 2 and bullet.rect.x <= SCREEN_HEIGHT:
			bullet_direction = 2

		if direction == 3 and bullet.rect.x >= 0:
			bullet_direction = 3

	# end game condition
	if player_lives < 0:
		exit()

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
	# player bullet
	# proper image of the bullet for the right movement
	if bullet_direction == 0:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image.set_colorkey(ALPHA)

	if bullet_direction == 3:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 90)
		bullet.image.set_colorkey(ALPHA)

	if bullet_direction == 2:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 180)
		bullet.image.set_colorkey(ALPHA)

	if bullet_direction == 1:
		bullet.image = pygame.image.load("static/bullet.png").convert()
		bullet.image = pygame.transform.rotate(bullet.image, 270)
		bullet.image.set_colorkey(ALPHA)

	# enemy moving direction
	# proper image of the enemy for the right movement
	if enemy_direction == 0:
		enemy.rect.y -= ENEMY_SPEED

		enemy.image = pygame.image.load("static/enemy.png").convert()
		enemy.image.set_colorkey(ALPHA)

		enemy_bullet.image = pygame.image.load("static/bullet.png").convert()
		enemy_bullet.image.set_colorkey(ALPHA)

		if enemy.rect.y <= enemy_moving_range:
			enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			enemy_direction = random.randint(0, 3)

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

	# spawning upgrade logic 
	if enemy_id == 15 and upgrade_counter == 0 or enemy_id == 10 and upgrade_counter == 1 or enemy_id == 5 and upgrade_counter == 2:
		upgrade = Block(pos_x=random.randint(1, 13), pos_y=random.randint(1, 13), img=random.choice(upgrade_list))
		upgrade_group.add(upgrade)

		upgrade_counter += 1

	# statement needed for changing enemy spawn point
	if enemy_spawn_switch >= 2:
		enemy_spawn_switch = -1

	# collision section
	# player collision section
	# if player hit enemy
	if pygame.sprite.groupcollide(player_group, enemy_group, False, False, pygame.sprite.collide_rect_ratio(.85)):
		pass

	# if player hit block
	if pygame.sprite.groupcollide(player_group, block_group, False, False, pygame.sprite.collide_rect_ratio(.85)):
		for item in block_group:
			pass

	# if player hit upgrade
	if pygame.sprite.groupcollide(player_group, upgrade_group, False, True, pygame.sprite.collide_rect_ratio(.85)):
		# and if upgrade is live add live
		if upgrade.img == "static/1up.png":
			player_lives += 1

		# and if upgrade is speed add speed
		if upgrade.img == "static/speed.png":
			PLAYER_SPEED += 1

		# and if upgrade is speed add speed
		if upgrade.img == "static/bulletsp.png":
			BULLET_SPEED += 1

	# restricting player upgrades
	# player lives
	if player_lives >= 10:
		player_lives = 10

	# player speed
	if PLAYER_SPEED >= 5:
		PLAYER_SPEED = 5

	# player bullet speed
	if BULLET_SPEED >= 12:
		BULLET_SPEED = 12

	# player bullet collision section
	# if players bullet hit enemy
	if pygame.sprite.groupcollide(bullet_group, enemy_group, True, False, pygame.sprite.collide_rect_ratio(.85)):
		enemy_health -= 1
		bullet_counter = 0

		# if enemy health is smaller or equal to zero destroy enemy 
		if enemy_health <= 0:
			pygame.sprite.groupcollide(bullet_group, enemy_group, True, True, pygame.sprite.collide_rect_ratio(.85))
			
			enemy_id -= 1
			enemy_health = 3

			if enemy_id >= 1:
				enemy_group = pygame.sprite.Group()
				enemy_spawn_switch += 1

				# enemy spawn point changing when new enemy got spawned
				enemy = Enemy(img="static/enemy.png", pos_x=enemy_spawn[enemy_spawn_switch])
				enemy.image = pygame.transform.rotate(enemy.image, 180)
				enemy_group.add(enemy)

				enemy_direction = random.randint(0, 3)
				enemy_moving_range = random.randint(0, SCREEN_WIDTH)
			else:
				enemy.kill()

	# if players bullet hit flag
	if pygame.sprite.groupcollide(bullet_group, flag_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		exit()

	# if players bullet hit block
	if pygame.sprite.groupcollide(bullet_group, block_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		bullet_counter = 0

	# if enemy bullet hit player
	if pygame.sprite.groupcollide(enemy_bullet_group, player_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		player_lives -= 1

		player_group = pygame.sprite.Group()
		player = Player(img="static/hero.png")
		player_group.add(player)

	# enemy collision section
	# if enemy hit flag
	if pygame.sprite.groupcollide(enemy_group, flag_group, False, False, pygame.sprite.collide_rect_ratio(1)):
		pass

	# if enemy hit block
	if pygame.sprite.groupcollide(enemy_group, block_group, False, False, pygame.sprite.collide_rect_ratio(.85)):
		pass

	# enemy bullet collision section
	# if enemy bullet hit flag
	if pygame.sprite.groupcollide(enemy_bullet_group, flag_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		exit()

	# if enemy bullet hit block
	if pygame.sprite.groupcollide(enemy_bullet_group, block_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		bullet_counter = 0

	# if enemy bullet hit player bullet
	if pygame.sprite.groupcollide(enemy_bullet_group, bullet_group, True, True, pygame.sprite.collide_rect_ratio(.85)):
		pass

	# drawing sprites on the screen
	# filling complete screen with color
	SCREEN.fill(BLACK)

	# drawing explosion animation on the screen
	# SCREEN.blit(explosion[frame], (0, 0))

	# drawing groups on the screen
	bullet_group.update()
	bullet_group.draw(SCREEN)

	enemy_bullet_group.update()
	enemy_bullet_group.draw(SCREEN)

	enemy_group.update()
	enemy_group.draw(SCREEN)

	player_group.update()
	player_group.draw(SCREEN)

	block_group.update()
	block_group.draw(SCREEN)

	flag_group.update()
	flag_group.draw(SCREEN)

	upgrade_group.update()
	upgrade_group.draw(SCREEN)

	# drawing grid
	# for l1 in range(0, SCREEN_WIDTH, TILE):
	# 	pygame.draw.line(SCREEN, GREEN, (0, l1), (SCREEN_WIDTH, l1), LINE_THICKNESS)
	# 	for l2 in range(0, SCREEN_HEIGHT, TILE):
	# 		pygame.draw.line(SCREEN, GREEN, (l2, 0), (l2, SCREEN_HEIGHT), LINE_THICKNESS)

	# updating the screen
	pygame.display.flip()
	# FPS counter
	pygame.time.Clock().tick(FPS)