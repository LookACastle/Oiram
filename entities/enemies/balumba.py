from entities.enemies.simpleenemy import *
from constants import SCALE

class Balumba (Simpleenemy):
	def __init__(self, sheet, id, length, x, y, speed, animationSpeed, vx):
		Simpleenemy.__init__(self, sheet, id, length, x, y, 0, speed, animationSpeed, vx)
		self.vy = 3

	def clone(self, x, y):
		return Balumba(self.sheet, self.id, self.length, x, y, self.speed, self.animationSpeed, self.vx)	

	def wallCollide(self):
		self.vx = -self.vx