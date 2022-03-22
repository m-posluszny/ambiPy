from colorLibs.ColorParser import ColorParser
from common.utils import get_fps
from smartLight import LightController
import threading
import queue


class ExecuteOrchestrator(threading.Thread):
    def __init__(self, q: queue.Queue, c: LightController, compression=50) -> None:
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName(self.__class__.__name__)
        self.q = q
        self.color = ColorParser()
        self.controller = c
        self.compression = compression

    @get_fps
    def procedure(self):
        image = self.q.get()
        image = self.color.resize_image(image, self.compression)
        rgb = self.color.get_rgb_mean(image)
        bright = self.color.get_brightness(rgb)
        # temp = self.color.get_temperature(rgb)
        self.controller.set_brightness(bright)
        # self.controller.set_temperature(temp)

    def run(self):
        self.controller.configure()
        while True:
            self.procedure()
