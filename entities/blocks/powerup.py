from entities.animatedmob import *
from constants import *

class Powerup (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, content, usedid):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, False)
		self.usedid = usedid
		self.hitTime = 0
		self.mark = False
		self.oy = y
		self.content = content
		self.empty = False
		self.solid = True
		self.hit = False;

	def clone(self, x, y):
		return Powerup(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.content, self.usedid)	

	def rightDirection (self, direction):
		if (direction[1] < 0):
			return True
		return False

	def tick(self, level):
		if (not self.empty):
			self.animationtick()
		
		if (self.hitTime > 0):
			self.y -= 5
			self.hitTime -= 1
		else:
			if (self.y >= self.oy):
				self.y = self.oy
			else:
				if (self.content != None):
					level.addEntity(self.content, self.x, self.oy - 16*SCALE)
					self.content = None
				if (self.id != self.usedid):
						self.id = self.usedid
				self.y += 5

		if(self.mark):
			self.dead = True

	def trigger(self, target):
		if (self.hit == False):
			self.empty = True
			self.hit = True
			self.hitTime = 6

	def collide(self, victim):
		pass