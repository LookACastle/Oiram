from pausemenu.menuitem.slideobject import *
from pausemenu.menuitem.button import *
from constants import *

class OptionMenu:
	def __init__(self, screen, configManager):
		#slider param
		# x, y, screen, margin, lowerlimit, upperlimit, initialvalue, title, dragaction
		#SlideObject( 20, 40, screen, 2, 20, 120, 60, "tps", speedAction)
		self.objects = [
		SlideObject( 20, 20, screen, 2, 1, 4, configManager.getGraphicInt("scale"), "scale", scaleAction),
		SlideObject( 20, 40, screen, 2, 20, 120, configManager.getGraphicInt("tps"), "tps", speedAction),
		SlideObject( 20, 60, screen, 2, 10, 120, configManager.getLevelInt("x_tile_count"), "tile x", xdrawAction),
		SlideObject( 20, 80, screen, 2, 10, 66, configManager.getLevelInt("y_tile_count"), "tile y", ydrawAction),
		Button("back", 0, 120, screen, 2, backAction, 0)
		]
		self.objects[4].center(200)

	def resetHover(self):
		for o in self.objects:
			if (o.isHoverAble):
				o.hover = False

	def updatefont():
		for o in self.objects:
			o.updatefont()

	def getCollision(self, x, y):
		collided = []
		for o in self.objects:
			if (o.checkCollision(x, y)):
				collided.append(o)
		return collided

	def resetPress(self):
		for o in self.objects:
			if (o.isPressAble()):
				o.pressed = False

	def render(self, screen, x, y):
		for o in self.objects:
			o.render(screen, x, y)

def scaleAction(main, dragged):
	main.rescaleDislpay(dragged.value)

def speedAction(main, dragged):
	main.tps = dragged.value

def xdrawAction(main, dragged):
	main.levelManager.horizontaltilecount = dragged.value
	main.resizeDisplay()

def ydrawAction(main, dragged):
	main.levelManager.verticaltaltilecount = dragged.value
	main.resizeDisplay()

def backAction(main):
	main.pausemenu.changeMenu("main")