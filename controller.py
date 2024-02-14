from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def configure_screensaver(self, image_size, speed_x, speed_y):
        return self.model.configure_screensaver(image_size, speed_x, speed_y)
