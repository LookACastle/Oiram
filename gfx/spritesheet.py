import pygame
import re
from constants import *

class SpriteSheet:
	def __init__(self, path):
		self.sheet = pygame.image.load("Sprites/"+path)
		size = self.sheet.get_rect().size

		self.width = size[0]
		self.height = size[1]

		regex = re.findall("((?<=\_)[0-9][0-9])", path)

		self.spritewidth = int(regex[0])
		self.spriteheight = int(regex[1])
		self.rowcount = int(self.width/self.spritewidth)

		self.sprite = pygame.Surface((self.spritewidth, self.spriteheight)).convert_alpha()

		self.scaleWidth = self.spritewidth*SCALE
		self.scaleHeight = self.spriteheight*SCALE

		self.output = pygame.Surface((self.scaleWidth, self.scaleHeight)).convert_alpha()
		self.scaledoutput = pygame.Surface(((int(self.spriteheight/2)*SCALE), int((self.spritewidth/2)*SCALE))).convert_alpha()

	def getSprite(self, index):
		y = int(index/self.rowcount)
		x = index-y*self.rowcount

		#print(x,y,x*self.spritewidth, y*self.spriteheight*self.width)
		self.sprite.fill((0,0,0,0))
		self.sprite.blit(self.sheet, (0,0), (x*self.spritewidth, y*self.spriteheight, self.spritewidth, self.spriteheight))
		pygame.transform.scale(self.sprite, (self.scaleWidth, self.scaleHeight), self.output)
		return self.output

	def getScaledSprite(self, index):
		y = int(index/self.rowcount)
		x = index-y*self.rowcount

		#print(x,y,x*self.spritewidth, y*self.spriteheight*self.width)
		self.sprite.fill((0,0,0,0))
		self.sprite.blit(self.sheet, (0,0), (x*self.spritewidth, y*self.spriteheight, self.spritewidth, self.spriteheight))
		pygame.transform.scale(self.sprite, (int((self.spritewidth/2)*SCALE), int((self.spriteheight/2)*SCALE)), self.scaledoutput)
		return self.scaledoutput