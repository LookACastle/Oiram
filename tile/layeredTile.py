from tile.tile import Tile

class LayeredTile (Tile):
	def __init__(self, id, fid):
		Tile.__init__(self, id)
		self.fid = fid

	def render (self, screen, x, y):
		screen.drawSprite( 1, self.id, x, y)
		screen.drawSprite( 1, self.fid, x, y)
		
		