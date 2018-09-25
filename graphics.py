import pygame


width = 800
height = 600

assets = {}

renderables = []

background = None

textsurface = None

enemytextsurface = None

score = None

screen = None

myfont = None


def update(player, enemy):
	global screen, background, renderables, width, height
	
	scoreDisplay = "Score: " + str(player.score)
	score = myfont.render(scoreDisplay, False, (0, 0, 0))
	playertextsurface = myfont.render('Player One', False, (0, 0, 0))
	
	screen.fill((0,0,0))
	
	if background:
		screen.blit(background, (0, 0, width, height))	
		
	screen.blit(textsurface,(50,20))
	
	screen.blit(enemytextsurface,(650,20))
	
	screen.blit(score,(400,20))
	
	pygame.draw.rect(screen, player.health_color, (50, 10, player.health, 10))
	
	pygame.draw.rect(screen, enemy.health_color, (650, 10, enemy.health, 10))
	
	for r in renderables:
		r.render(screen)

	pygame.display.flip()				

def register(renderable):
	global renderables
	if renderable not in renderables:
		renderables.append(renderable)

def remove(renderable):
	global renderables
	if renderable in renderables:
		renderables.remove(renderable)

		
def init():
	global screen
	pygame.display.init()
	screen = pygame.display.set_mode((width, height))
	
	

	
def load(file):
	global assets
	if file in assets:
		return assets[file]
	else:
		image = pygame.image.load(file)
		assets[file] = image
		return image
		