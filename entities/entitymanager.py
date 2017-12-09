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
from entities.projectiles.waterball import *

#items to pick up
from entities.pickup.shroom import *
from entities.pickup.fireflower import *
from entities.pickup.star import *
from entities.pickup.coin import *
from entities.pickup.coindrop import *

from constants import *

class EntityManager:
	def __init__ (self):
		# vær opmærksom på at pygame bruger BGR farver
		self.entities = [None]*(0xFFFFFF+1)
		self.entities[0x00C7FF] = Star(TEXTURE, STAR, 11,0,0, 60, 0.3, True)
		self.entities[0x0F0000] = Powerup(TEXTURE, POWERUP, 5,0,0, 60, 0.2, 0x020000)
		self.entities[0x0F0001] = Powerup(TEXTURE, POWERUP, 5,0,0, 60, 0.2, 0x01FFFF)
		self.entities[0x0F0002] = Powerup(TEXTURE, POWERUP, 5,0,0, 60, 0.2, 0x050000)
		self.entities[0x00FFFF] = Coin(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 0.1, True)
		self.entities[0x01FFFF] = Coindrop(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 0.4, True)

		#end flag
		self.entities[0xFF0000] = FlagPole(TEXTURE, 0, 0)
		self.entities[0xFF0100] = FlagTop(TEXTURE, 0, 0)

		#entity register [id1 - id2 - dir]
		#Balumba
		self.entities[0x010000] = Balumba(ENEMIES, BALUMBA, 2, 0, 0, 1, 0.1, 1)
		self.entities[0x010001] = Balumba(ENEMIES, BALUMBA, 2, 0, 0, 1, 0.1, -1)

		#Enlargen shroom
		self.entities[0x020000] = Shroom(TEXTURE, SHROOM, 2, 0, 0, 3, 0.08, True)

		#Legobro
		self.entities[0x030000] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 20, 0.08, False)
		self.entities[0x030001] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 20, 0.08, True)

		#Lego projectile
		self.entities[0x040000] = Lego(ENEMIES, LEGO, 4, 0, 0, 3, 0.16, True, False)
		self.entities[0x040001] = Lego(ENEMIES, LEGO, 4, 0, 0, 3, 0.16, True, True)

		#Flower
		self.entities[0x050000] = FireFlower(TEXTURE, FLOWER, 2, 0, 0, 3, 0.08, True)

		#Water bullet
		self.entities[0x060000] = Waterball(ENEMIES, WATER_DOWN, 1, 0, True)
		self.entities[0x060001] = Waterball(ENEMIES, WATER_DOWN, 1, 0, False)

	def getEntity(self,color):
		return self.entities[color]
