from tile.tile import *
from tile.layeredtile import LayeredTile
from constants import *

class TileManager:
	def __init__ (self):
		# fra paint 0xRRGGBB
		# til farve 0xBBGGRR
		self.tiles = [None]*(0xFFFFFF+1)

		self.tiles[0x105C96] = Tile(DIRT, True)
		self.tiles[0x0FFF0F] = Tile(GRASSDIRT, True)
		self.tiles[0xFF00FF] = Tile(POWERUP, True)
		self.tiles[0x0C9AAF] = Tile(BLOCK, True)
		self.tiles[0x0099FF] = Tile(BRICK, True)
		self.tiles[0xDBDBDB] = Tile(STONE, True)
		
		self.tiles[0xb469ff] = Tile(SKY, False)
		
		self.tiles[0x139932] = LayeredTile(SKY, GRASS)
		self.tiles[0x00FFFF] = LayeredTile(SKY, COIN_STILL)

		self.tiles[0xFFFFFF] = Tile(SKY, False)
		self.tiles[0xFFFF00] = Tile(STONE_UNDERWORLD, False)
		self.nullTile = Tile(BLOCK, False)

		GRASS_DIRT = 0


	def getNullTile(self):
		return self.nullTile

	def getTile(self,color):
		return self.tiles[color]
