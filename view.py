import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
import sys

class View:
    def __init__(self, controller):
        self.controller = controller
        self.model = controller.model
        self.screenWidth, self.screenHeight = 1000, 800
        self.backgroundColor = (0, 0, 0)
        self.default_speed = [2, 2]
        self.image_size = (200, 200)

        self.config_window = tk.Tk()
        self.config_window.title("Zen Screensaver Settings")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TButton', background='#4CAF50', foreground='white')
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0')

        self.image_frame = ttk.Frame(self.config_window)
        self.image_frame.pack(pady=10)

        self.browse_button = ttk.Button(self.image_frame, text="Browse Image", command=self.configure_screensaver)
        self.browse_button.pack(side=tk.LEFT, padx=10)

        self.selected_image_label = ttk.Label(self.image_frame, text="No image selected")
        self.selected_image_label.pack(side=tk.LEFT)

        self.speed_frame = ttk.Frame(self.config_window)
        self.speed_frame.pack(pady=10)

        self.speed_x_var = tk.IntVar(value=self.default_speed[0])
        self.speed_y_var = tk.IntVar(value=self.default_speed[1])

        self.speed_x_label = ttk.Label(self.speed_frame, text="Speed X:")
        self.speed_x_label.grid(row=0, column=0, padx=5, pady=5)
        self.speed_x_entry = ttk.Entry(self.speed_frame, textvariable=self.speed_x_var)
        self.speed_x_entry.grid(row=0, column=1, padx=5, pady=5)
        self.speed_x_slider = ttk.Scale(self.speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.speed_x_var)
        self.speed_x_slider.grid(row=0, column=2, padx=5, pady=5)

        self.speed_y_label = ttk.Label(self.speed_frame, text="Speed Y:")
        self.speed_y_label.grid(row=1, column=0, padx=5, pady=5)
        self.speed_y_entry = ttk.Entry(self.speed_frame, textvariable=self.speed_y_var)
        self.speed_y_entry.grid(row=1, column=1, padx=5, pady=5)
        self.speed_y_slider = ttk.Scale(self.speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.speed_y_var)
        self.speed_y_slider.grid(row=1, column=2, padx=5, pady=5)

        self.config_window.update_idletasks()
        self.config_window.update()

    def configure_screensaver(self):
        speed_x = self.speed_x_var.get()
        speed_y = self.speed_y_var.get()
        image_size = self.image_size
        success = self.controller.configure_screensaver(image_size, speed_x, speed_y)
        if success:
            self.config_window.withdraw()
            self.show_zen_screen()

    def show_zen_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("Zen Screens")

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(self.backgroundColor)

            if self.model.logo:
                if self.model.logoRect is None:
                    self.model.logoRect = self.model.logo.get_rect(center=(self.screenWidth // 2, self.screenHeight // 2))
                screen.blit(self.model.logo, self.model.logoRect)
                self.model.logoRect = self.model.logoRect.move(self.model.logoSpeed)
                if self.model.logoRect.left < 0 or self.model.logoRect.right > self.screenWidth:
                    self.model.logoSpeed[0] = -self.model.logoSpeed[0]
                if self.model.logoRect.top < 0 or self.model.logoRect.bottom > self.screenHeight:
                    self.model.logoSpeed[1] = -self.model.logoSpeed[1]

            pygame.display.flip()
            clock.tick(60)
