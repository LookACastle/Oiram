from tile.tile import Tile
from constants import *

class LayeredTile (Tile):
	def __init__(self, id, fid):
		Tile.__init__(self, id, False)
		self.fid = fid

	def render (self, screen, x, y):
		screen.drawSprite( TEXTURE, self.id, x, y)
		screen.drawSprite( TEXTURE, self.fid, x, y)
		
		
