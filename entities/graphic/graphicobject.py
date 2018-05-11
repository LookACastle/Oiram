from constants import TPS
class GraphicObject():
	def __init__(self, sheet, id, x, y, width, height, fixed, scale):
		self.id = id
		self.sheet = sheet
		self.x = x
		self.y = y
		self.vy = -1
		self.fixed = fixed
		self.visible = True
		self.scale = scale
		self.collision = False
		self.solid = False
		self.dead = False
		self.width = width
		self.height = height
		self.lifetime = TPS*2

	def clone(self, x, y):
		return GraphicObject(self.sheet, self.id, x, y, self.width, self.height, self.fixed, self.scale)

	def tick(self, level):
		self.lifetime -= 1
		self.y += self.vy
		self.vy *= 0.98
		if (self.lifetime == 0):
			self.dead = True

	def render (self, screen):
		if (self.fixed):
			screen.drawScaledGUISprite(self.sheet, self.id, self.x, self.y, self.scale)
		else:
			screen.drawScaledSprite( self.sheet, self.id, self.x, self.y, self.scale)

		