from pausemenu.menuitem.slideobject import *
from constants import *

class OptionMenu:
	def __init__(self, screen):
		#slider param
		#x, y, screen, margin, lowerlimit, upperlimit, initialvalue, title
		self.objects = [
		SlideObject( 20*SCALE, 0, screen, 2, 1, 4, 3, "scale", scaleAction)
		]

	def resetHover(self):
		for o in self.objects:
			if (o.isHoverAble):
				o.hover = False

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