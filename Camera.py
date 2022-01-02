from pygame.math import Vector2
class Camera:
	def __init__(self, dir, plane):
		self.dir = Vector2(0, -1)
		self.plane = Vector2(0.66, 0)