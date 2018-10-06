from entities.enemies.simpleenemy import *
from constants import *

class Balumba (Simpleenemy):
	def __init__(self, sheet, id, length, x, y, speed, animationSpeed, vx):
		Simpleenemy.__init__(self, sheet, id, length, x, y, 0, speed, animationSpeed, vx)
		self.vy = 3
		self.collision = True
		self.mobcontrol = True

	def clone(self, x, y):
		return Balumba(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.vx)	

	def tick (self, level):
		if (not level.isSolidTile(int((self.x)/16 + self.vx), int((self.y + 16 + 8)/16))):
			self.wallCollide()
			print("outside")
		if(self.deadTime <= 0):
			if (self.mark):
				self.dead = True
				return
			self.simpleMovement(level)
		else:
			self.id = BALUMBA_DEAD
			self.deadTime -= 1
			self.mark = True

	def kill (self, overwrite):
		self.deadTime = 15

	def wallCollide(self):
		self.vx = -self.vx