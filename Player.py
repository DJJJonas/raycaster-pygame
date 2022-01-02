from pygame.math import Vector2
class Player:
	def __init__(self, pos, camera):
		self.pos = Vector2(pos[0], pos[1])
		self.mapPos = Vector2(int(pos[0]), int(pos[1]))
		self.camera = camera

	def move(self, dir):
		self.pos += dir
		self.mapPos.x = int(self.pos.x)
		self.mapPos.y = int(self.pos.y)

	def rotate(self, ang):
		self.camera.dir = self.camera.dir.rotate_rad(ang)
		self.camera.plane = self.camera.plane.rotate_rad(ang)