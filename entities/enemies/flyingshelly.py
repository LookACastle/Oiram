from entities.enemies.shelly import *
import random

class FlyingShelly(Shelly):
	def __init__(self, sheet, id, length, x, y, speed, animationSpeed, vx, shell):
		Shelly.__init__(self, sheet, id, length, x, y, speed, animationSpeed, vx, shell)
		self.intialtime = random.randint(40, 100)
		self.downTime = self.intialtime
		self.vy = 1
		self.flip = self.vx >= 0

	def clone(self, x, y):
		return FlyingShelly(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.vx, self.shell)	

	def tick (self, level):
		self.animationtick()
		if (self.mark):
			self.dead = True
			return
		if (self.downTime == 0):
			self.downTime = self.intialtime
			self.vy = -self.vy
		else:
			self.downTime -= 1
		self.x += self.vx
		self.y += self.vy
	
	def wallCollide(self):
		pass