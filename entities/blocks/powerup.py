from entities.animatedmob import *
from constants import *

class Powerup (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, content):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, False)
		self.hitTime = 0
		self.mark = False
		self.oy = y
		self.content = content
		self.empty = False
		self.solid = True

	def clone(self, x, y):
		return Powerup(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.content)	

	def tick(self, level):
		if (not self.empty):
			self.animationtick()
			
		if (self.hitTime > 0):
			if (self.content != None):
				level.addEntity(self.content, self.x, self.y - 16*SCALE)
				self.content = None
			self.y -= 5
			self.hitTime -= 1
		else:
			if (self.y >= self.oy):
				self.y = self.oy
			else:
				self.y += 5

		if(self.mark):
			self.dead = True

		if (self.content == None and self.y == self.oy):
			level.setTile(int(self.x/(16*SCALE) + 0.1), int(self.y/(16*SCALE) + 0.1), 0x0C9AAF)
			self.mark = True

	def trigger(self, target):
		print("col")
		if (self.content != None):
			self.empty = True
			self.hitTime = 6

	def collide(self, victim):
		pass