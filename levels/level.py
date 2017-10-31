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
					temp.append(self.tileManager.getTile(0xFFFFFF))
		return temp

	def getTile(self, x, y):
		if (x<0 or x>self.width): return tileManager.getNullTile()
		if (y<0 or x>self.height): return tileManager.getNullTile()
		return self.map[x + y*self.width]
	def drawlevel(self, screen, px, py):

		xOffset = 0
		xTile = 0
		if (px >= X_TILE_COUNT*8*SCALE-8*SCALE):
			xOffset = X_TILE_COUNT*8*SCALE-px-8*SCALE
			xTile = int(-xOffset/(16*SCALE))
		if (xTile + X_TILE_COUNT >= self.width ):
			xOffset = X_TILE_COUNT*8*SCALE-(self.width*16 - X_TILE_COUNT*8)*SCALE
			xTile = self.width - X_TILE_COUNT - 1
		for x in range(0 , X_TILE_COUNT+1):
			for y in range(0,Y_TILE_COUNT):
				tile = self.map[xTile + x + y*self.width]
				if (tile == None):
					screen.drawSprite( 1, 0, xOffset+(x+xTile)*16*SCALE, y*16*SCALE)
				else:
					tile.render(screen, xOffset+(x+xTile)*16*SCALE, y*16*SCALE)
		
