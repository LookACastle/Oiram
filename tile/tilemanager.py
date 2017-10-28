from tile.tile import *

class TileManager:
	def __init__ (self):
		self.tiles = [None]*(0xFFFFFF+1)
		self.tiles[0x0000FF] = Tile(7)

	def getTile(self,color):
		return self.tiles[color]
