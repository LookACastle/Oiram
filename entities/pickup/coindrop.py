from entities.pickup.coin import *

class Coindrop (Coin):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		Coin.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)
		self.timeToLive = 20

	def clone(self, x, y):
		return Coindrop(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	

	def tick(self, level):
		self.animationtick()

		if (self.timeToLive > 0):
			self.timeToLive -= 1
			if (self.timeToLive < 5):
				self.y += 5
			else:
				self.y -= 7
		else:
			self.dead = True
			level.addCoin += 1
