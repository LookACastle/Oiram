from entities.animatedmob import *

class Shroom (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)

	def clone(self, x, y):
		return Shroom(self.sheet, self.id, self.length, x, y, self.pause, self.animationSpeed, self.collision)	
		
	def tick(self, level):
		self.animationtick()

		coly = self.movey(level)

	def collide(self, victim):
		victim.enlarge()
		self.dead = True