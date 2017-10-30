from tile.tile import *

class TileManager:
	def __init__ (self):
		# fra paint 0xRRGGBB
		# til farve 0xBBGGRR
		self.tiles = [None]*(0xFFFFFF+1)
		self.tiles[0x0FFF0F] = Tile(0)
		self.tiles[0xFFFFFF] = Tile(2)
		self.nullTile = Tile(2)

	def getNullTile(self):
		return self.nullTile

	def getTile(self,color):
		return self.tiles[color]
