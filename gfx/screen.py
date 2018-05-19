import pygame
from constants import *
from gfx.spritesheet import SpriteSheet

class Screen:
	def __init__(self, display, width, height, scale):
		self.display = display

		self.sheets = []
		self.xOffset = 0
		self.yOffset = 0

		self.scale = scale

		self.width = width
		self.height = height

		#self.font = pygame.font.SysFont("monospace", 15)
		self.fontlarge = pygame.font.Font("gfx/DefaultFont.ttf", 20*self.scale)
		self.fontsmall = pygame.font.Font("gfx/DefaultFont.ttf", 10*self.scale)
	
		for path in SPRITE_LIST:
			self.sheets.append(SpriteSheet(path, self.scale))

	def rescale(self, newscale):
		self.scale = newscale
		self.fontlarge = pygame.font.Font("gfx/DefaultFont.ttf", 20*self.scale)
		self.fontsmall = pygame.font.Font("gfx/DefaultFont.ttf", 10*self.scale)
		for sheet in self.sheets:
			sheet.scale(newscale)

	def setOffset(self, x, y):
		self.xOffset = x
		self.yOffset = y

	def drawSprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), ((x+self.xOffset)*self.scale, (y+self.yOffset)*self.scale))

	def drawColouredFlippedSprite(self, id, tileId, x, y, flip, overlay, strength):
		sprite = pygame.transform.flip(self.sheets[id].getSprite(tileId), flip, False)
		pxarray = pygame.PixelArray(sprite)
		if (strength > 0):
			for px in range(0, int(sprite.get_width()/self.scale)):
				for py in range(0,int(sprite.get_height()/self.scale)):
					color = sprite.unmap_rgb(pxarray[px*self.scale, py*self.scale])
					if (color[3]  == 0xFF):
						cstrength = 1-strength
						r = color[0]*cstrength + overlay[0]*strength
						g = color[1]*cstrength + overlay[1]*strength
						b = color[2]*cstrength + overlay[2]*strength
						for sx in range(px*self.scale, px*self.scale + self.scale):
							for sy in range(py*self.scale, py*self.scale + self.scale):
								pxarray[sx, sy] = (r, g, b)
		#ns = pxarray.make_surface()
		del pxarray
		self.display.blit(sprite , ((x+self.xOffset)*self.scale,(y+self.yOffset)*self.scale))

	def drawRotateSprite(self, id, tileId, x, y, angle):
		self.display.blit(pygame.transform.rotate(self.sheets[id].getSprite(tileId), angle), ((x+self.xOffset)*self.scale,(y+self.yOffset)*self.scale))

	def drawFlippedSprite(self, id, tileId, x, y, flipx, flipy = False):
		self.display.blit(pygame.transform.flip(self.sheets[id].getSprite(tileId), flipx, flipy), ((x+self.xOffset)*self.scale,(y+self.yOffset)*self.scale))

	def drawScaledSprite(self, id, tileId, x, y, scale):
		self.display.blit(self.sheets[id].getScaledSprite(tileId, scale), ((x+self.xOffset)*self.scale,(y+self.yOffset)*self.scale))

	def drawScaledFlippedSprite(self, id, tileId, x, y, scale, flip):
		self.display.blit(pygame.transform.flip(self.sheets[id].getScaledSprite(tileId, scale), flip, False), ((x+self.xOffset)*self.scale,(y+self.yOffset)*self.scale))

	def writeLargeText (self, txt, x, y, c = (255,255,255)):
		label = self.fontlarge.render(txt, 1, c)
		self.display.blit(label, (x*self.scale, y*self.scale))

	def writeSmallText (self, txt, x, y, c = (255,255,255)):
		label = self.fontsmall.render(txt, 1, c)
		self.display.blit(label, (x*self.scale, y*self.scale))

	def drawScaledGUISprite(self, id, tileId, x, y, scale):
		self.display.blit(self.sheets[id].getScaledSprite(tileId, escale), (x*self.scale, y*self.scale))

	def drawGUISprite(self, id, tileId, x, y):
		self.display.blit(self.sheets[id].getSprite(tileId), (x*self.scale, y*self.scale))

	def renderOverlay(self):
		self.overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
		self.overlay.fill((10,10,10,100))
		
	def drawOverlay(self):
		self.display.blit(self.overlay , (0,0))
		
