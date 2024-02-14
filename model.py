import pygame
import os
import tkinter as tk
from tkinter import filedialog

class Model:
    def __init__(self):
        self.logo = None
        self.logoRect = None
        self.logoSpeed = [2, 2]

    def load_image(self, image_path, size):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)

    def browse_image_path(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename()
        return file_path

    def configure_screensaver(self, image_size, speed_x, speed_y):
        image_path = self.browse_image_path()
        if os.path.isfile(image_path):
            self.logo = self.load_image(image_path, image_size)
        else:
            print(f"Error: The file '{image_path}' does not exist.")
            return False
        self.logoSpeed = [speed_x, speed_y]
        return True
