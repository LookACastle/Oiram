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
		for y in range(0,self.height):
			for x in range(0,self.width):
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
					screen.drawSprite( 1, 0, x*16*SCALE, y*16*SCALE)
				else:
					screen.drawSprite( 1, 1, x*16*SCALE, y*16*SCALE)
		
