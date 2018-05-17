from pausemenu.menuitem.textobject import *
from constants import *

class MainMenu:
	def __init__(self, screen):
		options = ["Resume", "Options", "Quit"]
		actions = [resumeAction, optionAction, quitAction]
		self.objects = []
		y = 0
		maxwidth = 0
		for i in range(0, len(options)):
			textbox = TextObject(options[i], 45*SCALE, y + 30*SCALE, screen, 30, actions[i])
			if (textbox.width > maxwidth):
				maxwidth = textbox.width
			self.objects.append(textbox)
			y += 40*SCALE

		for o in self.objects:
			o.center(maxwidth)
	
	def resetHover(self):
		for o in self.objects:
			if (o.isHoverAble):
				o.hover = False

	def resetPress(self):
		for o in self.objects:
			if (o.isPressAble()):
				o.pressed = False

	def getCollision(self, x, y):
		collided = []
		for o in self.objects:
			if (o.checkCollision(x, y)):
				collided.append(o)
		return collided

	def render(self, screen, x, y):
		for o in self.objects:
			o.render(screen, x, y)

def quitAction(main):
	main.levelManager.changeLevel(main.player)
	main.pausemenu.active = False

def resumeAction(main):
	main.pausemenu.active = False

def optionAction(main):
	main.pausemenu.changeMenu("option")