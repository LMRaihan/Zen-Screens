#ZenScreens
import pygame
import sys

pygame.init()

screenWidth, screenHeight = 1000, 800
logoSpeed = [2, 2]
backgroundColor = (0, 0, 0)

#creating a Pygame screen with the specified dimensions
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Zen Screens") #window-screen

logo = pygame.image.load("x.jpg")
logo = pygame.transform.scale(logo, (200, 200))
logoRect = logo.get_rect() #rectangle object associated with "x"

#Create a Pygame clock object to control the frame rate
clock = pygame.time.Clock()

#QUIT handling loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

    screen.fill(backgroundColor) 
    #draw the logo image onto the screen at its current position.
    screen.blit(logo, logoRect) 
    # Move the logo rectangle by the specified speed       
    logoRect = logoRect.move(logoSpeed) 

  #Bounce the logo off the screen edges
    if logoRect.left < 0 or logoRect.right > screenWidth:
        logoSpeed[0] = -logoSpeed[0]
    if logoRect.top < 0 or logoRect.bottom > screenHeight:
        logoSpeed[1] = -logoSpeed[1]

  #the display to show the changes made during this iteration of the game loop.
    pygame.display.flip()
  # Adjust the frame rate as needed                              
    clock.tick(60)   
