from constants import *

class Tile:
	def __init__(self, sheet,  id, solid):
		self.id = id
		self.sheet = sheet
		self.solid = solid
		self.test = False

	def isSolid (self):
		return self.solid

	def render (self, screen, x, y):
		screen.drawSprite( self.sheet, self.id, x, y)
	
	def collision(self, target, level):
		pass
		