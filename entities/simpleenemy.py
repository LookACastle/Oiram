from entities.animatedmob import *

class Simpleenemy (animatedMob):
	def __init__(self, sheet, id, length, x, y, animationSpeed, collision, gravity, vx):
		animatedMob.__init__(self, sheet, id, length, x, y, 0, animationSpeed, collision)
		self.vx = vx

	def clone(self, x, y):
		return Simpleenemy(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	
		
	def tick(self, level):
		self.animationtick()

		col = self.movey(level)
		

	def collide(self, victim):
		self.dead = True