from constants import *
from pausemenu.menuitem.baseobject import *

class SlideObject(BaseObject):
	def __init__(self, x, y, screen, margin, lowerlimit, upperlimit, initialvalue, title, dragaction):
		BaseObject.__init__(self)
		self.label = screen.font30.render(str(initialvalue), 1, (255,255,255))
		self.title = screen.font30.render(title, 1, (255,255,255))
		self.theight = self.title.get_height()/2
		self.twidth = self.title.get_width() + 20*SCALE
		self.lheight = self.label.get_height()/3
		self.width = 88*SCALE
		self.height = 12*SCALE
		self.x = x
		self.y = y
		self.margin = margin
		self.upper = upperlimit
		self.lower = lowerlimit
		self.valuewidth = self.upper - self.lower
		self.value = initialvalue
		self.mx = self.x
		self.setMarker(initialvalue)
		self.dragaction = dragaction

	def checkCollision(self, x, y):
		if (x + self.margin + self.twidth > self.x and x < self.x+self.width + self.margin + self.twidth and y + self.margin > self.y - self.margin/2 and y - self.margin/2 < self.y+self.height+self.margin): 
			return True
		return False

	def drag(self, x, y):
		value = int((((x - self.twidth)/self.width)+0.1)*(self.valuewidth))
		self.value = value + self.lower
		self.setMarker(value)

	def setMarker(self, value):
		self.mx = ((value)/self.valuewidth)*self.width - self.lower*SCALE
		if (self.mx < 0):
			self.mx = self.twidth + self.x
			self.value = self.lower
		elif (self.mx > self.width):
			self.mx = self.width - self.lower*SCALE + self.twidth + self.x
			self.value = self.upper
		else:
			self.mx +=  self.twidth + self.x

	def isPressAble(self):
		return True

	def isDragAble(self):
		return True

	def render(self, screen, x, y):
		self.label = screen.font30.render(str(self.value), 1, (255,255,255))
		self.lheight = self.label.get_height()/3
		cx = self.x + x
		cy = self.y + y
		screen.display.blit( self.title, (cx + 4*SCALE, cy ))
		screen.display.blit( self.label, (cx + self.width + 5*SCALE + self.twidth, cy - self.lheight + self.theight - 4*SCALE ))
		screen.drawGUISprite(MENU_SLIDE, MENU_ITEM, cx + self.twidth, cy + self.theight - 4*SCALE)
		screen.drawGUISprite(MENU_BUTTON, MENU_ITEM, x + self.mx - 3.5*SCALE, cy - 6*SCALE + self.theight - 4*SCALE)
		

		
		