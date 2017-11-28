#base entities
from entities.entity import Entity
from entities.animatedmob import *

#end flags
from entities.flags.flagpole import *
from entities.flags.flagtop import *

#enemies
from entities.enemies.gumba import *
from entities.enemies.hammerbro import *

#projectile entities
from entities.projectiles.hammer import *

#items to pick up
from entities.pickup.shroom import *
from entities.pickup.star import *
from constants import *

class EntityManager:
	def __init__ (self):
		# vær opmærksom på at pygame bruger BGR farver
		self.entities = [None]*(0xFFFFFF+1)
		self.entities[0x00C7FF] = Star(TEXTURE, STAR, 11,0,0, 60, 0.3, True)
		self.entities[0xFF00FF] = animatedMob(TEXTURE, POWERUP, 5,0,0, 60, 0.3, True)
		self.entities[0x00FFFF] = animatedMob(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 0.1, True)

		#end flag
		self.entities[0xFF0000] = FlagPole(TEXTURE, 0, 0)
		self.entities[0xFF0100] = FlagTop(TEXTURE, 0, 0)

		#entity register [dir - id2 - id]
		self.entities[0x000001] = Gumba(ENEMIES, GUMBA, 2, 0, 0, 1, 0.1, 1)
		self.entities[0x100001] = Gumba(ENEMIES, GUMBA, 2, 0, 0, 1, 0.1, -1)
		self.entities[0x000002] = Shroom(TEXTURE, SHROOM, 2, 0, 0, 3, 0.08, True)
		self.entities[0x000003] = Hammerbro(LARGENEMIES, HAMMERBRO, 4, 0, 0, 20, 0.08, False)
		self.entities[0x000103] = Hammerbro(LARGENEMIES, HAMMERBRO, 4, 0, 0, 20, 0.08, True)
		self.entities[0x000004] = Hammer(ENEMIES, LEGO, 4, 0, 0, 3, 0.08, True, False)
		self.entities[0x000104] = Hammer(ENEMIES, LEGO, 4, 0, 0, 3, 0.08, True, True)

	def getEntity(self,color):
		return self.entities[color]
