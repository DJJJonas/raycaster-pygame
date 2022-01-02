import pygame
from Ray import Ray
from Player import Player
from Camera import Camera

pygame.init()

size = WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pseudo 3D")

player = Player( (6, 6), Camera((0, -1), (0.66, 0)) )

clock = pygame.time.Clock()
text = pygame.font.SysFont("arial", 10)

ray = Ray(player.pos, player.camera.dir)

while True:
	fps = clock.tick(60)
	#	EVENTS
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			# Key events
			if event.key == pygame.K_ESCAPE:
				exit()

	#	KEYS
	if pygame.key.get_pressed()[pygame.K_w]:
		player.move(player.camera.dir/10)
	if pygame.key.get_pressed()[pygame.K_a]:
		player.move(player.camera.dir.rotate(-90)/10)
	if pygame.key.get_pressed()[pygame.K_s]:
		player.move(player.camera.dir/-10)
	if pygame.key.get_pressed()[pygame.K_d]:
		player.move(player.camera.dir.rotate(90)/10)
	if pygame.key.get_pressed()[pygame.K_q]:
		player.rotate(-0.03)
	if pygame.key.get_pressed()[pygame.K_e]:
		player.rotate(0.03)
	if pygame.key.get_pressed()[pygame.K_1]:
		command = input("Command: ")
		print(command)

	#	BACKGROUNDS
	screen.fill((190, 190, 255))
	pygame.draw.rect(screen, (130,130,130), (0, HEIGHT/2, WIDTH, HEIGHT))

	#	RAY SHOOTS
	for pixel in range(WIDTH+1):
		multiplier = 2 * (pixel/WIDTH) -1
		cameraPixel = player.camera.plane * multiplier

		rayDir = player.camera.dir + cameraPixel

		ray = Ray(player.pos, rayDir)
		#	WALL LINES

		wallLineHeight = HEIGHT/ray.perpendicularDist

		lineStartY = HEIGHT/2 - wallLineHeight/2
		lineEndY = HEIGHT/2 + wallLineHeight/2
		r=0
		g=0
		b=0

		if ray.hittedWall == 1:
			r=250;g=250;b=250
		elif ray.hittedWall == 2:
			r=0;g=250;b=0
		elif ray.hittedWall == 3:
			r=250;g=250;b=0
		elif ray.hittedWall == 4:
			r=0;g=0;b=250
		if ray.hitSide == 0:
			r -= r*0.10;g -= g*0.10;b -= b*0.10

		pygame.draw.line(screen, (r, g, b), (pixel, lineStartY), (pixel, lineEndY))

	pygame.display.flip()