from tile.tile import *
from tile.layeredtile import LayeredTile
from constants import *

class TileManager:
	def __init__ (self):
		# fra paint 0xRRGGBB
		# til farve 0xBBGGRR
		self.tiles = [None]*(0xFFFFFF+1)


		"""
		-------------Default level Tiles-------------
		"""
		self.tiles[0x105C96] = Tile(TEXTURE, DIRT, True)
		self.tiles[0x0FFF0F] = Tile(TEXTURE, GRASSDIRT, True)
		self.tiles[0xFF00FF] = Tile(TEXTURE, POWERUP, True)
		self.tiles[0x0C9AAF] = Tile(TEXTURE, BLOCK, True)
		self.tiles[0x0099FF] = Tile(TEXTURE, BRICK, True)
		self.tiles[0xDBDBDB] = Tile(TEXTURE, STONE, True)
		
		self.tiles[0xb469ff] = Tile(TEXTURE, SKY, False)
		
		self.tiles[0x139932] = LayeredTile(TEXTURE, SKY, GRASS)
		self.tiles[0x00FFFF] = LayeredTile(TEXTURE, SKY, COIN_STILL)

		self.tiles[0xFFFFFF] = Tile(TEXTURE, SKY, False)
		self.tiles[0xFFFF00] = Tile(TEXTURE, STONE_UNDERWORLD, False)
		self.nullTile = Tile(TEXTURE, BLOCK, False)


		"""
		-------------Overworld map Tiles-------------
		"""
		self.tiles[0x29B547] = Tile(OVERWORLDMAP, BG, False)


	def getNullTile(self):
		return self.nullTile

	def getTile(self,color):
		return self.tiles[color]
