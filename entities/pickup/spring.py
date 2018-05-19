from entities.animatedmob import *
from constants import *

class Spring (animatedMob):
	def __init__(self, sheet, id, length, x, y, animationSpeed):
		animatedMob.__init__(self, sheet, id, length, x, y, 0, animationSpeed, True)
		self.hitTime = 0
		self.held = True
		self.killable = False

	def clone(self, x, y):
		return Spring(self.sheet, self.id, self.length, x, y, self.animationSpeed)	

	def tick(self, level):
		self.movey(level)
		self.applyGravity(GLOBAL_GRAVITY, NORMAL_VERTICAL_MAX_SPEED)
		if (self.hitTime > 0):
			self.animationtick()
			self.hitTime -= 1

	def align(self, direction, level):
		cy = (self.y + self.y1)/16 + 0.1
		cyh = (self.y - self.y2)/16 + self.height - 0.2
		if (not direction):
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

	def collide(self, victim):
		if (victim.vy > 0 and (self.y + 16 != victim.y + victim.height*16 and victim.jump == True)):
			victim.vy = -2.5
			self.vy = -0.2
			victim.jump = True
			victim.boosttimer = 10
			self.hitTime = 22