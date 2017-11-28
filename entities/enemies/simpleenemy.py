from entities.animatedmob import *
from constants import SCALE

class Simpleenemy (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, speed, animationSpeed, vx):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, True)
		self.vx = vx
		self.deadTime = 0
		self.mark = False
		self.speed = speed

	def clone(self, x, y):
		return Simpleenemy(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.vx)	
	
	def simpleMovement(self, level):
		self.animationtick()
		coly = self.movey(level)
		if (self.y > level.height*16*SCALE):
			self.mark = True
		colx = self.movex(level)
		if (colx):
			self.wallCollide()

	def tick(self, level):
		if(self.deadTime <= 0):
			if (self.mark):
				self.dead = True
				return
			self.simpleMovement(level)
		else:
			self.id = 6
			self.deadTime -= 1
			self.mark = True

	def collide(self, victim):
		if (self.deadTime <= 0):
			if (victim.invincibleCounter > 0 or victim.jump):
				self.deadTime = 15
				if (victim.jump):
					victim.vy = -3
				return
			victim.kill(False)
