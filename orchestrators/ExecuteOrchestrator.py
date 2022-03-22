import threading
import queue
from colorLibs.ColorParser import ColorParser
from smartLight import LightController


class ExecuteOrchestrator(threading.Thread):
    def __init__(self, q: queue.Queue, c: LightController) -> None:
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName(self.__class__.__name__)
        self.q = q
        self.color = ColorParser()
        self.controller = c

    def run(self):
        while True:
            image = self.q.get()
            bright = self.color.get_brightness(image)
            temp = self.color.get_temperature(image)
            self.controller.set_brightness(bright)
            self.controller.set_temperature(temp)
