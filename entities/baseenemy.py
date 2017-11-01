from entities.mob import *

class Baseenemy (Mob):
	def __init__(self, sheet, x, y, collision, speed):
		Mob.__init__(self, sheet, 0, x, y, collision, speed)
		self.vx = -1
	
	
	def tick(self, level):
		col = self.movex()
		
		if col == 1:
			self.vx = -self.vx