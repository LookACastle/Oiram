import pygame
import copy
from tile import *
from constants import *
import importlib

class Level:
	def __init__(self, path, tileManager, entityManager, threadManager):
		self.tileManager = tileManager
		self.entityManager = entityManager
		self.threadManager = threadManager
		temp = path.replace(".png", "").split("-")
		self.backgroundtile = None
		self.type = temp[0]
		self.name = int(temp[1])
		self.map = []
		self.entities = []
		self.loadedEntities = []
		self.loadedMap = []
		self.spawnx = 0
		self.spawny = 0
		self.loadTileMap(path)
		self.open = True
		self.cleared = False
		self.coinCount = 0
		self.pauseTimer = 0
		self.endFlag = False
		self.entityQueue = []
		self.addCoin = 0

	def loadTileMap (self, path):
		img = pygame.image.load("levels/levels/" + path)
		size = img.get_rect().size
		self.width = size[0]
		self.height = size[1]
		pixel = pygame.PixelArray(img)
		tube = False;
		delayedentities = []
		self.backgroundtile = self.tileManager.getTile(pixel[0][0])
		for y in range(0,self.height):
			for x in range(0,self.width):
				colour = pixel[x][y]
				if (colour == 0xFF0001):
					self.spawnx = x*16
					self.spawny = y*16
				if (tube):
					tube = False
					colour = 0x0F0100
				if (colour == 0x346800 or colour == 0x10D080):
					tube = True

				tile = self.tileManager.getTile(colour)

				if (tile != None):
					self.loadedMap.append(tile)
				else:
					self.loadedMap.append(self.tileManager.getTile(0xFFFFFF))
				entity = self.entityManager.getEntity(pixel[x][y])
				if (entity != None):
					self.loadedEntities.append(entity.clone(x*16, y*16))
		self.map = self.loadedMap[:]

	def reset (self):
		self.exhausted = []
		self.entities = []
		for e in self.loadedEntities:
			self.entities.append(e.clone(e.x, e.y))
		self.map = self.loadedMap[:]

	def tileCollision(self, points, colType):
		for p in points:
			tile = self.getTile(p[0], p[1])
			if (tile.isSolid()):
				return True
		return False
	
	def isSolidTile(self, x, y):
		if (y < 0 or y > self.height-1): return False
		return self.map[x + y*self.width].isSolid()
		

	def getTile(self, x, y):
		if (x<0 or x>=self.width): return self.tileManager.getNullTile()
		if (y<0 or y>=self.height): return self.tileManager.getNullTile()
		return self.map[x + y*self.width]

	def setTile(self, x, y, c):
		if (x<0 or x>=self.width): return
		if (y<0 or y>=self.height): return
		self.map[x + y*self.width] = self.tileManager.getTile(c)

	def tick(self, player):
		for e in self.entities:
			self.entityQueue.append(e)
		self.entities = self.entityQueue
		self.entityQueue = []

		iOffset = 0
		if (self.pauseTimer <= 0 and not player.dead):
			for i in range(0,len(self.entities)):
				e = self.entities[i - iOffset]
				if(e.visible):
					e.tick(self)
					if (e.collision and e.entitycollision):
						self.entityCollision(e, True)
				if (e.dead):
					del(self.entities[i- iOffset])
					iOffset +=1
			for coin in range(0, self.addCoin):
					player.addCoin()
			self.addCoin = 0
		else:
			self.pauseTimer -= 1

	def addEntity(self, c, x, y):
		self.entityQueue.append(self.entityManager.getEntity(c).clone(x, y))

	def placeEntity(self, e):
		self.entityQueue.append(e)
	
	def getQueuedEntity (self):
		return self.entityQueue[len(self.entityQueue)-1]

	def addProjectile(self, c, x, y, vx, vy):
		e = self.entityManager.getEntity(c).clone(x, y)
		e.addvel(vx, vy)
		self.entityQueue.append(e)		
	
	def triggerBlock(self, x, y, target):
		for e in self.entities:
			if (e.solid and e.visible):
				if (e.rightDirection([target.vx, target.vy])):
					for w in range(0, e.width):
						if ((e.x + w*16 == x) and e.y == y):
							e.trigger(target)

	def entityCollision (self, target, flip):
		for e in self.entities:
			if (e.collision):
				col = e.entityCollision(target)
				if (col):
					if (flip):
						target.collide(e)
					else:
						e.collide(target)
		return None

	def collideEntity (self, target):
		collided = []
		for e in self.entities:
			if (e.collision):
				col = e.entityCollision(target)
				if (col):
					collided.append(e)
		return collided

	def pickupEntity(self, target):
		collided = None
		for i in range(0, len(self.entities)):
			e = self.entities[i]
			if (e.collision and e.held):
				col = e.entityCollision(target)
				if (col):
					collided = self.entities.pop(i)
					break
		return collided

	def collideTile (self, target, x, y):
		self.getTile(x, y).collision(target, self)
		
	def drawlevel(self, screen, px, py, w, h):
		
		xOffset = 0
		xTile = 0
		halfScreenWidth = w*8
		halfTile = 8
		if (px >= halfScreenWidth - halfTile):
			xOffset = halfScreenWidth - px - halfTile
			xTile = int(-xOffset/(16))
		if (xTile + w >= self.width ):
			xOffset = w*halfTile-(self.width*16 - w*8)
			xTile = self.width - w - 1

		yOffset = 0
		yTile = 0
		if (py > h*8-8):
			yOffset = h*8-py-8
			yTile = int(-yOffset/16)
		if (yTile + h >= self.height ):
			yOffset = h*8-(self.height*16 - h*8)
			yTile = self.height - h - 1
		
		screen.setOffset(xOffset, yOffset)

		for x in range(0 , w + 1):
			for y in range(0,h + 1):
				index = xTile + x + (y+yTile)*self.width
				if (index >= 0 and index < len(self.map)-2): 
					tile = self.map[index]
					if (tile != None):
						self.threadManager.queueWork((3, tile.render, screen, (x+xTile)*16, (y+yTile)*16))
				else:
					self.backgroundtile.render(screen, (x+xTile)*16, (y+yTile)*16)

		
		for e in self.entities:
			if (e.x + xOffset > 0 and e.x + xOffset<w*16 or e.x + e.width*16 + xOffset > 0 and e.x + e.width*16 + xOffset<w*16 ):
				e.render(screen)
				e.visible = True
			else:
				e.visible = False
	