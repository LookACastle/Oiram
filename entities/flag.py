from entities.mob import *

class Flag (Mob):
	def __init__(self, sheet, id, x, y):
		Mob.__init__(self, sheet, id, x, y, True, 0)
		
	def clone(self, x, y):
		return Flag(self.sheet, self.id, x, y)	

	def collide(self, victim):
		victim.done = True

	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y + self.yOffset)