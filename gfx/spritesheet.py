import pygame
import re
from constants import *

class SpriteSheet:
	def __init__(self, path, scale):
		self.sheet = pygame.image.load("Sprites/"+path).convert_alpha()
		size = self.sheet.get_rect().size

		self.width = size[0]
		self.height = size[1]

		parsing = path.replace(".png", "").split("_")

		self.spritewidth = int(parsing[1])
		self.spriteheight = int(parsing[2])

		self.scalewidth = self.spritewidth*scale
		self.scaleheight = self.spriteheight*scale

		self.spritesheet = pygame.transform.scale(self.sheet, (self.width*scale, self.height*scale))

		self.sprites = []
		for y in range(0,self.height,self.spriteheight):
			for x in range(0,self.width,self.spritewidth):
				self.sprites.append(self.spritesheet.subsurface((x*scale, y*scale, self.scalewidth, self.scaleheight)))
	
	def getSprite(self, index):
		return self.sprites[index]

	def getScaledSprite(self, index, scale):
		return pygame.transform.scale(self.sprites[index], ((int(self.scalewidth/scale), int(self.scaleheight/scale))))

	def scale(self, newscale):
		self.spritesheet = pygame.transform.scale(self.sheet, (self.width*newscale, self.height*newscale))
		self.scalewidth = self.spritewidth*newscale
		self.scaleheight = self.spriteheight*newscale
		self.sprites = []
		for y in range(0,self.height,self.spriteheight):
			for x in range(0,self.width,self.spritewidth):
				self.sprites.append(self.spritesheet.subsurface((x*newscale, y*newscale, self.scalewidth, self.scaleheight)))
			