from entities.enemies.simpleenemy import *
from constants import *

class Spikey (Simpleenemy):
	def __init__(self, sheet, id, length, x, y, speed, animationSpeed, vx):
		Simpleenemy.__init__(self, sheet, id, length, x, y, 0, speed, animationSpeed, vx)
		self.vy = 3
		self.killable = False

	def clone(self, x, y):
		return Balumba(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.vx)	

	def tick (self, level):
		if(self.deadTime <= 0):
			if (self.mark):
				self.dead = True
				return
			self.simpleMovement(level)
		else:
			self.id = BALUMBA_DEAD
			self.deadTime -= 1
			self.mark = True

	def wallCollide(self):
		self.vx = -self.vx