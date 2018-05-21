from entities.pickup.coin import *
import random

class Coindrop (Coin):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		Coin.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)
		self.timeToLive = 20
		self.vx = -(random.randint(0, 10)-5)/10
		self.vy = -3

	def clone(self, x, y):
		return Coindrop(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	

	def tick(self, level):
		self.animationtick()
		self.x += self.vx

		if (self.timeToLive > 0):
			self.vy += 0.2
			self.y += self.vy
			self.timeToLive -= 1
		else:
			self.dead = True
			level.addCoin += 1
