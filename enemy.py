import pygame
import graphics
import math
BLACK = (0, 0, 0)
	
class enemy():

		
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.frame = 1
		self.speed = 3.5
		self.vel = 0
		self.spritesheet = graphics.load("sprite.png")
		self.right = False
		self.left = False
		self.jump = False
		self.punch = False
		self.health = 100
		self.load_images()
		self.image = self.frames_l[0]
		self.death = False
		self.deathEffect = True
		self.hit = False
		
	def get_image(self, x, y, width, height):
		# grab an image out of a larger spritesheet
		image = pygame.Surface((width, height))
		image.blit(self.spritesheet, (0, 0), (x, y, width, height))
		return image
		
	def load_images(self):
		self.frames_r = [self.get_image(48, 0, 48, 45),
							self.get_image(0, 0, 48, 45),
							self.get_image(96, 0, 48, 45)]
		for frame in self.frames_r:
				frame.set_colorkey(BLACK)
				
		self.frames_l = [self.get_image(376, 0, 48, 45),
							self.get_image(314, 0, 48, 45),
							self.get_image(423, 0, 48, 45)]
		for frame in self.frames_l:
				frame.set_colorkey(BLACK)
				
		self.frames_death_l = [self.get_image(320, 96, 48, 45),
							self.get_image(368, 96, 54, 45)]
		for frame in self.frames_death_l:
				frame.set_colorkey(BLACK)
				
		self.frames_death_r = [self.get_image(96, 96, 48, 45),
							self.get_image(40, 96, 54, 45)]
		for frame in self.frames_death_r:
				frame.set_colorkey(BLACK)
		self.frames_hit_r = [self.get_image(142, 96, 48, 45)]
		for frame in self.frames_hit_r:
				frame.set_colorkey(BLACK)
		self.frames_hit_l = [self.get_image(280, 96, 48, 45)]
		for frame in self.frames_hit_l:
				frame.set_colorkey(BLACK)
		
	def update(self, player):
		
		if self.health <= 0:
			self.speed = 0
			self.health = 0
			if self.deathEffect:
				self.frame = 0
				self.deathEffect = False
				player.score +=1
			if self.left:
				self.image = self.frames_death_l[int(self.frame)]
			if self.right:
				self.image = self.frames_death_r[int(self.frame)]
			if not self.death:
				self.frame += .25
			if self.frame == 2:
				self.death = True

		else:
			
			
			if self.health > 75:
				self.health_color = pygame.Color(0, 255, 0, 255)
			elif self.health > 50:
				self.health_color = pygame.Color(0, 255, 255, 255)
			else:
				self.health_color = pygame.Color(255, 0, 0, 255)
				
			if player.x >= self.x:
				self.right = True
				self.left = False
				if abs(player.x-self.x) >= 30:	
					self.x += self.speed
					self.frame += .25
					if self.frame == 3:
						self.frame = 0
				else:
					self.frame = 0
				self.image = self.frames_r[int(self.frame)]
					
			
			elif player.x <= self.x:
				self.right = False
				self.left = True
				if abs(player.x-self.x) >= 30:
					self.x -= self.speed
					self.frame += .25
					if self.frame == 3:
						self.frame = 0
				else:
					self.frame = 0
				self.image = self.frames_l[int(self.frame)]
			

			
			

		
		
	def render(self, surface):
		if self.death:
			surface.blit(self.image, (self.x, self.y+20, 48,48))
		elif self.hit:
			self.frame = 0
			if self.right:
				self.image = self.frames_hit_r[int(self.frame)]
			if self.left:
				self.image = self.frames_hit_l[int(self.frame)]
			surface.blit(self.image, (self.x, self.y, 48,48))
			self.hit = False
		elif not self.death:
			surface.blit(self.image, (self.x, self.y, 48,48))
		

				
