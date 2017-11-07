from tile.tile import Tile
from constants import *

class ScaledTile (Tile):
	def __init__(self, sheet, id):
		Tile.__init__(self, sheet, id, False)

	def render (self, screen, x, y):
		screen.drawScaledSprite( self.sheet, self.id, x, y)
		
		
