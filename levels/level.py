import pygame
from tile import *
from constants import *

class Level:
	def __init__(self, path, tileManager):
		self.tileManager = tileManager
		self.map = self.getTileMap(path)

	def getTileMap (self, path):
		img = pygame.image.load("levels/level1.png")
		size = img.get_rect().size
		self.width = size[0]
		self.height = size[1]
		pixel = pygame.PixelArray(img)
		temp = []
		for x in range(0,len(pixel)):
			for y in range(0,len(pixel[x])):
				tile = self.tileManager.getTile(pixel[x][y])
				if (tile != None):
					temp.append(tile)
				else:
					temp.append(None)
		return temp

	def drawlevel(self, screen, x, y):
		for x in range(0,self.width):
			for y in range(0,self.height):
				tile = self.map[x+y*self.width]
				if (tile == None):
					screen.drawSprite( 0, 1, x*16*5, y*16*5)
				else:
					screen.drawSprite( 0, 10, x*16*5, y*16*5)
		
