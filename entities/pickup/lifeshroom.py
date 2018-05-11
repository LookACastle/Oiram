from entities.animatedmob import *

class LifeShroom (animatedMob):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		animatedMob.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)
		self.killable = False

	def clone(self, x, y):
		return LifeShroom(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	
		
	def tick(self, level):
		self.animationtick()

	def collide(self, victim):
		victim.addLife()
		self.dead = True