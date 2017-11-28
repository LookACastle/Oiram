from entities.animatedmob import *

class Coin (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)

	def clone(self, x, y):
		return Shroom(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	
		
	def tick(self, level):
		self.animationtick()

	def collide(self, victim):
		victim.addCoin()
		self.dead = True