import pygame
import copy
from tile import *
from constants import *

class Level:
	def __init__(self, path, tileManager, entityManager):
		self.tileManager = tileManager
		self.entityManager = entityManager
		self.map = []
		self.entities = []
		self.loadedEntities = []
		self.loadTileMap(path)
		self.open = True
		self.cleared = False
		self.pause = False
		self.endFlag = False
		self.coinCount = 0

	def loadTileMap (self, path):
		img = pygame.image.load("levels/levels/" + path)
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
					self.loadedEntities.append(entity.clone(x*16*SCALE, y*16*SCALE))

	def reset (self):
		self.entities = []
		for e in self.loadedEntities:
			self.entities.append(e.clone(e.x, e.y))

	def tileCollision(self, points, colType):
		for p in points:
			tile = self.getTile(p[0], p[1])
			if (tile.isSolid()):
				return True
		return False
	
	def isSolidTile(self, x, y):
		if (x < 0 or x >= self.width): return True
		if (y<0 or y >=self.height): return False
		return self.map[x + y*self.width].isSolid()

	def getTile(self, x, y):
		if (x<0 or x>=self.width): return self.tileManager.getNullTile()
		if (y<0 or y>=self.height): return self.tileManager.getNullTile()
		return self.map[x + y*self.width]

	def tick(self):
		iOffset = 0
		if (not self.pause):
			for i in range(0,len(self.entities)):
				e = self.entities[i - iOffset]
				e.tick(self)
				if (e.dead):
					del(self.entities[i])
					iOffset +=1

	def entityCollision (self, target):
		for e in self.entities:
			if (e.collision):
				col = e.entityCollision(target)
				if (col):
					return e
		return None

	def collideTile (self, target, x, y):
		self.getTile(x, y).collision(target, self)
		
	def drawlevel(self, screen, px, py):

		xOffset = 0
		xTile = 0
		halfScreenWidth = X_TILE_COUNT*8*SCALE
		halfTile = 8*SCALE
		if (px >= halfScreenWidth - halfTile):
			xOffset = halfScreenWidth - px - halfTile
			xTile = int(-xOffset/(16*SCALE))
		if (xTile + X_TILE_COUNT >= self.width ):
			xOffset = X_TILE_COUNT*halfTile-(self.width*16 - X_TILE_COUNT*8)*SCALE
			xTile = self.width - X_TILE_COUNT - 1

		yOffset = 0
		yTile = 0
		if (py > Y_TILE_COUNT*8*SCALE-8*SCALE):
			yOffset = Y_TILE_COUNT*8*SCALE-py-8*SCALE
			yTile = int(-yOffset/(16*SCALE))
		if (yTile + Y_TILE_COUNT >= self.height ):
			yOffset = Y_TILE_COUNT*8*SCALE-(self.height*16 - Y_TILE_COUNT*8)*SCALE
			yTile = self.height - Y_TILE_COUNT - 1

		screen.setOffset(xOffset, yOffset)

		for x in range(0 , X_TILE_COUNT + 1):
			for y in range(0,Y_TILE_COUNT + 1):
				tile = self.map[xTile + x + (y+yTile)*self.width]
				if (tile != None):
					tile.render(screen, (x+xTile)*16*SCALE, (y+yTile)*16*SCALE)
		
		for e in self.entities:
			if (e.x + xOffset > 0 and e.x + xOffset<X_TILE_COUNT*16*SCALE or e.x + e.width*16*SCALE + xOffset > 0 and e.x + e.width*16*SCALE + xOffset<X_TILE_COUNT*16*SCALE ):
				e.render(screen)
		
		
