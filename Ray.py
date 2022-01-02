from pygame.math import Vector2
from math import inf as infinity
from gamemap import gamemap

class Ray:
	def __init__(self, pos, rayDir):
		try:
			self.deltaDistX = abs(1/rayDir.x)
		except ZeroDivisionError:
			self.deltaDistX = infinity
		try:
			self.deltaDistY = abs(1/rayDir.y)
		except ZeroDivisionError:
			self.deltaDistY = infinity

		mapPos = Vector2(int(pos.x), int(pos.y))

		self.distToSideX = 0
		self.distToSideY = 0

		self.stepX = 0
		self.stepY = 0

		if (rayDir.x < 0):
			self.distToSideX = (pos.x - mapPos.x) * self.deltaDistX
			self.stepX = -1
		else:
			self.distToSideX = (mapPos.x + 1 - pos.x) * self.deltaDistX
			self.stepX = +1

		if (rayDir.y < 0):
			self.distToSideY = (pos.y - mapPos.y) * self.deltaDistY
			self.stepY = -1
		else:
			self.distToSideY = (mapPos.y + 1 - pos.y) * self.deltaDistY
			self.stepY = +1

		self.hit = False

		self.ddaLineSizeX = self.distToSideX
		self.ddaLineSizeY = self.distToSideY

		self.wallMapPos = Vector2(mapPos.x, mapPos.y)

		self.hitSide = 0
		self.hittedWall = 0

		while self.hit == False:
			if self.ddaLineSizeX < self.ddaLineSizeY:
				self.wallMapPos.x += self.stepX
				self.ddaLineSizeX += self.deltaDistX
				self.hitSide = 0
			else:
				self.wallMapPos.y += self.stepY
				self.ddaLineSizeY += self.deltaDistY
				self.hitSide = 1

			if gamemap [ int(self.wallMapPos.y) ] [ int(self.wallMapPos.x) ] > 0:
				self.hit = True
				self.hittedWall = gamemap [ int(self.wallMapPos.y) ] [ int(self.wallMapPos.x) ]

		if self.hitSide == 0:
			self.euclideanDist = abs(self.wallMapPos.x - pos.x + ((1-self.stepX)/2)*rayDir.magnitude())/rayDir.x
			self.perpendicularDist = abs(self.wallMapPos.x - pos.x + ((1-self.stepX)/2))/rayDir.x
		else:
			self.euclideanDist = abs(self.wallMapPos.y - pos.y + ((1-self.stepY)/2)*rayDir.magnitude())/rayDir.y
			self.perpendicularDist = abs(self.wallMapPos.y - pos.y + ((1-self.stepY)/2))/rayDir.y
