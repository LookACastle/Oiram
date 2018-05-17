class BaseObject:
	def __init__(self):
		self.pressed = False
		self.action = None
	
	def isPressAble(self):
		return False

	def isHoverAble(self):
		return False

	def isDragAble(self):
		return False

		