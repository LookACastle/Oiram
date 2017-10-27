import pygame
import re

class SpriteSheet:
	def __init__(self, path):
		self.sheet = pygame.image.load(path)
		size = self.sheet.get_rect().size
		self.width = size[0]
		self.height = size[1]
		regex = re.findall("((?<=\_)[0-9][0-9])", path)
		self.spritewidth = int(regex[0])
		self.spriteheight = int(regex[1])
		self.rowcount = int(self.width/self.spritewidth)

	def getSprite(self, index):
		print(index,self.rowcount)
		y = int(index/self.rowcount)
		x = index-y*self.rowcount
		print(x,y,x*self.spritewidth, y*self.spriteheight*self.width)