from levels.level import *

class LevelManager (Level):
	def __init__(self, tileManager, entityManager):
		Level.__init__(self, MAP, tileManager, entityManager)
		self.currentlevel = None
		self.levels = []
		self.loadLevels()
		self.playerv = (0,0)
		self.mapwidth = 16
		self.mapheight = 16
		self.cpos = (0,0)
		self.velocity = (0,0)
		self.movementTicks = 0
	
	def getCurrentLevel (self):
		return self.currentlevel

	def tick(self):
		if (self.movementTicks > 0):
			self.movementTicks -= 1
		else:
			self.movementTicks = 0
			self.velocity = (0, 0)

	def changeLevel (self):
		self.currentlevel = self.levels[0]

	def getVelocity(self):
		return self.velocity

	def drawCurrentlevel(self, screen, px, py):
		if (self.currentlevel == None):
			self.drawlevel(screen, px, py)
			for x in range(0,self.mapheight):
				for y in range(0,self.mapwidth):
					screen.drawSprite( TEXTURE, POWERUP, (1+4*x)*16*SCALE, (1+4*y)*16*SCALE)
		else:
			self.currentlevel.drawlevel(screen, px, py)

	def loadLevels (self):
		for path in LEVELS:
			if (path == None):
				self.levels.append(None)
			else:
				level = Level(path, self.tileManager, self.entityManager)
				self.levels.append(level)

	def goLeft (self):
		self.velocity = (-1,0)
		#self.cpos[0] += 1
		self.movementTicks = 16*4

	def goRight (self):
		self.velocity = (1,0)
		#self.cpos[0] -= 1
		self.movementTicks = 16*4

	def goDown (self):
		self.velocity = (0,1)
		self.movementTicks = 16*4

	def goUp (self):
		self.velocity = (0,-1)
		self.movementTicks = 16*4