import pygame
from constants import *
from gfx.spritesheet import SpriteSheet
class Screen:
	def __init__(self):
		self.display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
		self.sheets = []
		for path in SPRITE_LIST:
			self.sheets.append(SpriteSheet(path))

	def drawSprite(self, id, tileId, x, y):
		pass