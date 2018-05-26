from entities.enemies.simpleenemy import *
from constants import *

class Shell (Simpleenemy):
	def __init__(self, sheet, id, length, x, y, speed, animationSpeed):
		Simpleenemy.__init__(self, sheet, id, length, x, y, 0, speed, animationSpeed, 0)
		self.vy = 3
		self.held = True
		self.killable = False
		self.realeaseTimer = 0
		self.mobcontrol = True
		self.speed = 1.5
		self.lifespan = 600
		self.entitycollision = True

	def clone(self, x, y):
		return Shell(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed)	

	def align(self, direction, level):
		self.vy = 0
		self.realeaseTimer = 10
		cy = (self.y + self.y1)/16 + 0.1
		cyh = (self.y - self.y2)/16 + self.height - 0.2
		if (not direction):
			self.vx = self.speed
			cx = (self.x - self.x2)/16
			nx = int(cx) + 1 + self.width
			if (nx < 0 or nx >= level.width): 
				self.x = int(cx)*16
			else:
				col1 = level.isSolidTile(nx, int(cy))
				col2 = level.isSolidTile(nx, int(cyh))
				if (col1 or col2):
					self.x = int(cx + 1)*16 + 0.1 + self.x2 - 16
		else:
			self.vx = -self.speed
			cx = (self.x + self.x1)/16
			nx = int(cx) - 1
			if (cx <= 0 or nx >= level.width): 
				self.x = int(cx + 1)*16
				return True
			else:
				col1 = level.isSolidTile(nx, int(cy))
				col2 = level.isSolidTile(nx, int(cyh))
				if (col1 or col2):
					self.x = int(cx + 1)*16 - 0.1 - self.x1

	def tick (self, level):
		if(self.vx != 0):
			self.simpleMovement(level)
		if (self.realeaseTimer > 0):
			self.realeaseTimer -= 1
		if (self.lifespan <= 0):
			self.dead = True
			if (self.vx >= 0):
				level.addEntity(0x0A0000, self.x, self.y - 16)
			else:
				level.addEntity(0x0A0001, self.x, self.y - 16)
		self.lifespan -= 1

	def collide(self, victim):
		if (self.vx != 0):
			if (self.realeaseTimer <= 0):
				victim.kill(False)
		else:
			if (victim.y + victim.height*16 < self.y + 16 and victim.vy >= 0 and victim.mobcontrol == False):
				self.realeaseTimer = 10
				victim.vy = -ORIAM_VERTICAL_MAX_SPEED
				victim.jump = True
				if (self.x > victim.x):
					self.vx = self.speed
				else:
					self.vx = -self.speed


	def wallCollide(self):
		self.vx = -self.vx
