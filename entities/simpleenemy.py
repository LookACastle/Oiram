from entities.animatedmob import *
from constants import SCALE

class Simpleenemy (animatedMob):
	def __init__(self, sheet, id, length, x, y, speed, animationSpeed, gravity, vx):
		animatedMob.__init__(self, sheet, id, length, x, y, 0, animationSpeed, True)
		self.gravity = gravity
		if (gravity):
			self.vy = 3
		self.vx = vx
		self.deadTime = 0
		self.mark = False
		self.speed = speed

	def clone(self, x, y):
		return Simpleenemy(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.gravity, self.vx)	
		
	def tick(self, level):
		
		if(self.deadTime <= 0):
			if (self.mark):
				self.dead = True
				return
			self.animationtick()
			coly = self.movey(level)
			colx = self.movex(level)
			if (colx):
				self.vx = -self.vx
		else:
			self.id = 6
			self.deadTime -= 1
			self.mark = True

		

	def collide(self, victim):
		if (self.deadTime <= 0):
			if (victim.invincibleCounter > 0 or victim.jump):
				self.deadTime = 30
				if (victim.jump):
					victim.vy = -3
				return
			victim.kill(False)
