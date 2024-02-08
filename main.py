import pygame
import sys
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

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

    # Hide the configuration window after completing the configuration
    config_window.withdraw()

    # Show the Zen Screen
    show_zen_screen()

def show_zen_screen():
    global logo, logoRect, logoSpeed
    
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

# Pygame initialization
pygame.init()

screenWidth, screenHeight = 1000, 800
backgroundColor = (0, 0, 0)

# Default screensaver speed
default_speed = [2, 2]

# Create a Tkinter window for configuring screensaver settings
config_window = tk.Tk()
config_window.title("Zen Screensaver Settings")

# Configure the style of the GUI elements
style = ttk.Style()
style.theme_use("clam")  # Change to any theme you like
style.configure('TButton', background='#4CAF50', foreground='white')
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0')

# Frame for the image selection
image_frame = ttk.Frame(config_window)
image_frame.pack(pady=10)

# Browse button to select the image path
browse_button = ttk.Button(image_frame, text="Browse Image", command=configure_screensaver)
browse_button.pack(side=tk.LEFT, padx=10)

# Label to display selected image path
selected_image_label = ttk.Label(image_frame, text="No image selected")
selected_image_label.pack(side=tk.LEFT)

# Speed sliders frame
speed_frame = ttk.Frame(config_window)
speed_frame.pack(pady=10)

# Speed sliders
speed_x_var = tk.IntVar(value=default_speed[0])
speed_y_var = tk.IntVar(value=default_speed[1])

speed_x_label = ttk.Label(speed_frame, text="Speed X:")
speed_x_label.grid(row=0, column=0, padx=5, pady=5)
speed_x_entry = ttk.Entry(speed_frame, textvariable=speed_x_var)
speed_x_entry.grid(row=0, column=1, padx=5, pady=5)
speed_x_slider = ttk.Scale(speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=speed_x_var)
speed_x_slider.grid(row=0, column=2, padx=5, pady=5)

speed_y_label = ttk.Label(speed_frame, text="Speed Y:")
speed_y_label.grid(row=1, column=0, padx=5, pady=5)
speed_y_entry = ttk.Entry(speed_frame, textvariable=speed_y_var)
speed_y_entry.grid(row=1, column=1, padx=5, pady=5)
speed_y_slider = ttk.Scale(speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=speed_y_var)
speed_y_slider.grid(row=1, column=2, padx=5, pady=5)

# Specify the size of the image
image_size = (200, 200)

# Initialize screensaver parameters
logo = None
logoSpeed = default_speed
logoRect = None

# Update the Tkinter window
config_window.update_idletasks()
config_window.update()

# Start the Tkinter event loop
config_window.mainloop()

