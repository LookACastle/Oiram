from constants import *
from pausemenu.menuitem.baseobject import *

class TextBox (BaseObject):
	def __init__(self, text, x, y, screen, size):
		BaseObject.__init__(self)
		if(size == 0):
			self.label = screen.fontlarge.render(text, 1, (255,255,255))
		if (size == 1):
			self.label = screen.fontsmall.render(text, 1, (255,255,255))
		self.size = size
		self.width = self.label.get_width()/screen.scale
		self.height = self.label.get_height()/screen.scale
		self.x = x
		self.y = y
		self.text = text

	def checkCollision(self, x, y):
		return False

	def center(self, width):
		difference = width-self.width
		self.x += difference/2

	def render(self, screen, x, y):
		if (self.size == 0):
			screen.writeLargeText(self.text,  self.x + x, self.y + y, (255,255,255))
		if (self.size == 1):
			screen.writeSmallText(self.text,  self.x + x, self.y + y, (255,255,255))
		

		