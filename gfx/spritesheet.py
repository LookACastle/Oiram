import pygame
import re
from constants import *

class SpriteSheet:
	def __init__(self, path):
		sheet = pygame.image.load("Sprites/"+path)
		size = sheet.get_rect().size

		self.width = size[0]
		self.height = size[1]

		regex = re.findall("((?<=\_)[0-9][0-9])", path)

		self.spritewidth = int(regex[0])
		self.spriteheight = int(regex[1])

		self.sprites = []

		self.scaleWidth = self.spritewidth*SCALE
		self.scaleHeight = self.spriteheight*SCALE
		
		for y in range(0,self.height,self.spriteheight):
			for x in range(0,self.width,self.spritewidth):
				sheetSection = pygame.Surface((self.spritewidth, self.spriteheight)).convert_alpha()
				sheetSection.fill((0,0,0,0))
				sheetSection.blit(sheet, (0,0), (x, y, self.spritewidth, self.spriteheight))
				self.sprites.append(sheetSection)

		self.output = pygame.Surface((self.scaleWidth, self.scaleHeight)).convert_alpha()
		self.scaledoutput = pygame.Surface(((int(self.spritewidth/2)*SCALE), int((self.spriteheight/2)*SCALE))).convert_alpha()

	def getSprite(self, index):
		pygame.transform.scale(self.sprites[index], (self.scaleWidth, self.scaleHeight), self.output)
		return self.output

	def getScaledSprite(self, index):
		pygame.transform.scale(self.sprites[index], (((int(self.spritewidth/2)*SCALE), int((self.spriteheight/2)*SCALE))), self.scaledoutput)
		return self.scaledoutput