from colorLibs.ColorParser import ColorParser
from smartLight import LightController
from structures.CappedQueue import CappedQueue
from common.utils import get_fps
import threading


class SenderOrchestrator(threading.Thread):
    def __init__(self, colorQueue: CappedQueue, c: LightController) -> None:
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName(self.__class__.__name__)
        self.colorQueue = colorQueue
        self.color = ColorParser()
        self.controller = c

    def send_procedure(self):
        colors = self.colorQueue.get()
        self.controller.set_brightness(colors.get("brightness", 125))
        try:
            self.controller.set_temperature(colors.get("colortemp", 2000))
        except:
            pass
        self.controller.apply()

    def run(self):
        self.controller.configure()
        while True:
            self.send_procedure()
