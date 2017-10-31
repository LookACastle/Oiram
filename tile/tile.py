class Tile:
	def __init__(self, id):
		self.id = id
		
	def render (self, screen, x, y):
		screen.drawSprite( 1, self.id, x, y)
		
		