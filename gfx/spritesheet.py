import pygame
import re
from constants import *

class SpriteSheet:
	def __init__(self, path):
		sheet = pygame.image.load("Sprites/"+path).convert_alpha()
		size = sheet.get_rect().size

		self.width = size[0]
		self.height = size[1]

		regex = re.findall("((?<=\_)[0-9][0-9])", path)

		self.spritewidth = int(regex[0])
		self.spriteheight = int(regex[1])

		self.scalewidth = self.spritewidth*SCALE
		self.scaleheight = self.spriteheight*SCALE

		self.spritesheet = pygame.transform.scale(sheet, (self.width*SCALE, self.height*SCALE))

		self.sprites = []
		for y in range(0,self.height,self.spriteheight):
			for x in range(0,self.width,self.spritewidth):
				self.sprites.append(self.spritesheet.subsurface((x*SCALE, y*SCALE, self.scalewidth, self.scaleheight)))

	def getSprite(self, index):
		return self.sprites[index]

	def getScaledSprite(self, index):
		return pygame.transform.scale(self.sprites[index], ((int(self.scalewidth/2), int(self.scaleheight/2))))