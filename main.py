import pygame , time
pygame.init()
screenWidth, screenHeight = 1920, 1080
logoSpeed = [1, 1]
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((screenWidth,screenHeight))

logo = pygame.image.load("x.jpg")
logo = pygame.transform.scale(logo,(100,100))
logoRect = logo.get_rect()

while True:
  screen.fill(backgroundColor)

  screen.blit(logo,logoRect)
  logoRect = logoRect.move(logoSpeed)

  if logoRect.left < 0 or logoRect.right > screenWidth:
    logoSpeed[0] = -logoSpeed[0]
  if logoRect.top < 0 or logoRect.bottom > screenHeight:
    logoSpeed[1] = -logoSpeed[1]

  pygame.display.flip()
  time.sleep(10/1000)