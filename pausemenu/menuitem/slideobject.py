from constants import *
from pausemenu.menuitem.baseobject import *

class SlideObject(BaseObject):
	def __init__(self, x, y, screen, margin, lowerlimit, upperlimit, initialvalue, title, dragaction):
		BaseObject.__init__(self)
		self.screen = screen
		self.titletxt = title
		self.label = screen.fontsmall.render(str(initialvalue), 1, (255,255,255))
		self.title = screen.fontsmall.render(self.titletxt, 1, (255,255,255))
		self.theight = self.title.get_height()/2/screen.scale
		self.twidth = self.title.get_width()/screen.scale + 20
		self.lheight = self.label.get_height()/3/screen.scale
		self.width = 88
		self.height = 12
		self.x = x
		self.y = y
		self.margin = margin
		self.upper = upperlimit
		self.lower = lowerlimit
		self.valuewidth = self.upper - self.lower
		self.value = initialvalue
		self.mx =(self.value-self.lower)*(self.width/self.valuewidth)
		self.dragaction = dragaction

	def checkCollision(self, x, y):
		if (x + self.margin > self.x + 48 and x < self.x + self.width + self.margin + 52 and y + self.margin > self.y - self.margin/2 and y - self.margin/2 < self.y+self.height+self.margin): 
			return True
		return False

	def drag(self, x, y):
		value = int(((x-71)/self.width + 1/self.valuewidth/2)*self.valuewidth)
		newvalue = value + self.lower
		if (newvalue != self.value):
			self.value = newvalue
			self.setMarker(value)

	def setMarker(self, value):
		self.mx = ((value)/self.valuewidth)*self.width
		if (self.mx < 0):
			self.mx = 0
			self.value = self.lower
		elif (self.mx > self.width):
			self.mx = self.width
			self.value = self.upper

	def isPressAble(self):
		return True

	def isDragAble(self):
		return True

	def render(self, screen, x, y):
		self.label = screen.fontsmall.render(str(self.value), 1, (255,255,255))
		self.title = screen.fontsmall.render(self.titletxt, 1, (255,255,255))
		self.theight = self.title.get_height()/2/screen.scale
		self.twidth = self.title.get_width()/screen.scale + 20
		self.lheight = self.label.get_height()/3/screen.scale
		cx = self.x + x
		cy = self.y + y
		screen.display.blit( self.title, ((cx + 4)*screen.scale, cy*screen.scale ))
		screen.display.blit( self.label, ((x + self.width + 76)*screen.scale, (cy - self.lheight + self.theight - 4)*screen.scale ))
		screen.drawGUISprite(MENU_SLIDE, MENU_ITEM, x + 70, cy + self.theight - 4)
		screen.drawGUISprite(MENU_BUTTON, MENU_ITEM, x + 70 + self.mx - 2, cy - 6 + self.theight - 4)
		

		
		