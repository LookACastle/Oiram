#base entities
from entities.entity import Entity
from entities.animatedmob import *

#blocks
from entities.blocks.powerup import *
from entities.blocks.brick import *
from entities.blocks.coinbrick import *
from entities.blocks.basetube import *

#end flags
from entities.flags.checkpoint import *
from entities.flags.flagpole import *
from entities.flags.flagtop import *

#enemies
from entities.enemies.balumba import *
from entities.enemies.legobro import *
from entities.enemies.spikey import *
from entities.enemies.shelly import *

#projectile entities
from entities.projectiles.lego import *
from entities.projectiles.waterball import *
from entities.projectiles.brickfragment import *
from entities.projectiles.shell import *

#items to pick up
from entities.pickup.shroom import *
from entities.pickup.lifeshroom import *
from entities.pickup.fireflower import *
from entities.pickup.star import *
from entities.pickup.coin import *
from entities.pickup.coindrop import *
from entities.pickup.spring import *

#interceptors
from entities.interceptor.fireghost import *

#graphics
from entities.graphic.graphicobject import *


from constants import *

class EntityManager:
	def __init__ (self):
		# vær opmærksom på at pygame bruger BGR farver
		self.entities = [None]*(0xFFFFFF+1)
		self.entities[0x00C7FF] = Star(TEXTURE, STAR, 11,0,0, 60, 0.3, True)
		self.entities[0x0F0000] = Powerup(TEXTURE, POWERUP, 5,0,0, 60, 0.2, 0x020000, BLOCK)
		self.entities[0x0F0002] = Powerup(TEXTURE, POWERUP, 5,0,0, 60, 0.2, 0x050000, BLOCK)
		self.entities[0x0F0003] = Powerup(TEXTURE, POWERUP, 5,0,0, 60, 0.2, None, BLOCK)
		self.entities[0x0F0004] = Powerup(TEXTURE, POWERUP, 5,0,0, 60, 0.2, 0x00C7FF, BLOCK)
		self.entities[0x0F0005] = Powerup(TEXTURE, SKY, 5,0,0, 60, 0.2, 0x020001, BLOCK)
		self.entities[0x0F0006] = Powerup(TEXTURE, SKY, 5,0,0, 60, 0.2, None, BLOCK)
		
		self.entities[0x0F0100] = Brick(TEXTURE, BRICK,0,0)
		self.entities[0x0F0200] = CoinBrick(TEXTURE, BRICK,0,0)
		self.entities[0x00FFFF] = Coin(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 0.1, True)
		self.entities[0x01FFFF] = Coindrop(TEXTURE, COIN_FLIP_ANIMATION, 8,0,0, 0, 0.4, True)

		#Tubes
		self.entities[0x346800] = BaseTube(TUBES, TOPTUBE, 0, 0, 2, 1)
		self.entities[0x10D080] = BaseTube(TUBES, BASETUBE, 0, 0, 2, 1)
		
		#end flag
		self.entities[0xFF0002] = Checkpoint(TEXTURE, WIN_FLAG_2,0,0)
		self.entities[0xFF0000] = FlagPole(TEXTURE, 0, 0)
		self.entities[0xFF0100] = FlagTop(TEXTURE, 0, 0)

		#entity register [id1 - id2 - dir]
		#Balumba
		self.entities[0x010000] = Balumba(ENEMIES, BALUMBA, 2, 0, 0, 1, 0.1, 1)
		self.entities[0x010001] = Balumba(ENEMIES, BALUMBA, 2, 0, 0, 1, 0.1, -1)

		#Enlargen shroom
		self.entities[0x020000] = Shroom(TEXTURE, SHROOM, 2, 0, 0, 3, 0.08, True)
		self.entities[0x020001] = LifeShroom(TEXTURE, SHROOM_HP, 2, 0, 0, 3, 0.08, True)

		#Legobro
		self.entities[0x030000] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 20, 0.08, False)
		self.entities[0x030001] = Legobro(LARGENEMIES, LEGOBRO, 4, 0, 0, 20, 0.08, True)

		#Lego projectile
		self.entities[0x040000] = Lego(ENEMIES, LEGO, 4, 0, 0, 3, 0.16, True, False)
		self.entities[0x040001] = Lego(ENEMIES, LEGO, 4, 0, 0, 3, 0.16, True, True)

		#Flower
		self.entities[0x050000] = FireFlower(TEXTURE, FLOWER, 2, 0, 0, 3, 0.08, True)

		#Water bullet
		self.entities[0x060000] = Waterball(ENEMIES, WATER_DOWN, 0, 0, True)
		self.entities[0x060001] = Waterball(ENEMIES, WATER_DOWN, 0, 0, False)

		#Spikey
		self.entities[0x070000] = Spikey(ENEMIES, SPIKE, 2, 0, 0, 1, 0.1, 1)
		self.entities[0x070001] = Spikey(ENEMIES, SPIKE, 2, 0, 0, 1, 0.1, -1)

		#fire ghost
		self.entities[0x080000] = FireGhost(ENEMIES, FIRE_GHOST, 0, 0)

		#Pickups
		self.entities[0x290CFF] = Spring(ENEMIES, SPRING, 5, 0, 0, 0.25)
		self.entities[0x539631] = Shell(ENEMIES, GREEN_SHELL, 1, 0, 10, 1, 1)

		#brick fragments
		self.entities[0x090000] = BrickFragment(FRAGMENTS, FULL, 0, 0)
		self.entities[0x090001] = BrickFragment(FRAGMENTS, LEFT_TOP, 0, 0)
		self.entities[0x090002] = BrickFragment(FRAGMENTS, TOP, 0, 0)
		self.entities[0x090003] = BrickFragment(FRAGMENTS, HALF, 0, 0)
		self.entities[0x090004] = BrickFragment(FRAGMENTS, HALF_WIDE, 0, 0)

		#Shelly
		self.entities[0x0A0000] = Shelly(LARGENEMIES, GREEN_SHELLY, 2, 0, 0, 1, 0.1, 1, 0x539631)
		self.entities[0x0A0001] = Shelly(LARGENEMIES, GREEN_SHELLY, 2, 0, 0, 1, 0.1, -1, 0x539631)

		#Graphics
		self.entities[0xFF00FF] = GraphicObject(ONEUP, ONEUP_TEXT, 0, 0, 2.9, 0.5, False, 2)

	def getEntity(self,color):
		return self.entities[color]
