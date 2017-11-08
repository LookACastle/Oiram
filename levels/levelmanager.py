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

		self.levels[0].open = True
		self.playerv = (0,0)
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
		if (self.currentlevel != None):
			self.currentlevel.tick()

	def changeLevel (self, player):
		if (self.currentlevel == None):
			level = self.levels[self.cpos[0] + self.cpos[1]*self.mapwidth]
			if (isinstance(level, Level)):
				if (level.open):
					self.currentlevel = level
					player.x = 100
					player.y = SCREEN_HEIGHT-5*16*SCALE
					player.vx = 0
					player.vy = 0
		else:
			self.currentlevel = None
			player.x = (1+4*self.cpos[0])*16*SCALE
			player.y = (1+4*self.cpos[1])*16*SCALE
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
						if (currentlevel.open):
							if (not currentlevel.cleared):
								screen.drawScaledSprite( OVERWORLDMAP, OPEN_DOOR, (1+4*x)*16*SCALE, (1+4*y)*16*SCALE)
							else:
								screen.drawScaledSprite( OVERWORLDMAP, COMPLETE_DOOR, (1+4*x)*16*SCALE, (1+4*y)*16*SCALE)
						else:
							screen.drawScaledSprite( OVERWORLDMAP, CLOSED_DOOR, (1+4*x)*16*SCALE, (1+4*y)*16*SCALE)
		else:
			self.currentlevel.drawlevel(screen, px, py)

	def loadLevels (self):
		levels = open("levels/maplevels.txt","r")
		x = 0
		y = 0
		for line in levels:
			formattedLine = line.replace("\n","").split("	")
			for s in formattedLine:
				if (len(s) > 0):
					if (s[0] == "/"):
						t = s.replace('/',"").split(",")
						self.levels[x + y*self.mapwidth] = (int(t[0]), int(t[1]))
					else:
						self.levels[x + y*self.mapwidth] = Level(s, self.tileManager, self.entityManager)
				x += 1
			x = 0
			y += 1

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
			self.movementTicks = 16*4

	def goRight (self):
		if (self.getMapTile(self.cpos[0] + 1, self.cpos[1]) != None):
			self.velocity.append((1,0))
			self.addMovement(1, 0)
			self.movementTicks = 16*4

	def goDown (self):
		if (self.getMapTile(self.cpos[0], self.cpos[1] + 1) != None):
			self.velocity.append((0,1))
			self.addMovement(0, 1)
			self.movementTicks = 16*4

	def goUp (self):
		if (self.getMapTile(self.cpos[0], self.cpos[1] - 1) != None):
			self.velocity.append((0,-1))
			self.addMovement(0, -1)
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