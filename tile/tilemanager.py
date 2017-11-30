from tile.tile import *
from tile.layeredtile import LayeredTile
from tile.scaledtile import ScaledTile
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
		self.tiles[0x0C9AAF] = Tile(TEXTURE, BLOCK_PUSH, True)
		self.tiles[0xDBDBDB] = Tile(TEXTURE, STONE, True)

		#Castle
		self.tiles[0x0099FF] = Tile(TEXTURE, BRICK, False)
		self.tiles[0x0199FF] = Tile(TEXTURE, CASTLE_1, False)
		self.tiles[0x0299FF] = Tile(TEXTURE, CASTLE_2, False)
		self.tiles[0x0399FF] = Tile(TEXTURE, CASTLE_3, True)
		self.tiles[0x0499FF] = Tile(TEXTURE, CASTLE_4, False)
		self.tiles[0x0599FF] = Tile(TEXTURE, CASTLE_5, False)
		self.tiles[0x0699FF] = Tile(TEXTURE, CASTLE_6, False)


		self.tiles[0x139932] = LayeredTile(TEXTURE, SKY, GRASS)

		for c in range(0x0F0000, 0x0F0002):
			self.tiles[c] = Tile(TEXTURE, SKY, True)
		self.tiles[0xFFFFFF] = Tile(TEXTURE, SKY, False)
		self.tiles[0xFFFF00] = Tile(TEXTURE, STONE_UNDERWORLD, False)
		self.nullTile = Tile(TEXTURE, BLOCK, False)

		"""
		-------------Overworld map Tiles-------------
		"""
		self.tiles[0x29B547] = ScaledTile(OVERWORLDMAP, BG)
		self.tiles[0xB7B7B7] = ScaledTile(OVERWORLDMAP, H_ROAD)
		self.tiles[0xB8B8B8] = ScaledTile(OVERWORLDMAP, V_ROAD)



	def getNullTile(self):
		return self.nullTile

	def getTile(self,color):
		return self.tiles[color]
