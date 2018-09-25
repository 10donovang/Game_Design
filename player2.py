import pygame
import graphics
BLACK = (0, 0, 0)


	
class Player:
		
	def __init__(self, x, y):
		self.x=x
		self.y=y
		self.frame = 1
		self.speed = 5
		self.vel = 0
		self.spritesheet = graphics.load("sprite.png")
		self.right = False
		self.left = False
		self.jump = False
		self.punch = False
		self.health = 100
		self.health_color = pygame.Color(0, 255, 0, 255)
		self.score = 0
		self.load_images()
		self.image = self.frames_r[0]
		self.attack_r = False
		self.attack_l = False
		self.death = False
		self.kick = False
		self.kickEffect = True
		self.punchEffect =True
		
		
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
							self.get_image(329, 0, 48, 45),
							self.get_image(423, 0, 48, 45)]
		for frame in self.frames_l:
				frame.set_colorkey(BLACK)
				
		self.frames_punch_r = [self.get_image(48, 0, 48, 45),
							self.get_image(92, 48, 48, 45),
							self.get_image(138, 48, 48, 45)]
		for frame in self.frames_punch_r:
				frame.set_colorkey(BLACK)
				
		self.frames_punch_l = [self.get_image(376, 0, 48, 45),
							self.get_image(329, 48, 48, 45),
							self.get_image(283, 48, 48, 45)]
		for frame in self.frames_punch_l:
				frame.set_colorkey(BLACK)
				
		self.frames_kick_r = [self.get_image(48, 0, 48, 45),
							self.get_image(180, 96, 48, 45),
							self.get_image(48, 0, 48, 45)]
		for frame in self.frames_kick_r:
				frame.set_colorkey(BLACK)
				
		self.frames_kick_l = [self.get_image(376, 0, 48, 45),
							self.get_image(230, 96, 48, 45),
							self.get_image(376, 0, 48, 45)]
		for frame in self.frames_kick_l:
				frame.set_colorkey(BLACK)
		
		self.frames_death_l = [self.get_image(320, 96, 48, 45),
							self.get_image(368, 96, 54, 45)]
		for frame in self.frames_death_l:
				frame.set_colorkey(BLACK)
				
		self.frames_death_r = [self.get_image(96, 96, 48, 45),
							self.get_image(48, 96, 54, 45)]
		for frame in self.frames_death_r:
				frame.set_colorkey(BLACK)


		
	def update(self,enemy):
			
		if self.health <= 0:
			self.speed = 0
			self.health = 0
			if self.deathEffect:
				self.frame = 0
				self.deathEffect = False
			if self.left:
				self.image= self.frames_death_l[int(self.frame)]
			if self.right:
				self.image= self.frames_death_r[int(self.frame)]
			if not self.death:
				self.frame += .25
			if self.frame == 2:
				self.death = True
				
		
		elif self.kick == True:
			if self.kickEffect:
				self.frame = 0
				self.kickEffect = False
			if self.attack_r:
				self.frame += .25
				if self.frame == 2:
					self.frame = 0
					self.kick = False
				self.image = self.frames_kick_r[int(self.frame)]				
			if self.attack_l:
				self.frame += .25
				if self.frame == 2:
					self.frame = 0
					self.kick = False
					self.kickEffect = True
				self.image= self.frames_kick_l[int(self.frame)]
			
			
		elif self.punch == True:
			if self.punchEffect:
				self.frame = 0
				self.punchEffect = False
			if self.attack_r:
				self.frame += .25
				if self.frame == 3:
					self.frame = 0
					self.punch = False
				self.image = self.frames_punch_r[int(self.frame)]				
			if self.attack_l:
				self.frame += .25
				if self.frame == 3:
					self.frame = 0
					self.punch = False
					self.punchEffect = True
				self.image= self.frames_punch_l[int(self.frame)]

		
		else:
			if self.health > 75:
				self.health_color = pygame.Color(0, 255, 0, 255)
			elif self.health > 50:
				self.health_color = pygame.Color(0, 255, 255, 255)
			else:
				self.health_color = pygame.Color(255, 0, 0, 255)
				
		
			if self.right:
				if enemy.x-self.x >= 30 or self.y < 400:
					self.x+=self.speed
					self.frame += .25
					if self.frame == 3:
						self.frame = 0
					self.image = self.frames_r[int(self.frame)]
				
				elif enemy.x < self.x and enemy.x-self.x <= 30:
					self.x+=self.speed
					self.frame += .25
					if self.frame == 3:
						self.frame = 0
					self.image = self.frames_r[int(self.frame)]
			
			if self.left:
				if self.x-enemy.x >= 30 or self.y < 400:
					self.x-=self.speed
					self.frame += .25
					if self.frame == 3:
						self.frame = 0
					self.image = self.frames_l[int(self.frame)]
				
				elif enemy.x > self.x and self.x-enemy.x <= 30:
					self.x-=self.speed
					self.frame += .25
					if self.frame == 3:
						self.frame = 0
					self.image = self.frames_l[int(self.frame)]
					
			if self.jump:
				self.y -= self.vel
				self.vel-=1
			if self.vel == 0:
				self.jump = False
			if self.jump == False and self.y < 400:
				if self.vel == 0:
					self.vel = 13
				else:
					self.y+=self.vel
					self.vel-=1
			if self.y > 400:
				self.y=400
				
		
		
	def render(self, surface):
				surface.blit(self.image, (self.x, self.y, 48,48))
				
				
	def handler(self, event):
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				self.left = True
				self.attack_r = False
				self.attack_l = True
			if keys[pygame.K_RIGHT]:
				self.right = True
				self.attack_r = True
				self.attack_l = False
			if not keys[pygame.K_LEFT]:
				self.left = False
			if not keys[pygame.K_RIGHT]:
				self.right = False
			if keys[pygame.K_SPACE] and self.y == 400:
				self.jump = True
				self.vel = 12
			if keys[pygame.K_a]:
				self.punch = True
			if keys[pygame.K_s]:
				self.kick = True
			if event.type == pygame.KEYUP:
				if not self.punch == True:
					self.frame = 0
					if self.attack_r:
						self.image = self.frames_r[int(self.frame)]
					if self.attack_l:
						self.image = self.frames_l[int(self.frame)]
				
