from entities.pickup.shroom import *

class FireFlower (Shroom):
	def __init__(self, sheet, id, length, x, y, pause, animationSpeed, collision):
		Shroom.__init__(self, sheet, id, length, x, y, pause, animationSpeed, collision)

	def clone(self, x, y):
		return FireFlower(self.sheet, self.id, self.length, x, y, self.addPause, self.animationSpeed, self.collision)	

	def collide(self, victim):
		victim.enlarge(True)
		self.dead = True