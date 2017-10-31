from tile.tile import *
from tile.layeredTile import LayeredTile
from constants import *

class TileManager:
	def __init__ (self):
		# fra paint 0xRRGGBB
		# til farve 0xBBGGRR
		self.tiles = [None]*(0xFFFFFF+1)

		self.tiles[0x105C96] = Tile(DIRT)
		self.tiles[0x0FFF0F] = Tile(GRASSDIRT)
		self.tiles[0xFF00FF] = Tile(POWERUP)
		self.tiles[0x6F85B8] = Tile(BLOCK)
		self.tiles[0x0099FF] = Tile(BRICK)
		self.tiles[0xDBDBDB] = Tile(STONE)


		self.tiles[0x139932] = LayeredTile(SKY, GRASS)
		self.tiles[0x00FFFF] = LayeredTile(SKY, COIN)

		self.tiles[0xFFFFFF] = Tile(SKY)
		self.nullTile = Tile(SKY)

		GRASS_DIRT = 0


	def getNullTile(self):
		return self.nullTile

	def getTile(self,color):
		return self.tiles[color]
