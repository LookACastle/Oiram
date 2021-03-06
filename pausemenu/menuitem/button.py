from constants import *
from pausemenu.menuitem.baseobject import *

class Button (BaseObject):
	def __init__(self, text, x, y, screen, margin, action, size):
		BaseObject.__init__(self)
		if(size == 0):
			self.label = screen.fontlarge.render(text, 1, (255,255,255))
		if (size == 1):
			self.label = screen.fontsmall.render(text, 1, (255,255,255))
		self.size = size
		self.hover = False
		self.width = self.label.get_width()/screen.scale
		self.height = self.label.get_height()/screen.scale
		self.x = x
		self.y = y
		self.margin = margin
		self.text = text
		self.action = action

	def checkCollision(self, x, y):
		if (x + self.margin > self.x and x < self.x+self.width + self.margin and y + self.margin > self.y and y < self.y+self.height+self.margin): 
			return True
		return False

	def isPressAble(self):
		return True

	def isHoverAble(self):
		return True

	def center(self, width):
		difference = width-self.width
		self.x += difference/2

	def render(self, screen, x, y):
		if (self.hover):
			if (self.size == 0):
				screen.writeLargeText(self.text,  self.x + x + 2, self.y + y + 4, (100,100,100))
			if (self.size == 1):
				screen.writeSmallText(self.text,  self.x + x + 2, self.y + y + 4, (100,100,100))
		if (self.size == 0):
			screen.writeLargeText(self.text,  self.x + x, self.y + y, (255,255,255))
		if (self.size == 1):
			screen.writeSmallText(self.text,  self.x + x, self.y + y, (255,255,255))
		

		