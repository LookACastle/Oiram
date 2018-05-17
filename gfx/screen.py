import pygame
from constants import *
from gfx.spritesheet import SpriteSheet

class Screen:
	def __init__(self, display):
		self.display = display
		self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_RES_HEIGHT)).convert_alpha()
		for x in range(0, int(SCREEN_WIDTH)):
			for y in range(0, int(SCREEN_HEIGHT)):
				self.overlay.set_at((x, y), (30,30,30,100))
		self.sheets = []
		self.xOffset = 0
		self.yOffset = 0
		#self.font = pygame.font.SysFont("monospace", 15)
		self.font70 = pygame.font.Font("gfx/DefaultFont.ttf", 70)
		self.font30 = pygame.font.Font("gfx/DefaultFont.ttf", 30)
		
		self.scale = SCALE

		for path in SPRITE_LIST:
			self.sheets.append(SpriteSheet(path))

	def rescale(self, newscale):
		self.scale = newscale
		for sheet in self.sheets:
			sheet.scale(newscale)

	def setOffset(self, x, y):
		self.xOffset = x
		self.yOffset = y

	def drawSprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), (x+self.xOffset, y+self.yOffset))

	def drawColouredFlippedSprite(self, id, tileId, x, y, flip, overlay, strength):
		sprite = pygame.transform.flip(self.sheets[id].getSprite(tileId), flip, False)
		pxarray = pygame.PixelArray(sprite)
		if (strength > 0):
			for px in range(0, int(sprite.get_width()/SCALE)):
				for py in range(0,int(sprite.get_height()/SCALE)):
					color = sprite.unmap_rgb(pxarray[px*SCALE, py*SCALE])
					if (color[3]  == 0xFF):
						cstrength = 1-strength
						r = color[0]*cstrength + overlay[0]*strength
						g = color[1]*cstrength + overlay[1]*strength
						b = color[2]*cstrength + overlay[2]*strength
						for sx in range(px*SCALE, px*SCALE + SCALE):
							for sy in range(py*SCALE, py*SCALE + SCALE):
								pxarray[sx, sy] = (r, g, b)
		#ns = pxarray.make_surface()
		del pxarray
		self.display.blit(sprite , (x+self.xOffset,y+self.yOffset))

	def drawRotateSprite(self, id, tileId, x, y, angle):
		self.display.blit(pygame.transform.rotate(self.sheets[id].getSprite(tileId), angle), (x+self.xOffset,y+self.yOffset))

	def drawFlippedSprite(self, id, tileId, x, y, flipx, flipy = False):
		self.display.blit(pygame.transform.flip(self.sheets[id].getSprite(tileId), flipx, flipy), (x+self.xOffset,y+self.yOffset))

	def drawScaledSprite(self, id, tileId, x, y, scale):
		self.display.blit(self.sheets[id].getScaledSprite(tileId, scale), (x+self.xOffset,y+self.yOffset))

	def drawScaledFlippedSprite(self, id, tileId, x, y, scale, flip):
		self.display.blit(pygame.transform.flip(self.sheets[id].getScaledSprite(tileId, scale), flip, False), (x+self.xOffset,y+self.yOffset))

	def writeText (self, txt, x, y):
		label = self.font70.render(txt, 1, (255,255,255))
		self.display.blit(label, (x, y))

	def drawScaledGUISprite(self, id, tileId, x, y, scale):
			self.display.blit(self.sheets[id].getScaledSprite(tileId, scale), (x,y))

	def drawGUISprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), (x, y))


	def drawOverlay(self):
		self.display.blit(self.overlay, (0, 0))
