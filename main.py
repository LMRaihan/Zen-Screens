#ZenScreens

import pygame
import sys
import os
import tkinter as tk
from tkinter import filedialog

def load_image(image_path, size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, size)

def browse_image_path():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

def configure_screensaver():
    global logo, logoRect, logoSpeed

    image_path = browse_image_path()
    if os.path.isfile(image_path):
        logo = load_image(image_path, image_size)
    else:
        print(f"Error: The file '{image_path}' does not exist.")
        return

    # Set screensaver speed
    speed_x = speed_x_var.get()
    speed_y = speed_y_var.get()
    logoSpeed = [speed_x, speed_y]

pygame.init()

screenWidth, screenHeight = 1000, 800
backgroundColor = (0, 0, 0)

# Default screensaver speed
default_speed = [2, 2]

# Create a Tkinter window for configuring screensaver settings
config_window = tk.Tk()
config_window.title("Zen Screensaver Settings")

# Browse button to select the image path
browse_button = tk.Button(config_window, text="Browse Image", command=configure_screensaver)
browse_button.pack()

# Speed sliders
speed_x_var = tk.IntVar(value=default_speed[0])
speed_y_var = tk.IntVar(value=default_speed[1])

speed_x_label = tk.Label(config_window, text="Speed X:")
speed_x_label.pack()
speed_x_slider = tk.Scale(config_window, from_=1, to=10, orient=tk.HORIZONTAL, variable=speed_x_var)
speed_x_slider.pack()

speed_y_label = tk.Label(config_window, text="Speed Y:")
speed_y_label.pack()
speed_y_slider = tk.Scale(config_window, from_=1, to=10, orient=tk.HORIZONTAL, variable=speed_y_var)
speed_y_slider.pack()

# Specify the size of the image
image_size = (200, 200)

# Initialize screensaver parameters
logo = None
logoSpeed = default_speed
logoRect = None

#creating a Pygame screen with the specified dimensions
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Zen Screens") #window-screen

# Initialize logoRect with the initial position
logoRect = pygame.Rect((screenWidth//2 - image_size[0]//2, screenHeight//2 - image_size[1]//2), image_size)

#Create a Pygame clock object to control the frame rate
clock = pygame.time.Clock()

#QUIT handling loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

    screen.fill(backgroundColor) 

    if logo:
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

    config_window.update_idletasks()
    config_window.update()
