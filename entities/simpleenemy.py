from entities.animatedmob import *
from entities.oriam import Oriam

class Simpleenemy (animatedMob):
	def __init__(self, sheet, id, length, x, y, animationSpeed, collision, gravity, vx):
		animatedMob.__init__(self, sheet, id, length, x, y, 0, animationSpeed, True)
		self.gravity = gravity
		if (gravity):
			self.vy = 3
		self.vx = vx
		self.deadTime = 0
		self.mark = False

	def clone(self, x, y):
		return Simpleenemy(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	
		
	def tick(self, level):

		if(self.deadTime <= 0):
			if (self.mark):
				self.dead = True
				return
			self.animationtick()
			col = self.movey(level)
			col = self.movex(level)
			if (col):
				self.vx = -self.vx
		else:
			self.id = 6
			self.deadTime -= 1
			self.mark = True

		

	def collide(self, victim):
		if (victim.vy > 0):
			if (victim)
		self.dead = True