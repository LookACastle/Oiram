from pausemenu.menuitem.textobject import *
from constants import *

class MainMenu:
	def __init__(self, x, y, screen):
		self.x = x
		self.y = y
		options = ["Resume", "Options", "Quit"]
		self.objects = []
		y = 0
		for t in options:
			self.objects.append(TextObject(t, self.x + 45*SCALE,self.y + y + 30*SCALE, screen))
			y += 40*SCALE
		
	def checkCollision(self, x, y):
		for o in self.objects:
			o.checkCollision(x, y)

	def render(self, screen, x, y):
		for o in self.objects:
			o.render(screen, x, y)
		