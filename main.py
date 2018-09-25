import pygame, sys
import graphics
from player2 import *
import music
import mask
graphics.init()
music.init()
import event
from enemy import *



pygame.display.set_caption("First Game")

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.


graphics.background = graphics.load('bg.png')

myfont = pygame.font.SysFont('Times New Roman', 20)
graphics.myfont = myfont
playertextsurface = graphics.myfont.render('Player One', False, (0, 0, 0))
enemytextsurface = graphics.myfont.render('Unit 1', False, (0, 0, 0))


graphics.textsurface = playertextsurface
graphics.enemytextsurface = enemytextsurface

player = Player(50,400)
unit1 = enemy(750,400)


graphics.register(player)
graphics.register(unit1)


def quit(e):
	global run
	if e.type == pygame.QUIT:
		run = False
	elif e.type == pygame.KEYUP:
		if ((e.key == pygame.K_F4) and
		   (e.mod and pygame.KMOD_ALT)):
			run = False

#mainloop
event.register(player.handler)
event.register(quit)

clock = pygame.time.Clock()
run = True
frame = 0


mask.init(player, unit1)

while run:

	clock.tick(60)


	
	event.update()
	if not player.death:	
		player.update(unit1)
	if not unit1.death:
		unit1.update(player)
	graphics.update(player, unit1)
	mask.update(player, unit1)
	
	

pygame.quit()