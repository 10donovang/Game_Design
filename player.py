import pygame
import graphics



	
class Player:
		
	def __init__(self, x, y):
		self.x=x
		self.y=y
		self.frame = -2
		self.spritesheet = graphics.load("sprite.png")
		self.mapping = {
			"left" : [(47 * (7+i), 0, 48 ,45) for i in range(4)],
			"right" : [(48 * i, 0, 48 ,45) for i in range(4)],
			"punching right": [(48* (2+i), 46, 48, 45) for i in range(2)],
			"punching left": [(48* (7-i), 46, 48, 45) for i in range(2)],
		}
		self.speed = 0
		self.facing = "right"
		self.sheet = False
		self.jump = False
		self.yVel = 0
		self.jumpLeft = False
		self.jumpRight = False

	def update(self):
			if self.sheet == False:
				self.frame = (self.frame + self.speed) % 3
			elif self.sheet == True:
				self.frame = (self.frame - self.speed) % 3
			if self.frame == 2.75:
				self.sheet = True
				self.frame = 2 
			elif self.frame == 0:
				self.sheet = False
				self.frame = 0.75 
			if self.jump:
				self.y -= self.yVel
				self.yVel -=10
				if self.y <=0:
					self.y = 0
				if self.y >= 400:
					self.jump = False
					self.y = 400
			print(self.frame)
				

			
			
	def render(self, surface):
			surface.blit(self.spritesheet,
			             (self.x, self.y, 48,48),
			             self.mapping[self.facing][int(self.frame)])
			
	def handler(self, event):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.facing = "left"
			self.speed = .25
			self.x -= 2
			if self.x < 0:
				self.x = 0
			self.jumpLeft = True
			self.jumpRight = False
			
		elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
			self.facing = "left"
			self.speed = .25
			self.x -= 2
			if self.x < 0:
				self.x = 0
			self.jumpLeft = True
			self.jumpRight = False
			if self.jump == False:
				self.jump = True
				self.yVel = 50
		
		if event.type == pygame.KEYDOWN:
#			if event.key == pygame.K_LEFT:
#				self.facing = "left"
#				self.speed = .25
#				self.x -= 2
#				if self.x < 0:
#					self.x = 0
#				self.jumpLeft = True
#				self.jumpRight = False
			if event.key == pygame.K_RIGHT:
				self.facing = "right"
				self.speed = .25
				self.x += 2
				if self.x > (799 - 48):
					self.x = 799 - 48
				self.jumpLeft = False
				self.jumpRight = True
			if not event.key == pygame.K_RIGHT:
				self.jumpRight = False
			if not event.key == pygame.K_LEFT:
				self.jumpLeft = False
			if event.key == pygame.K_m:
				if self.facing == "left":
					self.facing = "punching left"
					self.frame = .5
				if self.facing == "right":
					self.facing = "punching right"
					self.frame = .5

			if event.key == pygame.K_SPACE:
				if self.jump == False:
					self.jump = True
					self.yVel = 50
				if self.jump == True:
					if self.jumpLeft == True:
						self.facing = "left"
						self.speed = .25
						self.x -= 2
						if self.x < 0:
							self.x = 0
					if self.jumpRight == True:
						self.facing = "right"
						self.speed = .25
						self.x += 2
						if self.x > (799 - 48):
							self.x = 799 - 48

			

	
					
		if event.type == pygame.KEYUP:
			self.speed = 0
			self.frame = -2
