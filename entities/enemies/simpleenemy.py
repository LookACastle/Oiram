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
		pass

	def kill(self):
		self.dead = True

	def collide(self, victim):
		if (self.deadTime <= 0):
			if (victim.invincibleCounter > 0 or victim.jump):
				cx = victim.x + (victim.width*SCALE)/2
				if (cx > self.x or cx < self.x + self.width*SCALE):
					self.kill()
					self.collision = False
					if (victim.jump):
						victim.vy = -3
					return
			victim.kill(False)
