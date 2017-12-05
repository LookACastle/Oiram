#base entities
from entities.entity import Entity
from entities.animatedmob import *

#blocks
from entities.blocks.powerup import *

#end flags
from entities.flags.flagpole import *
from entities.flags.flagtop import *

#enemies
from entities.enemies.balumba import *
from entities.enemies.legobro import *

#projectile entities
from entities.projectiles.lego import *

#items to pick up
from entities.pickup.shroom import *
from entities.pickup.star import *
from entities.pickup.coin import *
from entities.pickup.coindrop import *

from constants import *

class EntityManager:
	def __init__ (self):
		# vær opmærksom på at pygame bruger BGR farver
		self.entities = [None]*(0xFFFFFF+1)
		self.entities[0x00C7FF] = Star(TEXTURE, STAR, 11,0,0, 60, 3, True)

		self.entities[0x0F0000] = Powerup(TEXTURE, POWERUP, 5,0,0, 180, 9, 0x020000)
		self.entities[0x0F0001] = Powerup(TEXTURE, POWERUP, 5,0,0, 180, 9, 0x01FFFF)

		self.entities[0x00FFFF] = Coin(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 2, True)
		self.entities[0x01FFFF] = Coindrop(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 2, True)

		#end flag
		self.entities[0xFF0000] = FlagPole(TEXTURE, 0, 0)
		self.entities[0xFF0100] = FlagTop(TEXTURE, 0, 0)

		#entity register [dir - id2 - id]
		self.entities[0x010000] = Balumba(ENEMIES, GUMBA, 2, 0, 0, 1, 3, 1)
		self.entities[0x010001] = Balumba(ENEMIES, GUMBA, 2, 0, 0, 1, 3, -1)
		self.entities[0x020000] = Shroom(TEXTURE, SHROOM, 2, 0, 0, 3, 8, True)
		self.entities[0x030000] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 60, 20, False)
		self.entities[0x030001] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 60, 20, True)
		self.entities[0x040000] = Lego(ENEMIES, LEGO, 4, 0, 0, 3, 8, True, False)
		self.entities[0x040001] = Lego(ENEMIES, LEGO, 4, 0, 0, 3, 8, True, True)

	def getEntity(self,color):
		return self.entities[color]
