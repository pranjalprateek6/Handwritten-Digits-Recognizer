import pygame
from main import *
from PIL import Image

pygame.init()
BLUE = (255,255,255)
RED = (255, 0, 0)
isPressed = False
pygame.display.set_caption('Digits Recogniztion')
hmm = pygame.font.SysFont("Arial", 30)
res = pygame.font.SysFont("Arial", 60)

screen = pygame.display.set_mode((600,250))
clock = pygame.time.Clock()
rect = pygame.Rect(0, 0, 250, 250)
sub = screen.subsurface(rect)


def drawText(text, font, textColor, x, y):
	img = font.render(text, True, textColor)
	screen.blit(img, (x, y))
def drawTextResult(text, font, textColor, x, y):
	img = font.render(text, True, textColor)
	screen.blit(img, (x, y))

def drawCircle(screen,x,y):
  pygame.draw.circle(screen,BLUE,(x,y),5)
def clear():
	screen.fill((0,0,0))
	pygame.display.flip()
run = True
while run:
	for event in pygame.event.get():

		(x,y) = pygame.mouse.get_pos()
		if x < 250 and y < 250 :
			if event.type == pygame.MOUSEBUTTONDOWN:
				isPressed = True
			elif event.type == pygame.MOUSEBUTTONUP:
				isPressed = False
			if event.type == pygame.MOUSEMOTION and isPressed == True:
				(x,y) = pygame.mouse.get_pos()
				drawCircle(screen,x,y)

		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pygame.image.save(sub, "screenshot.png")
			if event.key == pygame.K_RIGHT:
				clear()
			if event.key == pygame.K_UP:
				image = Image.open('screenshot.png')
				new_image = image.resize((28, 28))
				new_image.save('screenshot.png')
				img2 = cv2.imread('screenshot.png')[:,:,0]
				img2 = np.array([img2])
				plt.imshow(img2[0], cmap=plt.cm.binary)
				plt.show()
				text = str(predict([img2]))
				drawTextResult(text, res, RED, 300,75)
		drawText("Digits is : ", hmm, BLUE, 300,50)


	pygame.display.flip()
