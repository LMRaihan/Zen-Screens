#ZenScreens
import pygame
import sys
import os

def load_image(image_path, size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, size)

pygame.init()

screenWidth, screenHeight = 1000, 800
logoSpeed = [2, 2]
backgroundColor = (0, 0, 0)

# Get user-defined image path
image_path = input("Enter the path of the image: ")

# Specify the size of the image
image_size = (200, 200)

# Ensure the path is correct and load the image dynamically
if os.path.isfile(image_path):
    logo = load_image(image_path, image_size)
else:
    print(f"Error: The file '{image_path}' does not exist.")
    sys.exit()

#creating a Pygame screen with the specified dimensions
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Zen Screens") #window-screen

logoRect = logo.get_rect() # rectangle object associated with the image

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
