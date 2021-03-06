from entities.mob import *
from constants import *

class FlagTop (Mob):
	def __init__(self, sheet, x, y):
		Mob.__init__(self, sheet, WIN_FLAG_TOP, x, y, True, 0)
		self.height = 4
		self.x1 = 7
		self.y1 = 10
		self.killable = False
		self.used = False
		
	def clone(self, x, y):
		return FlagTop(self.sheet, x, y)	

	def collide(self, victim):
		victim.victory()
		if (not self.used):
			victim.addLife()
			self.used = True
		
	def render (self, screen):
		screen.drawSprite( self.sheet, self.id, self.x, self.y)