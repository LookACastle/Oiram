from entities.animatedmob import *
from constants import *

class Spring (animatedMob):
	def __init__(self, sheet, id, length, x, y, animationSpeed, content, usedid):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, True)
		self.hitTime = 0
		self.HeldItem = False

	def clone(self, x, y):
		return HeldItem(self.sheet, self.id, self.length, x, y, 0, self.animationSpeed, self.content, self.usedid)	

	def tick(self, level):
		if (self.hitTime > 0):
			self.animationtick()
			sheete.hitTime -= 1

	def collide(self, victim):
		if (victim.vy > 0):
			victim.vy = -5
			self.hitTime = 10