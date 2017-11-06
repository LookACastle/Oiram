import pygame
from tile import *
from constants import *

class Level:
	def __init__(self, path, tileManager, entityManager):
		self.tileManager = tileManager
		self.entityManager = entityManager
		self.map = []
		self.entities = []
		self.loadTileMap(path)

	def loadTileMap (self, path):
		img = pygame.image.load("levels/" + path)
		size = img.get_rect().size
		self.width = size[0]
		self.height = size[1]
		pixel = pygame.PixelArray(img)
		self.map = []
		for y in range(0,self.height):
			for x in range(0,self.width):
				tile = self.tileManager.getTile(pixel[x][y])
				if (tile != None):
					self.map.append(tile)
				else:
					self.map.append(self.tileManager.getTile(0xFFFFFF))
				entity = self.entityManager.getEntity(pixel[x][y])
				if (entity != None):
					self.entities.append(entity.clone(x*16*SCALE, y*16*SCALE))

	def tileCollision(self, points, colType):
		for p in points:
			tile = self.getTile(p[0], p[1])
			if (tile.isSolid()):
				return True
		return False
	
	def isSolidTile(self, x, y):
		if (x<0 or x>self.width): return True
		if (y>self.height): return True
		if (y<0): return False
		return self.map[x + y*self.width].isSolid()

	def getTile(self, x, y):
		if (x<0 or x>self.width): return self.tileManager.getNullTile()
		if (y<0 or y>self.height): return self.tileManager.getNullTile()
		return self.map[x + y*self.width]

	def tick(self):
		for e in self.entities:
			e.tick(self)

	def drawlevel(self, screen, px, py):

		xOffset = 0
		xTile = 0
		if (px >= X_TILE_COUNT*8*SCALE-8*SCALE):
			xOffset = X_TILE_COUNT*8*SCALE-px-8*SCALE
			xTile = int(-xOffset/(16*SCALE))
		if (xTile + X_TILE_COUNT >= self.width ):
			xOffset = X_TILE_COUNT*8*SCALE-(self.width*16 - X_TILE_COUNT*8)*SCALE
			xTile = self.width - X_TILE_COUNT - 1
		
		screen.setOffset(xOffset, 0)
		
		for x in range(0 , X_TILE_COUNT+1):
			for y in range(0,Y_TILE_COUNT):
				tile = self.map[xTile + x + y*self.width]
				if (tile == None):
					screen.drawSprite( TEXTURE, POWERUP, (x+xTile)*16*SCALE, y*16*SCALE)
				else:
					tile.render(screen, (x+xTile)*16*SCALE, y*16*SCALE)

		for e in self.entities:
			e.render(screen)
		
