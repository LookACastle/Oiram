from entities.animatedmob import *

class Coin (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)
		self.killable = False

	def clone(self, x, y):
		return Coin(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	

	def collide(self, victim):
		if (not victim.dead):
			victim.addCoin()
		self.dead = True