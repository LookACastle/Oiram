#base entities
from entities.entity import Entity
from entities.animatedmob import *

#end flags
from entities.flags.flagpole import *
from entities.flags.flagtop import *

#enemies
from entities.enemies.balumba import *
from entities.enemies.legobro import *

#projectile entities
from entities.projectiles.hammer import *

#items to pick up
from entities.pickup.shroom import *
from entities.pickup.star import *
from entities.pickup.coin import *
from constants import *

class EntityManager:
	def __init__ (self):
		# vær opmærksom på at pygame bruger BGR farver
		self.entities = [None]*(0xFFFFFF+1)
		self.entities[0x00C7FF] = Star(TEXTURE, STAR, 11,0,0, 60, 0.3, True)
		self.entities[0xFF00FF] = animatedMob(TEXTURE, POWERUP, 5,0,0, 60, 0.3, True)
		self.entities[0x00FFFF] = Coin(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 0.1, True)

		#end flag
		self.entities[0xFF0000] = FlagPole(TEXTURE, 0, 0)
		self.entities[0xFF0100] = FlagTop(TEXTURE, 0, 0)

		#entity register [dir - id2 - id]
		self.entities[0x010000] = Balumba(ENEMIES, GUMBA, 2, 0, 0, 1, 0.1, 1)
		self.entities[0x010001] = Balumba(ENEMIES, GUMBA, 2, 0, 0, 1, 0.1, -1)
		self.entities[0x020000] = Shroom(TEXTURE, SHROOM, 2, 0, 0, 3, 0.08, True)
		self.entities[0x030000] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 20, 0.08, False)
		self.entities[0x030001] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 20, 0.08, True)
		self.entities[0x040000] = Hammer(ENEMIES, LEGO, 4, 0, 0, 3, 0.08, True, False)
		self.entities[0x040001] = Hammer(ENEMIES, LEGO, 4, 0, 0, 3, 0.08, True, True)

	def getEntity(self,color):
		return self.entities[color]
