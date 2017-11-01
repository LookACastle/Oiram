from constants import *

class Tile:
	def __init__(self, id, solid):
		self.id = id
		self.solid = solid

	def isSolid (self):
		return self.solid

	def render (self, screen, x, y):
		screen.drawSprite( TEXTURE, self.id, x, y)
		
		