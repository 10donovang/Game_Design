import pygame

def init():
	pygame.mixer.init()
	pygame.mixer.music.load('The Last Encounter (90s RPG Version) Full Loop.wav')
	pygame.mixer.music.play(-1)
