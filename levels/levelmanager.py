from levels.level import *
from constants import *

class LevelManager (Level):
	def __init__(self, tileManager, entityManager):
		Level.__init__(self, MAP, tileManager, entityManager)
		self.currentlevel = None
		self.mapwidth = MAP_WIDTH
		self.mapheight = MAP_HEIGHT

		self.levels = [None]*self.mapwidth*self.mapheight
		self.loadLevels()

		self.playerv = (0,0)
		self.cpos = [0,4]
		self.velocity = [(0)]
		self.movementTicks = -1

		self.horizontaltilecount = X_TILE_COUNT
		self.verticaltaltilecount = Y_TILE_COUNT

		self.openLevels = 0
		self.openlevel(1)

	def updateDrawDistance(screen, x, y):
		self.horizontaltilecount = x
		self.verticaltaltilecount = y

	def getCurrentLevel (self):
		return self.currentlevel

	def tick(self, player):
		if (self.movementTicks > 0):
			self.movementTicks -= 1
		else:
			if (len(self.velocity) != 0):
				del self.velocity[0]
				if (len(self.velocity) != 0):
					self.movementTicks = 16*4
			else:
				self.movementTicks = -1
		if (self.currentlevel != None):
			if (self.currentlevel.endFlag):
				if (player.lifeCount < 2 or player.mark):
					self.currentlevel.endFlag = False
					self.changeLevel(player)
				else:
					self.currentlevel.reset()
					player.reset()
					player.lifeCount -= 1
					self.currentlevel.endFlag = False
				return
			self.currentlevel.tick(player)

	def changeLevel (self, player):
		player.done = False
		player.lockinput = False
		player.invincibleCounter = 0
		player.overlaystrength = 0
		player.deadanimation = False
		if (self.currentlevel == None):
			level = self.levels[self.cpos[0] + self.cpos[1]*self.mapwidth]
			if (isinstance(level, Level)):
				if (level.open):
					self.currentlevel = level
					player.setCheckpoint(self.currentlevel.spawnx, self.currentlevel.spawny)
					self.currentlevel.reset()
					player.reset()
					player.mark = False
					player.speed = 2
					player.yOffset = 0
		else:
			if (self.currentlevel.cleared and self.currentlevel.type != "e"):
				self.openlevel(self.currentlevel.name + 1)
			self.currentlevel = None
			player.setCheckpoint((1+13+4*self.cpos[0])*16, (1+9+4*self.cpos[1])*16) 
			player.reset()
			player.speed = 1
			player.lifeCount = 3

	def getVelocity(self):
		return self.velocity[0]

	def drawCurrentlevel(self, screen, px, py):
		if (self.currentlevel == None):
			self.drawlevel(screen, px, py)
			for x in range(0,self.mapheight):
				for y in range(0,self.mapwidth):
					currentlevel = self.levels[x + y*self.mapwidth]
					if (isinstance(currentlevel, Level)):
						if (currentlevel.open):
							if (not currentlevel.cleared):
								screen.drawScaledSprite( OVERWORLDMAP, OPEN_DOOR, (1+13+4*x)*16, (1+9+4*y)*16, 2)
							else:
								screen.drawScaledSprite( OVERWORLDMAP, COMPLETE_DOOR, (1+13+4*x)*16, (1+9+4*y)*16, 2)
						else:
							screen.drawScaledSprite( OVERWORLDMAP, CLOSED_DOOR, (1+13+4*x)*16, (1+9+4*y)*16, 2)
		else:
			self.currentlevel.drawlevel(screen, px, py, self.horizontaltilecount, self.verticaltaltilecount)

	def loadLevels (self):
		levels = open("levels/maplevels.txt","r")
		x = 0
		y = 0
		for line in levels:
			formattedLine = line.replace("\n","").split("|")
			for s in formattedLine:
				if (len(s) > 0):
					if (s[0] != " "):
						if (s[0] == "/"):
							t = s.replace('/',"").replace(" ","").split(",")
							self.levels[x + y*self.mapwidth] = (int(t[0]), int(t[1]))
						else:
							self.levels[x + y*self.mapwidth] = Level(s, self.tileManager, self.entityManager)
				x += 1
			x = 0
			y += 1

	def openlevel (self, newlevel):
		if (self.openLevels < newlevel):
			self.openLevels = newlevel
		for level in self.levels:
			if (isinstance(level, Level)):
				if (level.name <= self.openLevels):
					level.open = True


	def addMovement(self, vx, vy):
		self.cpos[0] = self.cpos[0] + vx
		self.cpos[1] = self.cpos[1] + vy
		vel = self.getMapTile(self.cpos[0], self.cpos[1])
		if (isinstance(vel, tuple)):
			if (vel[0] != 0 or vel[1] != 0):
				if (vx !=0 and vel[0] != 0):
					self.setMapTile(self.cpos[0], self.cpos[1], (-vel[0], 0))
				elif (vy !=0 and vel[1] != 0):
					self.setMapTile(self.cpos[0], self.cpos[1], (0, -vel[1]))
				elif (vx !=0 and vel[1] != 0):
					self.setMapTile(self.cpos[0], self.cpos[1], (-vx, 0))
				elif (vy !=0 and vel[0] != 0):
					self.setMapTile(self.cpos[0], self.cpos[1], (0, -vy))
				else:
					self.setMapTile(self.cpos[0], self.cpos[1], (-vel[1] , -vel[0]))
				self.velocity.append(vel)
				self.addMovement(vel[0], vel[1])

	def setMapTile(self, x, y, item):
		self.levels[x + y*self.mapwidth] = item

	def getMapTile(self, x, y):
		if (x < 0 or x > self.mapwidth): return None
		if (y < 0 or y > self.mapheight): return None
		return self.levels[x + y*self.mapwidth]

	def goLeft (self):
		if (self.getMapTile(self.cpos[0] - 1, self.cpos[1]) != None):
			self.velocity.append((-1,0))
			self.addMovement(-1, 0)
			self.movementTicks = 16*4 + 1

	def goRight (self):
		if (self.getMapTile(self.cpos[0] + 1, self.cpos[1]) != None):
			self.velocity.append((1,0))
			self.addMovement(1, 0)
			self.movementTicks = 16*4 + 1

	def goDown (self):
		if (self.getMapTile(self.cpos[0], self.cpos[1] + 1) != None):
			self.velocity.append((0,1))
			self.addMovement(0, 1)
			self.movementTicks = 16*4 + 1

	def goUp (self):
		if (self.getMapTile(self.cpos[0], self.cpos[1] - 1) != None):
			self.velocity.append((0,-1))
			self.addMovement(0, -1)
			self.movementTicks = 16*4 + 1

	def drawlevel(self, screen, px, py):

		xOffset = 0
		xTile = 0
		if (px >= self.horizontaltilecount*8-8):
			xOffset = self.horizontaltilecount*8-px-8
			xTile = int(-xOffset/16)
		if (xTile + self.horizontaltilecount >= self.width ):
			xOffset = self.horizontaltilecount*8-(self.width*16 - self.horizontaltilecount*8)
			xTile = self.width - self.horizontaltilecount - 1
		
		yOffset = 0
		yTile = 0
		if (py > self.verticaltaltilecount*8-8):
			yOffset = self.verticaltaltilecount*8-py-8
			yTile = int(-yOffset/16)
		if (yTile + self.verticaltaltilecount >= self.height ):
			yOffset = self.verticaltaltilecount*8-(self.height*16 - self.verticaltaltilecount*8)
			yTile = self.height - self.verticaltaltilecount - 1

		screen.setOffset(xOffset, yOffset)

		for x in range(0 , self.horizontaltilecount + 1):
			for y in range(0,self.verticaltaltilecount + 1):
				tile = self.map[xTile + x + (y+yTile)*self.width]
				if (tile == None):
					screen.drawSprite( TEXTURE, POWERUP, (x+xTile)*16, (y+yTile)*16)
				else:
					tile.render(screen, (x+xTile)*16, (y+yTile)*16)