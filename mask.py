import pygame


def init(player, enemy):
	global unit1_mask, player_mask
	unit1_mask = pygame.mask.from_surface(enemy.image)
	player_mask = pygame.mask.from_surface(player.image)
	
def update(player, enemy):
	offset = (int(player.x - enemy.x), int(player.y - enemy.y))
	result = player_mask.overlap(unit1_mask, offset)
	if offset[0] >= -30 and offset[0] <= 30 and (player.punch == True or player.kick == True):
		enemy.health -= 1
		enemy.hit =  True
