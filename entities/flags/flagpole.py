from entities.mob import *
from constants import *

class FlagPole (Mob):
	def __init__(self, sheet, x, y):
		Mob.__init__(self, sheet, WIN_FLAG_POLE, x, y, True, 0)
		self.height = 4
		self.x1 = 8
		
	def clone(self, x, y):
		return FlagPole(self.sheet, x, y)	

	def collide(self, victim):
		victim.victory()

	def kill(self):
		pass
	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y)