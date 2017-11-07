from levels.level import *
from constants import *

class LevelManager (Level):
	def __init__(self, tileManager, entityManager):
		Level.__init__(self, MAP, tileManager, entityManager)
		self.currentlevel = None
		self.levels = []
		self.loadLevels()

		self.playerv = (0,0)

		self.mapwidth = 16
		self.mapheight = 16
		self.cpos = [0,0]
		self.velocity = [(0)]
		self.movementTicks = 0
	
	def getCurrentLevel (self):
		return self.currentlevel

	def tick(self):
		if (self.movementTicks > 0):
			self.movementTicks -= 1
		else:
			if (len(self.velocity) != 0):
				del self.velocity[0]
				if (len(self.velocity) != 0):
					self.movementTicks = 16*4
			else:
				self.movementTicks = 0

	def changeLevel (self, player):
		self.currentlevel = self.levels[self.cpos[0] + self.cpos[1]*self.mapwidth]
		if (self.currentlevel != None):
			player.x = 100
			player.y = SCREEN_HEIGHT-32*SCALE
			player.vx = 0
			player.vy = 0

	def getVelocity(self):
		return self.velocity[0]

	def drawCurrentlevel(self, screen, px, py):
		if (self.currentlevel == None):
			self.drawlevel(screen, px, py)
			for x in range(0,self.mapheight):
				for y in range(0,self.mapwidth):
					currentlevel = self.levels[x + y*self.mapwidth]
					if (isinstance(currentlevel, Level)):
						screen.drawSprite( TEXTURE, POWERUP, (1+4*x)*16*SCALE, (1+4*y)*16*SCALE)
		else:
			self.currentlevel.drawlevel(screen, px, py)

	def loadLevels (self):
		for item in LEVELS:
			if (not isinstance(item, str)):
				self.levels.append(item)
			else:
				level = Level(item, self.tileManager, self.entityManager)
				self.levels.append(level)

	def addMovement(self, x, y):
		if (isinstance(self.getMapTile(x,y), tuple)):
			vel = self.levels[x + y*self.mapwidth]
			self.setMapTile(x, y, (-vel[1], -vel[0]))
			self.cpos[0] = self.cpos[0] + vel[0]
			self.cpos[1] = self.cpos[1] + vel[1]
			self.velocity.append(vel)
			self.addMovement(x+vel[0], y+vel[1])

	def setMapTile(self, x, y, item):
		self.levels[x + y*self.mapwidth] = item

	def getMapTile(self, x, y):
		if (x < 0 or x > self.mapwidth): return None
		if (y < 0 or y > self.mapheight): return None
		return self.levels[x + y*self.mapwidth]

	def goLeft (self):
		if (self.getMapTile(self.cpos[0] - 1, self.cpos[1]) != None):
			self.velocity.append((-1,0))
			self.cpos[0] = self.cpos[0] - 1
			self.addMovement(self.cpos[0], self.cpos[1])
			self.movementTicks = 16*4

	def goRight (self):
		if (self.getMapTile(self.cpos[0] + 1, self.cpos[1]) != None):
			self.velocity.append((1,0))
			self.cpos[0] = self.cpos[0] + 1
			self.addMovement(self.cpos[0], self.cpos[1])
			self.movementTicks = 16*4

	def goDown (self):
		if (self.getMapTile(self.cpos[0], self.cpos[1] + 1) != None):
			self.velocity.append((0,1))
			self.cpos[1] = self.cpos[1] + 1
			self.addMovement(self.cpos[0], self.cpos[1])
			self.movementTicks = 16*4

	def goUp (self):
		if (self.getMapTile(self.cpos[0], self.cpos[1] - 1) != None):
			self.velocity.append((0,-1))
			self.cpos[1] = self.cpos[1] - 1
			self.addMovement(self.cpos[0], self.cpos[1])
			self.movementTicks = 16*4

	def drawlevel(self, screen, px, py):

		xOffset = 0
		xTile = 0
		if (px >= X_TILE_COUNT*8*SCALE-8*SCALE):
			xOffset = X_TILE_COUNT*8*SCALE-px-8*SCALE
			xTile = int(-xOffset/(16*SCALE))
		if (xTile + X_TILE_COUNT >= self.width ):
			xOffset = X_TILE_COUNT*8*SCALE-(self.width*16 - X_TILE_COUNT*8)*SCALE
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
				if (tile == None):
					screen.drawSprite( TEXTURE, POWERUP, (x+xTile)*16*SCALE, (y+yTile)*16*SCALE)
				else:
					tile.render(screen, (x+xTile)*16*SCALE, (y+yTile)*16*SCALE)