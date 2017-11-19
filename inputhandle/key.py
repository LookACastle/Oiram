class Key:
	def __init__(self):
		self.pressed = False

	def toggle(self):
		self.pressed = not self.pressed

	def isPressed(self):
		return self.pressed