import pygame
import sys
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Model
class ScreenSaverModel:
    def __init__(self):
        self.configuration = {
            'duration': 300,  # default duration in seconds
            'visuals': []     # list of selected visuals
        }
        self.idle_time = 0

    def update_configuration(self, duration, visuals):
        self.configuration['duration'] = duration
        self.configuration['visuals'] = visuals

    def set_idle_time(self, idle_time):
        self.idle_time = idle_time

# View
class ScreenSaverView:
    def __init__(self):
        self.config_window = tk.Tk()
        self.config_window.title("Zen Screensaver Settings")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('TButton', background='#4CAF50', foreground='white')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0')

        self.image_frame = ttk.Frame(self.config_window)
        self.image_frame.pack(pady=10)

        self.browse_button = ttk.Button(self.image_frame, text="Browse Image", command=self.configure_screensaver)
        self.browse_button.pack(side=tk.LEFT, padx=10)

        self.selected_image_label = ttk.Label(self.image_frame, text="No image selected")
        self.selected_image_label.pack(side=tk.LEFT)

        self.speed_frame = ttk.Frame(self.config_window)
        self.speed_frame.pack(pady=10)

        self.speed_x_var = tk.IntVar(value=2)
        self.speed_y_var = tk.IntVar(value=2)

        self.speed_x_label = ttk.Label(self.speed_frame, text="Speed X:")
        self.speed_x_label.grid(row=0, column=0, padx=5, pady=5)
        self.speed_x_slider = ttk.Scale(self.speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.speed_x_var)
        self.speed_x_slider.grid(row=0, column=1, padx=5, pady=5)

        self.speed_y_label = ttk.Label(self.speed_frame, text="Speed Y:")
        self.speed_y_label.grid(row=1, column=0, padx=5, pady=5)
        self.speed_y_slider = ttk.Scale(self.speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.speed_y_var)
        self.speed_y_slider.grid(row=1, column=1, padx=5, pady=5)

        self.image_size = (200, 200)

    def configure_screensaver(self):
        global logo, logoRect, logoSpeed

        image_path = self.browse_image_path()
        if os.path.isfile(image_path):
            logo = self.load_image(image_path, self.image_size)
        else:
            print(f"Error: The file '{image_path}' does not exist.")
            return

        speed_x = self.speed_x_var.get()
        speed_y = self.speed_y_var.get()
        logoSpeed = [speed_x, speed_y]

        self.config_window.withdraw()
        self.show_zen_screen()

    def browse_image_path(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def load_image(self, image_path, size):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)

    def show_zen_screen(self):
        global logo, logoRect, logoSpeed

        screen = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption("Zen Screens")

        logoRect = pygame.Rect((screenWidth // 2 - self.image_size[0] // 2, screenHeight // 2 - self.image_size[1] // 2), self.image_size)

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(backgroundColor)

            if logo:
                screen.blit(logo, logoRect)
                logoRect = logoRect.move(logoSpeed)

                if logoRect.left < 0 or logoRect.right > screenWidth:
                    logoSpeed[0] = -logoSpeed[0]
                if logoRect.top < 0 or logoRect.bottom > screenHeight:
                    logoSpeed[1] = -logoSpeed[1]

            pygame.display.flip()
            clock.tick(60)

# Controller
class ScreenSaverController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_user_input(self):
        duration = 600
        visuals = ['visual1', 'visual2']
        self.model.update_configuration(duration, visuals)

    def update_model_idle_time(self, idle_time):
        self.model.set_idle_time(idle_time)

    def trigger_screen_saver(self):
        print("Triggering screen saver...")

# Main function
def main():
    model = ScreenSaverModel()
    view = ScreenSaverView()
    controller = ScreenSaverController(model, view)

    controller.handle_user_input()

    idle_time = 120
    controller.update_model_idle_time(idle_time)

    controller.trigger_screen_saver()

if __name__ == "__main__":
    # Pygame initialization
    pygame.init()

    screenWidth, screenHeight = 1000, 800
    backgroundColor = (0, 0, 0)

    default_speed = [2, 2]

    logo = None
    logoSpeed = default_speed
    logoRect = None

    main()
